#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Package: cli.py
Author: ^-^
-----
cli module for deploy.
Require scrapyenv.
'''

import time
import subprocess
import click
from os import path
from xutil import xjson
from xutil.xprint import iprint

import deploy

# TODO: add machine alias host map

PATH_HERE = path.dirname(path.abspath(__file__))
PROJECT = path.basename(PATH_HERE)

@click.group()
def main():
    pass

@main.command()
@click.option('--targets', '-t', multiple=True,
              help='-t target1 -t target2 ...')
@click.option('--conf_file', '-c',
              help='config file, *.json')
def dp(targets, conf_file):
    '''
    Deploy the project.
    '''
    if not targets:
        iprint('require targets!, exit', color='r')
    deploy.deploy(targets, conf_file)

@main.command()
@click.option('--target', '-t')
@click.option('--conf_file', '-c',
              help='config file, *.json')
def pdp(target, conf_file):
    '''
    pre deploy project, e.g. gen setting.
    '''
    if not target:
        iprint('require target!, exit', color='r')
    deploy.pre_deploy(target, conf_file)

if __name__ == '__main__':
    main()
