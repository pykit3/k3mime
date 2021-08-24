#!/usr/bin/env python
# coding: utf-8

"""
Populate tmpl to a real repo
"""

import os
import re
import jinja2


def pjoin(*args):
    return os.path.join(*args)


def cp(fn):

    cur = os.path.abspath('.')
    name = os.path.split(cur)[1]

    t = '_building/tmpl/'
    relfn = fn[len(t):]
    base = os.path.split(fn)[0]
    if not os.path.exists(base):
        os.makedirs(base)

    src = fn
    dst = re.sub(r'xxnamexx', name, relfn)

    vs = {'name': name,
          'nameBig': name[0].upper() + name[1:],
          }

    print("populate ", src, " to ", dst)
    render_j2(src, vs, dst)

    os.unlink(src)


def render_j2(tmpl_path, tmpl_vars, output_path):
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader,
                                      undefined=jinja2.StrictUndefined)
    template = template_env.get_template(tmpl_path)

    txt = template.render(tmpl_vars)

    with open(output_path, 'w') as f:
        f.write(txt)


if __name__ == "__main__":
    for root, dirs, files in os.walk("_building/tmpl"):
        for fn in files:
            p = os.path.join(root, fn)
            cp(p)
