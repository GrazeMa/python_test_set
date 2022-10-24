#!/usr/bin/python
# -*- coding: utf-8 -*-

# 基础的 URL 地址
TestSavanaBaseUrl = 'https://qa-api-cb.snsports.cn'

# 类似 Router 的部分，跟在 baseUrl 后
ApiRouterUrl = '/api'
# XXRouterUrl = '/xx'

# 列举需要请求的具体 API 的 URL
# 自己测试接口
GRAZER_TEST_URL = '{}{}/GrazerTest.json'.format(TestSavanaBaseUrl, ApiRouterUrl)
# 登出接口
UN_REGISTER_URL = '{}{}/UnRegister.json'.format(TestSavanaBaseUrl, ApiRouterUrl)
