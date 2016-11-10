#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
import jieba
import json
import copy

def stastic(s):
    ls = jieba.cut(s)
    st = {}
    for x in ls:
        if x =='':
            continue
        elif x == '\n':
            continue
        st.setdefault(x, 0)
        st[x] += 1
    return st

def load_data(filep):
    jss = []
    with open(filep, 'r') as r:
        for l in r.readlines():
            jss.append(json.loads(l))
    return jss

def most_like(jjs, topn):
    print '='*5, 'most like', '='*5
    x = copy.deepcopy(jjs)
    x.sort(key=lambda x:int(x['like']), reverse=True)
    return x[:topn]

def most_collect(jjs, topn):
    print '='*5, 'most collect', '='*5
    x = copy.deepcopy(jjs)
    x.sort(key=lambda x:int(x['collect']), reverse=True)
    return x[:topn]

def get_girls_pics(jjs):
    pics = []
    for js in jjs:
        pics += js['picturls']
    return pics

def analyze_demand(jjs):
    def _c(js):
        js_ = [x for x in js['content'] if not x.strip() =='']
        return [x.split(u'：')[1] if x.find(u'：') > -1 else '' for x in js_[-3:]]

    ss = [' '.join(_c(x)) for x in jjs]
    return stastic(''.join(ss))

def main():
    filep = sys.argv[1]
    minnum, maxnum = 0, 10000
    try:
        minnum = int(sys.argv[2])
        maxnum = int(sys.argv[3])
    except:
        pass

    jjs = load_data(filep)
    for x in most_like(jjs, 10):
        print "like: ", x['like'], "picturls: ", x["picturls"][:1]

    for x in most_collect(jjs, 10):
        print "collect: ", x['collect'], "picturls: ", x["picturls"][:1]

    for x in get_girls_pics(jjs)[:10]:
        print x

    st = analyze_demand(jjs)
    for k, v in st.items():
        if int(v) > minnum and int(v) <= maxnum:
            print k, v

if __name__ == '__main__':
    main()

