#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from urllib.request import urlopen, Request
import gzip
import lxml.html
from lxml import etree
import shutil


def get_request(url):
    request = Request(
        url=url,
        data=None,
        headers={
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
        })
    return request


def get_lxml_from_response(response):
    if response.info().get('Content-Encoding') == 'gzip':
        f = gzip.GzipFile(fileobj=response)
        return lxml.html.document_fromstring(f.read())
    else:
        return lxml.html.document_fromstring(response.read())


# Get list of 100 proxies
request = get_request("https://www.sslproxies.org/")
response = urlopen(request)
tree = get_lxml_from_response(response)
rows = tree.xpath("//tr/td/text()")

shutil.copy('haproxy.cfg.template', 'haproxy.cfg')
with open('haproxy.cfg', 'a') as conf_file:
    for i in range(100):
        host_index = 8 * i
        proxy = f'{rows[host_index]}:{rows[host_index + 1]}'
        conf_file.write(f'    server proxy-{i} {proxy} check\n')