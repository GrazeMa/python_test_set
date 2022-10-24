#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入第三方包
import json


# 通用方法：获得 JSON 字符串中第一层某参数的值
def get_val(json_str, param_name):
    # 将 JSON 字符串转为 dict 类型
    json_obj = json.loads(json_str)
    # 返回所需参数的值，若无此参数则返回空字符串
    return json_obj.get(param_name, '')


# 常用取值参数的封装
# 获得返回 JSON 中的 code 参数值
def get_code(json_str):
    return get_val(json_str, 'code')


# 获得返回 JSON 中的 messages 参数值
def get_msg(json_str):
    return get_val(json_str, 'messages')


# 获得返回 JSON 中的 (messages.)data 参数值
def get_data(json_str):
    return get_msg(json_str).get('data', {})
