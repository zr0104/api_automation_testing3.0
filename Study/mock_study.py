#coding=utf-8
import mock
import requests
import unittest
url = "http://www.imooc.com/login"
data = {
    "username":"13246821387",
    "password":"123456"
}
def post_request(url,data):
    res = requests.post(url,data=data).json()
    print(res)

def get_request(url,data):
    #requests.post
    #url = "http://www.imooc.com/login/register?user=111&pass=222"
    #url + data
    res = requests.get(url,params=data).json()
    print(res)

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"13246821387"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("111222",res())

    def test_02(self):
        url = "http://www.imooc.com/login"
        data = {
            "username":"13246821387"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("111222",res())

    def test_03(self):
        url = "http://www.imooc.com/login"
        data = {
            "username":"13246821387"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("111222",res())

    def test_04(self):
        url = "http://www.imooc.com/login"
        data = {
            "username":"13246821387"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("111222",res())

    def test_05(self):
        url = "http://www.imooc.com/login"
        data = {
            "username":"13246821387"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("111222",res())

# if __name__ == '__main__':
#     unittest.main()