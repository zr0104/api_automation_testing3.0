import requests
import urllib3
import os
import json
from urllib import request
import re
import certifi
from Util.handle_json import get_value
from Util.Fernet import FernetEncrdecr
from Util.handle_header import get_header
from Config.configuration import Config,MXConfig,HKConfig,ASPConfig
basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
urllib3.disable_warnings()


class GetCookie():
    def request_cookie(self, host, headers):
        """get cookie"""
        Cookies = {}
        username = FernetEncrdecr().decrdecr(Config.LOGIN_KEY.encode(), Config.LOGIN_USERNAME.encode())
        password = FernetEncrdecr().decrdecr(Config.LOGIN_KEY.encode(), Config.LOGIN_PASSWORD.encode())
        # print(key, username[0], password[0])
        params = "username={},password={},passwordType=PASSWORD".format(username[0], password[0])
        result = requests.post(host, data=params, headers=headers, verify=False)

        # print(result)
        # print(result.text)
        # print(result.status_code)
        # print(result.cookies)

        res_cookies = result.cookies
        res_cookies_value = res_cookies.get("JSESSIONID")
        Cookies["is_cookie"] = res_cookies_value
        # print(res_cookies_value)
        # print(Cookies)
        return Cookies


if __name__ == '__main__':
    get_cookie = GetCookie()
    host = "https://icash-mexico-dev-cloud-gcp.mx.hsbc"
    headers = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization": "Base NDUxNjk5NDg6shnIYOAYmdizMDI",
        "Host": "icash-mexico-dev-cloud-gcp.mx.hsbc",
        "appId":"5443534543",
        "applicationId": "BBDM"
      }
    print(get_cookie.request_cookie(host, headers))

