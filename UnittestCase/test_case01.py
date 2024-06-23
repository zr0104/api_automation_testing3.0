# coding=utf-8
import sys
import os
#base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
import unittest
sys.path.append('../')
from Base.base_request import request
url = "http://test.portal.lvdatong.com/#/index"
data = {
    "username":"qgs0051@lvdatong.com",
    "password":"12345678"
}
class TestCase01(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    @classmethod
    def setUpClass(cls):
        print("从>>>------------->case类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("到>>>------------->case类执行结束")

    #@unittest.skip("这个case_07不执行，跳过")
    def test_07(self):
        print("执行case07")
        flag = "abcdefghijklmnwwwwwww"
        s = "fads"
        self.assertIn(s,flag,msg="flag不包含s")

    host = "http://test.portal.lvdatong.com/#/index"

    @unittest.skip("跳过这条case_01用例")
    def test_01(self):
        print("执行case01")
        #res = requests.get(url=url,params=data).json()
        data1 = {
            "user":"11111"
        }
        self.assertDictEqual(data1,data)

    @unittest.skip("这个case_02不执行，跳过")
    def test_02(self):
        print("执行case02")
        data1 = {
            "username": "88@lvdatong.com",
            "password": "123456"
        }
        self.assertDictEqual(data1,data,msg="这两个字典不相等")

    @unittest.skip("这个case_03不执行，跳过")
    def test_03(self):
        print("执行case03")
        flag = True
        self.assertFalse(flag,msg="不等于True")

    @unittest.skipIf(4<5,"这个case_04不执行，跳过")
    def test_04(self):
        print("执行case04")
        flag = False
        self.assertTrue(flag,msg="不等于False")

    @unittest.skipIf(host == "http://test.portal.lvdatong.com/#/index","这个case_05不执行，跳过")
    def test_05(self):
        print("执行case05")
        flag = "1111"
        flag1 = "2222"
        self.assertEqual(flag,flag1,msg="这两个str不相等")

    def test_06(self):
        res = request.run_main('get',url,data)
        print(res)


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    '''
    suite.addTest(TestCase01('test_06'))
    suite.addTest(TestCase01('test_04'))
    suite.addTest(TestCase01('test_05'))
    suite.addTest(TestCase01('test_03'))
    suite.addTest(TestCase01('test_01'))
    suite.addTest(TestCase01('test_02'))
    suite.addTest(TestCase01('test_07'))
    '''
    tests = [TestCase01('test_07'),TestCase01('test_02'),TestCase01('test_06'),TestCase01('test_05'),TestCase01('test_01'),TestCase01('test_03'),TestCase01('test_04')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
