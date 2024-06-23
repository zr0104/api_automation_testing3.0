# coding=utf-8
import sys
import os
import urllib3
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import json
import requests
from requests import utils
from Util.handle_json import get_value
from Util.handle_init import handle_ini
from Util.handle_cookie import write_cookie
from requests import utils
from Base.logger import MyLogging
log = MyLogging().logger

class BaseRequest:
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        '''发送post请求'''
        urllib3.disable_warnings()
        response = requests.post(url=url,data=data,cookies=cookie,headers=header,verify=False)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        # res = response.text
        res = response
        return res

    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        '''发送get请求'''
        urllib3.disable_warnings()
        response = requests.get(url=url,params=data,cookies=cookie,headers=header,verify=False)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        # res = response.text
        res = response
        return res

    def run_main(self,method,url,data,host,cookie=None,get_cookie=None,header=None):
        '''
        执行方法，传递method、url、data参数
        '''
        if 'http' not in url:
            url = host + url
        #print(url)
        log.info("Require url: %s" % url)
        if method == 'get' or method == 'Get' or method == 'GET':
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)
        try:
            # res = json.loads(res)
            #print("这个结果是一个json")
            res = res
        except:
            print("This result is a text.")
        #print("--->",res)
        return res


request = BaseRequest()
if __name__ == '__main__':
    request = BaseRequest()
    param = {"username":"11111", "password":"pwd123456"}
    print(request.run_main('get','/login/v1/download','hosthk',param))
