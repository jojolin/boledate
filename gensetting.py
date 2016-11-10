#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Package: gensetting.py
Author: ^-^
-----

'''

from os import path
from jinja2 import Template
from xutil import xjson

def gen(config, save_file=None, tplt_file='setting.py.tplt'):
    tplt = None
    with open(tplt_file, 'r') as r:
        tplt = Template(r.read())

    res = tplt.render(config=config)
    if not save_file:
        save_file = tplt_file.replace('.tplt','')

    with open(save_file, 'w') as w:
        w.write(res)

    print 'generate %s successfully!' % save_file

def test_gen():
    path_here = path.dirname(path.abspath(__file__))
    project = path.basename(path_here)
    setting_dir = path.join(path_here, '%s/%s' % (project, project))
    tplt_file =  path.join(setting_dir, 'setting.py.tplt')
    save_file =  path.join(setting_dir, 'setting_test.py')
    gen(tplt_file, save_file)

def main():
    pass
    # test_gen_config()

if __name__ == '__main__':
    main()
