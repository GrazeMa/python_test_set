#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入第三方包
import commons.constants as cons
import configs.expected_req_res as exp
import configs.urls as url
import unittest
import utlis.json_utils as json_trans
import utlis.request_utils as req


# 断言检查返回码是否为 200
def assert_code_200(self, r):
    code = json_trans.get_code(r)
    # print(f'code_common: {code}')
    self.assertEqual(cons.CODE_200, code)


# 断言检查返回值是否为我们所期待的结果
def assert_data(self, r, expect):
    data = json_trans.get_data(r)
    # print(f'data: {data}')
    self.assertEqual(data, expect)


# 测试集
class MyTestCase(unittest.TestCase):

    # 测试 GET 请求全流程
    def test_get_req(self):
        r = req.get_req(url=url.GRAZER_TEST_URL, params={'param1': 'grazer'})
        # print(f'r: {r}')
        assert_code_200(self, r)
        assert_data(self, r, exp.TEST_GET_REQ)

    # 测试 POST 请求全流程
    def test_post_req(self):
        r = req.post_req(url=url.GRAZER_TEST_URL, form_data={'param1': 'grazer'})
        # print(f'r: {r}')
        assert_code_200(self, r)
        assert_data(self, r, exp.TEST_POST_REQ)


if __name__ == '__main__':
    unittest.main()
