# -*- coding: utf-8 -*-
import time
import logging
from twisted.internet.error import TimeoutError
import scrapy

class ProxyClient(object):

    def get_proxy(self, domain, num):
        '''
        get proxy
        @return:
        [(ip, port)]
        '''
        # TODO: add get_proxy logic
        ip = ''
        port = 1234
        ua = ''
        return [(ip, port, ua)]

    def feedback_proxy(self, domain, ip, port, state):
        logging.info('feedback proxy, domain:%s, ip:%s, port:%s, state:%s' \
                     % (domain, ip, port, state))
        # TODO: add feedback_proxy logic

class ProxyMiddleware(object):
    def __init__(self):
        self.pxy_cli = ProxyClient()

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            return
        # !! we comment the follow because when there's no pxy_cli available,
        # it's better throw exception then passing the request quiet.
        # if not self.pxy_cli:
        #     return
        self._set_new_req_proxy(request)

    def process_response(self, request, response, spider):
        banned_times_limit = request.meta['banned_times_limit']
        if self._is_banned(response):
            req = request
            logging.info('banned, url %s' % req.url)
            self.inc_meta_value(req, 'banned-times')
            if req.meta['banned-times'] > banned_times_limit:
                raise scrapy.exceptions.IgnoreRequest('banned')
            # feedback
            pxystr = req.meta['proxy']
            proxy_domain = req.meta['proxy_domain']
            ip, port = self._extract_proxy(pxystr)
            self._feedback_proxy(proxy_domain, ip, port)

            self._set_new_req_proxy(req)
            return req

        return response

    def inc_meta_value(self, request, meta_key):
        if meta_key in request.meta:
            request.meta[meta_key] += 1
        else:
            request.meta[meta_key] = 1

    def _set_new_req_proxy(self, req):
        proxy_domain = req.meta['proxy_domain']
        ip, port, ua = self._get_proxy(proxy_domain)
        req.meta['proxy'] = self._format_proxy(ip, port, 'http')
        req.headers['user-agent'] = ua

    def _get_proxy(self, proxy_domain):
        resp = self.pxy_cli.get_proxy(proxy_domain, 1)
        if resp is None:
            logging.info('get proxy failed, retry')
            time.sleep(0.5)
            resp = self.pxy_cli.get_proxy(proxy_domain, 1)
        if resp is None:
            logging.info('get proxy failed, retry')
            time.sleep(0.5)
            resp = self.pxy_cli.get_proxy(proxy_domain, 1)
        if resp is None:
            logging.info('get proxy failed!')
        pxy_uas = resp.proxy_uas[0]
        return (ip, port, ua)

    def _feedback_proxy(self, proxy_domain, ip, port):
        self.pxy_cli.feedback_proxy(proxy_domain, ip, port, state= 'banned' )

    def _is_banned(self, response):
        # TODO: add banned logic
        return False

    def _format_proxy(self, ip, port, tp='http'):
        '''
        tp - 'http' or 'https'
        '''
        return '%(tp)s://%(ip)s:%(port)s' % {'tp': tp, 'ip':ip, 'port':port}

    def _extract_proxy(self, proxystr):
        '''
        http://{PROXY_IP}:{PORT}
        '''
        x1 = proxystr.find('//')+2
        x2 = proxystr.find(':', x1)
        x3 = len(proxystr)
        ip = proxystr[x1: x2]
        port = proxystr[x2+1: x3]
        return (ip, port)