# -*- coding: utf-8 -*-
'''
Package: deploy.py
Author: ^-^
-----
deploy module.
'''
from os import path
import re
import subprocess
from ConfigParser import ConfigParser

from xutil import xjson
from xutil.xprint import iprint

import gensetting

PATH_HERE = path.dirname(path.abspath(__file__))
PROJECT = path.basename(PATH_HERE)

def deploy(targets, conf_file):
    for t in targets:
        host = get_target_host(t)
        version = get_project_version()
        pre_deploy(t, conf_file)
        iprint(do_deploy(t, version), 'deploy result', 'y')

def pre_deploy(target, conf_file):
    host = get_target_host(target)
    gen_setting(host, conf_file)

def do_deploy(target, version=None):
    if version:
        return subprocess.check_output('cd %s && scrapyd-deploy %s --version=%s' % (PROJECT, target, version), shell=True)
    else:
        return subprocess.check_output('cd %s && scrapyd-deploy %s' % (PROJECT, target), shell=True)

def gen_setting(host, conf_file):
    setting_dir = path.join(PATH_HERE, '%s/%s' % (PROJECT, PROJECT))
    save_file =  path.join(setting_dir, 'setting.py')
    config = xjson.loadf(conf_file)
    config.update({'host': host})
    gensetting.gen(config, save_file)

def get_project_version():
    return get_version_git()
    # return get_version_svn()

def get_version_svn():
    output = subprocess.check_output("svn info | grep Revision | awk -F: '{print $2}'")
    # (status, output) = commands.getstatusoutput("svn info | grep Revision | awk -F: '{print $2}'")
    return output.strip() if status in ('0', 0) else ''

def get_version_git():
    num_v = subprocess.check_output('git rev-list HEAD | wc -l', shell=True)
    commit_v = subprocess.check_output('git rev-list HEAD -n 1 | cut -c 1-7', shell=True)
    return '%sv%s' % (num_v.strip(), commit_v.strip())

def get_target_host(target):
    cfg_file = path.join(PATH_HERE, '%s/scrapy.cfg' % PROJECT)
    cf = ConfigParser(allow_no_value=True)
    cf.read(cfg_file)
    url = cf.get('deploy:%s' % target, 'url')
    return re.search('://([0-9.]+):', url).group(1)
