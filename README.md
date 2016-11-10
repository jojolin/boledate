# boledate

## run
> - set your own redis config in "./parse_items.py" and "./conf-release.json"
> - run `python ./cli.py` to see how to setup project.
> - run `scrapy crawl boledate -a debug-item='{{url@@title}}'` to run on debug-mode
> - run `scrapy crawl boledate` to read urls from redis.

## structures
> - cli.py: command interface
> - gensetting.py
>   - setting.py.tplt
>   - generate setting, should be re-written by specific project
> - genspider.py
>   - spider.py.tplt
>   - generate spider, should be re-written by specific project
> - deploy.py: do deploy
>   - conf-xx.json: config

## scrapy-project
> - extensions
>   - throttle.py
>   - xcontextfactory.py
>   - xrfpdupefilter.py
> - middlewares
>   - monitormiddleware.py
>   - proxymiddleware.py
>   - timeoutmiddleware.py
>   - xmiddleware.py
> - pipelines
>   - bufferpipeline.py: buffer commit logic
>   - mysqlpipeline.py: mysql logic
>   - redispipeline.py: redis logic
>   - xpipeline.py: template
> - spiders
>   - spiderbase.py: base spider
>   - cmdlinebase.py: command line base
>   - redisbase.py: redis base
>   - xspider.py: template

