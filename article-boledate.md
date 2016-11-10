# 11.11就要来啦！！程序猴猴们，除了剁手，瞧瞧女生们都想要什么男人吧（里面有福利）！！
- 宅惯了的技术男们，看看女生心里都怎么想的，赶紧加油努力吧！
- 本文以数据分析的角度，通过抓取“博乐在线”的[相亲模块](http://date.jobbole.com/)来分析女生都是什么想的。
- 如果有合适的，赶紧注册联系吧。时间不多了！！！
- 本着授人以渔的态度，为了广大同胞们的终身幸福。分析结果下面附带核心代码。全部代码可从[个人github](https://github.com/jojolin)下载。
- 由于时间有限，该项目仍需改善优化，相关文档说明后续补上^_^。

## 关键字
- 网页抓取，统计分析，图片一览

## 我们的目标
1 分析女生们的具体需求
3 提供女生图片一览（福利啊)
4 提供详情页浏览
5 看看其他男人的眼光(收藏数和喜欢数)	

## 等不及了，先看结果吧
- 本次总共抓取的女生征友贴共有402条，看了这个统计结果，作者表示知道该往哪个方向努力了:)
- 从最喜欢和收藏数来看，猴哥猴弟们的眼光还是很不错的喔:)
- 从部分图片链接来看，多人喜欢和多人收藏的妹子部分已经被领走了，所以，还单身的狗狗们，快快出手...
- 40以上的结果抽烟很显眼啊。各位，为了健康和幸福，有的就戒了吧。

```
402 /tmp/boledate-data.json
```

### 女生的要求（部分）
``` 40~ 
抽烟 50
交往 44
本科 41
责任心 45
身高 99
生活 47
喜欢 42
希望 81
```

``` 20~40
上进心 34
善良 22
遇到 23
175 21
170 36
成熟 30
稳重 22
定居 21
彼此 21
了解 26
性格 24
```

``` 10~20
专一 11
打算 11
工作 20
吸烟 17
包容 15
阳光 15
担当 19
脾气好 15
努力 18
三观 11
身体健康 15
真诚 17
责任感 15
不良嗜好 16
开朗 11
运动 19
人品 18
孝顺 17
乐观 11
学历 16
积极 11
互相 15
```

### 看看男生们的眼光
``` 前10个最多喜欢。
===== most like =====
like:  392 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabjw1f6vf3qusbaj20e80iygm5.jpg']
like:  287 picturls:  [u'http://ww3.sinaimg.cn/mw690/e9ef8eabgw1ezprv9c2l9j20qo0zkgxz.jpg']
like:  242 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f0ngkg2ophj20no0vkmzt.jpg']
like:  165 picturls:  [u'http://ww4.sinaimg.cn/mw690/e9ef8eabgw1f5ps2tnmecj20f40egq4l.jpg']
like:  150 picturls:  [u'http://ww3.sinaimg.cn/mw690/e9ef8eabgw1f5zjroxptuj20no0vkwkq.jpg']
like:  149 picturls:  [u'http://ww3.sinaimg.cn/mw690/e9ef8eabgw1exw9z6egslj20m810ogoy.jpg']
like:  146 picturls:  [u'http://ww4.sinaimg.cn/mw690/e9ef8eabjw1f6vfj8rj7mj20d20hfmy1.jpg']
like:  143 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabjw1f6vfodiwd7j20qo0qo43f.jpg']
like:  138 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f4gr7ch134j20qo0zk44h.jpg']
like:  138 picturls:  [u'http://ww1.sinaimg.cn/mw690/e9ef8eabgw1f3q5cmc5pqj207l0dimy2.jpg']
```

``` 前10个最多收藏
===== most collect =====
collect:  144 picturls:  [u'http://ww3.sinaimg.cn/mw690/e9ef8eabgw1ezprv9c2l9j20qo0zkgxz.jpg']
collect:  137 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabjw1f6vf3qusbaj20e80iygm5.jpg']
collect:  108 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f0ngkg2ophj20no0vkmzt.jpg']
collect:  69 picturls:  [u'http://ww4.sinaimg.cn/mw690/e9ef8eabgw1f5ps2tnmecj20f40egq4l.jpg']
collect:  63 picturls:  []
collect:  62 picturls:  [u'http://ww1.sinaimg.cn/mw690/e9ef8eabgw1evzw9xw4n1j20n40f778l.jpg']
collect:  62 picturls:  []
collect:  60 picturls:  [u'http://ww4.sinaimg.cn/mw690/e9ef8eabgw1er7bhn1pqbj20i50r8aeo.jpg']
collect:  57 picturls:  [u'http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f5prknuf28j208e0b7dg2.jpg']
collect:  56 picturls:  [u'http://ww3.sinaimg.cn/mw690/e9ef8eabgw1f5zjroxptuj20no0vkwkq.jpg']
```

### 女生图片一览
``` 一小部分
http://ww2.sinaimg.cn/small/e9ef8eabgw1f9cmeonhvjj205k07fwee.jpg
http://ww4.sinaimg.cn/mw690/e9ef8eabgw1f9cly41wahj20vm18y0y2.jpg
http://ww1.sinaimg.cn/mw690/e9ef8eabgw1f9cly50e7yj20xr1900ys.jpg
http://ww4.sinaimg.cn/mw690/e9ef8eabgw1f9cm5pknmsj20qo0zkmzr.jpg
http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f9cm5qba52j20hs0npmyp.jpg
http://ww1.sinaimg.cn/mw690/e9ef8eabgw1f9clst51ogj21hc1hch4s.jpg
http://ww1.sinaimg.cn/mw690/e9ef8eabgw1f9clstzbxoj20qo0zkwji.jpg
http://ww2.sinaimg.cn/mw690/e9ef8eabgw1f9clss2f4rj21401hck5k.jpg
http://ww4.sinaimg.cn/mw690/e9ef8eabgw1f9bakvmwpmj20u014041s.jpg
http://ww1.sinaimg.cn/mw690/e9ef8eabgw1f9hhxs9fh1j20g003y3zf.jpg
```

## 实现

### 准备
- python编程语言
- 开源框架scrapy
- 网络模块requests
- 缓冲对列redis
- jieba分词

### 工具包
- 基于ubuntu14.04
- 安装python2.7，pip等[具体参考](https://www.python.org/)
- `pip install requests`，模块， 爬取数据用[具体参考](http://www.scrapy.org/)
- `pip install scrpay`，爬虫模块，爬取数据用[具体参考](http://www.scrapy.org/)
- `pip install jieba`，中文分词模块，统计分析用，[具体参考](https://github.com/fxsjy/jieba)
- `pip install redis`, 中间队列[具体参考](https://pypi.python.org/pypi/redis/)

### 代码实现
- 实现逻辑
  - 独立进程a爬取所有条目的url和title并push到中间队列redis
  - scrapy爬虫从redis队列中读取url并爬取详情页，同时写入json文件供后续分析
  - 统计分析模块读取json文件，读取女生要求，用jieba分词并做统计分析
  - 分析脚本读取女生所有图片链接做展示
  - 分析脚本根据喜欢数和收藏数排序，并根据升／降序进行展示

- 实现所有条目的抓取，独立脚本。
``` parse_items.py
# ...

def get_nxt_pg_url(tree):
    nxt_url = tree.xpath('//li[@id="pagination-next-page"]/a/@href')
    return nxt_url[0] if nxt_url else None

def parse_items(tree):
    items = tree.xpath('//li[@class="media"]//h3[@class="p-tit"]/a')
    for u in items:
        tit = u.xpath('text()')[0]
        url = u.xpath('@href')[0]
        yield (url,  tit)
    nxt_pg_url = get_nxt_pg_url(tree)
    if nxt_pg_url:
        time.sleep(CRAWL_INTERVAL)
        for i in parse_items(get_page_tree(nxt_pg_url)):
            yield i

def parse(st_url):
    tree = get_page_tree(st_url)
    items = parse_items(tree)
    server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD)   
    for url, tit in items:
        server.lpush(REDIS_KEY, '@@'.join([url, tit]))
        print 'push item to redis: %s' % tit
		
# ...
```

- [相亲详情贴](http://date.jobbole.com/3629/)，确定需要的字段（我特地选了个很漂亮的女生哦！）
``` items.py
    iid = scrapy.Field()           # 标识字段
    title = scrapy.Field()         # 标题
    content = scrapy.Field()       # 相亲内容
    picturls = scrapy.Field()      # 图片链接
    like = scrapy.Field()          # 喜欢数
    collect = scrapy.Field()       # 收藏数
    launch_time = scrapy.Field()   # 发布时间
    place = scrapy.Field()         # 籍贯
```

- 爬虫爬取逻辑
``` datespider.py
# ...
    def ex_items(self, response):
        # TODO: extract items
        items = []
        item = BoledateItem()
        title = response.css('li.media > div.media-body > h1::text').extract()[0]
        if title.find(u'］') > -1:
            return []

        launch_time = response.css('li.media > div.media-body > p.p-meta > span::text').extract()[0]
        place = response.css('li.media > div.media-body > p.p-meta > span > a::text').extract()[0]
        content = response.css('div.p-entry > p::text').extract()
        picturls = response.css('div.p-entry > p > img::attr(src)').extract()
        like, collect = '0', '0'
        try:
            like = response.css('div#share-buttons > a')[0].css('h10::text').extract()[0]
        except IndexError:
            like = '0'
        try:
            collect = re.search('\d+', \
                    ''.join(response.css('div#share-buttons > a')[1].css('::text').extract())).group(0)
        except Exception:
            collect = '0'

        item['iid'] = title
        item['title'] = title
        item['content'] = content
        item['picturls'] = picturls
        item['like'] = like
        item['collect'] = collect
        item['launch_time'] = launch_time
        item['place'] = place
        items.append(item)
        return items
# ...
```

- scrapy管道jsonfilepipeline.py，写入到json文件中。
``` jsonfilepipeline.py
# ...
    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), encoding='utf-8')+'\n')
        return item
# ...
```

- 分析，独立脚本。
``` statistics.py
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
```

