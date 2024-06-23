#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import json
from Util.handle_json import get_value,read_json,write_value
#1.获取cookie
#2.写入cookie
#3.携带cookie
def get_cookie_value(cookie_key):
    '''
    获取cookie
    '''
    data = read_json("/Config/cookie.json")
    return data[cookie_key]

def write_cookie(data,cookie_key):
    '''
    写入cookie
    '''
    data1 = read_json("/Config/cookie.json")
    data1[cookie_key] = data
    write_value(data1)


if __name__ == '__main__':
    data = {
        "is_cookie":"A945D8C5DB5C40A9B7E02025FD019DD1"
    }
    print(data["is_cookie"])
    print(write_cookie(data,'web'))
    print(get_cookie_value("web"))
