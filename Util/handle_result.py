#coding=utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import json
from Util.handle_json import get_value
from deepdiff import DeepDiff
#print(get_value("api3/getbanneradvertver2","/Config/code_message.json"))
'''[
        {"1006": "token error"},
        {"10001": "用户名错误"},
        {"10002": "密码错误"}
    ]'''

def handle_result(url,code):
    #print("------>",code,"------>",type(code))
    data = get_value(url,"/Config/code_message.json")
    if data !=None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def get_result_json(url,status):
    data = get_value(url,"/Config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

def handle_result_json(dict1,dict2):
    '''
    校验格式
    '''
    #判断是不是字典类型isinstance(字段,类型)
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        #dict1={"aaa":"AAA","bbb":"BBBB","CC":[{"11":"22"},{"33":"44"}]}
        #dict2={"aaa":"123","bbb":"456","CC":[{"11":"111"},{"33":"44"}]}
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == '__main__':
    dict2={"aaa":"ddd","aaa1":"A1A","bbb":"BBBB","CC":[{"11":"22"},{"33":"44"}]}
    dict1={"aaa":"AAA","bbb":"BBBB","aaa3":"A1A","CC":[{"11":"111"},{"33":"44"}]}
    #print(handle_result('api3/getbanneradvertver2',"1006"))
    #print(handle_result_json(dict1,dict2))
    print(get_result_json("http://test.passport.be.lvdatong.com/sso/login","code"))
