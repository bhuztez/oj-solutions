#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import os
import os.path
import sys
import re

def get_title(dirname,filename):
    with open(os.path.join(dirname,filename),'r') as f:
        f.readline()
        return f.readline().strip()

def make_tuple(dirname,link_fmt,pid,filename):
    return (pid,get_title(dirname,filename),link_fmt(pid),filename)

def match_names(exp,names):
    for name in names:
        match = re.match(exp, name)
        if not match:
            continue
        yield match.group(1)


def format_content(TITLE,items):
    pid_length = max(max(len(pid)+8 for pid,_,_,_ in items),12)
    title_length = max(max(len(title)+8 for _,title,_,_ in items),12)

    return "{title}\n{0} {1}\n问题代号{2} 解题报告\n{0} {1}\n{3}{0} {1}\n\n{4}\n".format(
        "="*pid_length,"="*title_length," "*(pid_length-8),
        "".join("{0:{width}} `{1}`__\n".format("`%s`__"%pid,title,width=pid_length) for pid,title,_,_ in items),
        "".join(".. __: {}\n.. __: {}\n".format(link,filename) for _,_,link,filename in items),
        title=TITLE
    )

def update_POJ():
    TITLE="===========\nPOJ解题报告\n===========\n"
    DIR="POJ"
    names = list(match_names(r'(\d+)\.rst', os.listdir(DIR)))
    names.sort()
    items = [make_tuple("POJ","http://poj.org/problem?id={}".format,n,n+".rst") for n in names]

    with open(os.path.join(DIR,"README.rst"),'w') as f:
        f.write(format_content(TITLE,items))

DIRS={"POJ":update_POJ}

def main(subdir):
    DIRS[subdir]()

if __name__ == '__main__':
    main(sys.argv[1])
