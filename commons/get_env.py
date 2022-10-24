#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入第三方包
import os
import sys


# 获得当前的环境（用以区分环境 LOCAL/QA/PROD/TEST……）
# 注：使用此方法必须要在 Edit Configurations... 中进行 Parameters 参数的配置！
def get_env_from_parameters():
    # print(f'sys.argv[1]: {sys.argv[1]}')
    return sys.argv[1]


# 注：使用此方法必须要在 Edit Configurations... 中进行 Environment --> Environment variables 参数的配置！
def get_env_from_environment():
    # print(f'os.getenv("ENVIRONMENT"): {os.getenv("ENVIRONMENT")}')
    return os.getenv('ENVIRONMENT')


if __name__ == '__main__':
    get_env_from_parameters()
    get_env_from_environment()
