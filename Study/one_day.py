# coding=utf-8
import requests
from param_dict.param_d import SetGlobal
import time

class Requests():
    def __init__(self,driver):
        self.driver = driver
        self.gr = SetGlobal()

    def get_request(self):

        #获取ssesionId
        url1 = "http://test.passport.be.lvdatong.com/sso/login"
        # #获取Ticket
        url2 = "http://test.passport.be.lvdatong.com/sso/generateTicket"
        # #获取token,登录CRM
        # url3 = "http://test.portal.be.lvdatong.com/security/getToken"

        # (1,2,3,4,5)
        data1 = 'b+AfD/aAX0FKMTIyzAkY6Qwls6FNADhrVoN2ZPcWc8NN2bB6ZDAkL2URNHyKSla/FGXGcA9bRbT7lbs41afjIhfMDHnGeUe+AnygOPIwbK/Ry9b8vSGrV6aekih1ZF9vr6EGSuvMKrkW1Afu8IvFE1hGfBUCetYNFB0f02Hf7Vsgjp4vmbv4HW9aEY7tQcGA3M5Pd2lddTwiA+JHA3K/RQimXD+ycD5YcUxYMGGQkQHnkLBQZrWh/NrhJJbyWLEH+WplHkXRetu3pdSbpEQEBEKpNNOdbvTlJ7mVJISddvwnZF64eagIniGz4UrprXStFEuegkPT6wqmXJBvxhCWGQ=='
        data2 = {
            'sessionId':'${sessionId}'
        }
        # data3 = {
        #     'ticket':'${ticket}',
        #     'uuid':'09F6B3E6356E4881D6494F9A60C19E22'
        # }

        #requests.get(url)
        res1 = requests.post(url1,data1).text
        print(res1)

        self.gr.resolve_global_var(pre_resolve_var=data2,global_var_dic=res1)
        #print(result)

        time.sleep(2)
        # list1 = res1.split(',')[2]
        # print(list1)
        # text1 = list1.split(":")[2]
        # print(text1)
        res2 = requests.post(url2,data2).text
        print(res2)
        # res3 = requests.post(url3,data3).text
        # print(res3)

if __name__ == '__main__':
    Requests.get_request(self='')