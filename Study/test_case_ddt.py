#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import ddt
import unittest
from Util.handle_excel import excel_data

data = excel_data.get_excel_data()
#data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]

@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")
    @ddt.data(*data)
    def test_01(self,data):
        # case编号 作用 是否执行 前置条件 依赖key url method data cookie操作 header操作 预期结果方式 预期结果 result response数据
        case_id,function,is_run,codition,depend_key,url,method,request_data,cookie,header,execpet_method,execpet,result,result_data = data
        #casename,casenum,isrun,method,cookie =data1
        print("this is sentest case",case_id,function,is_run,codition,depend_key,url,method,request_data,cookie,header,execpet_method,execpet,result,result_data)


if __name__ == '__main__':
    unittest.main()
