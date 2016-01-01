#!/usr/bin/env python2

import os.path
import urlparse
from email.utils import formatdate
from dulwich.repo import Repo
from dulwich.objects import Blob, Tree, Commit
from docutils import io, nodes
from docutils.core import publish_doctree, publish_from_doctree
from render import MyWriter

repo = Repo(".")
commit_sha = repo.head()
commit = repo.get_object(commit_sha)
index = repo.open_index()
assert not list(index.changes_from_tree(repo.object_store, commit.tree)), "uncommited changes"

store = repo.object_store


def render_rst(blob, path):
    doc = publish_doctree(blob.as_raw_string())
    for node in doc.traverse(nodes.reference):
        uri = urlparse.urlparse(node['refuri'])
        if not uri.netloc and os.path.basename(uri.path) == "README.rst":
            node['refuri'] = urlparse.urlunparse(
                (uri.scheme, uri.netloc, uri.path[:-10] or "./", uri.params, uri.query, uri.fragment))

    output = publish_from_doctree(
        doc,
        destination_path=path,
        writer=MyWriter(),
        settings_overrides = {
            'embed_stylesheet': False,
            'xml_declaration': False,
            'math_output': 'mathjax'})

    new_blob = Blob.from_string(output)
    store.add_object(new_blob)
    return new_blob.id


def render_tree(tree, path):
    new_tree = Tree()

    for entry in tree.items():
        item = repo[entry.sha]
        if isinstance(item, Tree):
            new_tree.add(entry.path, entry.mode, render_tree(item, path+(entry.path,)))
        elif isinstance(item, Blob):
            if entry.path.startswith(".") or ("." not in entry.path) or entry.path.endswith(".py"):
                continue
            if not entry.path.endswith(".rst"):
                new_tree.add(entry.path, entry.mode, entry.sha)
            else:
                name = "index.html" if entry.path == 'README.rst' else (entry.path[:-4]+".html")
                new_tree.add(name, entry.mode, render_rst(item, os.path.join(*(path +(name,)))))

    store.add_object(new_tree)
    return new_tree.id


new_commit = Commit()
new_commit.author = commit.author
new_commit.committer = commit.committer
new_commit.author_time = commit.author_time
new_commit.commit_time = commit.commit_time
new_commit.author_timezone = commit.author_timezone
new_commit.commit_timezone = commit.commit_timezone
new_commit.encoding = commit.encoding
new_commit.message = commit.message
new_commit.tree = render_tree(repo[commit.tree], ('.',))
store.add_object(new_commit)
repo['refs/heads/gh-pages'] = new_commit.id
