#!/usr/bin/env python2

import os
import os.path
import urlparse
from docutils import nodes, utils
from docutils.core import publish_cmdline
from docutils.writers.html4css1 import Writer, HTMLTranslator
from docutils.utils.math import unichar2tex, math2html


class MyHTMLTranslator(HTMLTranslator):

    doctype = "<!doctype html>\n"
    head_prefix_template = "<html>\n<head>\n"
    katex_url = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/"

    def __init__(self, document):
        HTMLTranslator.__init__(self, document)

    def script_call(self, path):
        path = utils.relative_path(self.settings._destination, path)
        return self.mathjax_script % self.encode(path)

    def visit_math(self, node, math_env=''):
        tag = ('div', 'span')[math_env == '']
        math_code = node.astext().translate(unichar2tex.uni2tex_table)
        start_tag = self.starttag(node, tag, suffix='\n', CLASS='formula', ALT=math_code)

        math2html.DocumentParameters.displaymode = (math_env != '')
        math_code = math2html.math2html(math_code)

        if self.math_output_options:
            self.katex_url = self.math_output_options[0]

        self.math_header = [
            self.stylesheet_call(utils.find_file_in_dirs("math.css", self.settings.stylesheet_dirs)),
            self.stylesheet_link % (self.katex_url + "katex.min.css"),
            self.mathjax_script % (self.katex_url + "katex.min.js"),
            self.script_call(utils.find_file_in_dirs("render.js", self.settings.stylesheet_dirs))
        ]

        self.body.append(start_tag)
        self.body.append(math_code)
        if math_env:
            self.body.append('\n')
        self.body.append('</%s>\n' % tag)
        raise nodes.SkipNode

    def visit_reference(self, node):
        uri = urlparse.urlparse(node['refuri'])
        if not uri.netloc and uri.path.endswith(".rst"):
            node['refuri'] = urlparse.urlunparse((uri.scheme, uri.netloc, uri.path[:-4]+".html", uri.params, uri.query, uri.fragment))
        return HTMLTranslator.visit_reference(self, node)


class MyWriter(Writer):
    def __init__(self):
        Writer.__init__(self)
        self.translator_class = MyHTMLTranslator

if __name__ == '__main__':
    publish_cmdline(writer=MyWriter())
