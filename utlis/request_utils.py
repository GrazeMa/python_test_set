#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入第三方包
import requests


# GET 请求
def get_req(url, params=None):
    # 发送 GET 请求
    r = requests.get(url=url, params=params, verify=False, timeout=2)
    # 返回请求结果
    return r.text


# POST 请求
def post_req(url, headers=None, form_data=None, json=None):
    # 默认的 Header
    init_headers = {'content-type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    # 若传入的参数 headers 不为空，则合并到默认的 Header 中
    if headers:
        init_headers.update(headers)
    # 发送 POST 请求
    r = requests.post(url=url, headers=init_headers, data=form_data, json=json, verify=False, timeout=2)
    # 返回请求结果
    return r.text
