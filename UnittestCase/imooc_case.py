#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
#print(base_path)
#base_path = os.getcwd()
import unittest
import json
import mock
import HTMLTestRunner
from Base.base_request import request
def read_json():
    with open(base_path+"/Config/temp_data.json") as f:
        data = json.load(f)
        return data

def get_value(key):
    data = read_json()
    return data[key]


host = 'http://www.imooc.com/'
class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host+'/api3/getbanneradvertver2'
        data = {
            'timestamp': '1561269343481',
            'uid': '7213561',
            'token': '7ad09430cbaf927af642ab843ec374ef',
            'type': '1',
            'marking': 'androidbanner',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }
        mock_method = mock.Mock(return_value=get_value('/api3/getbanneradvertver2'))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1000)

    def beta4(self):
        url = host + 'api3/beta4'
        data = {
            'timestamp': '1561269343486',
            'uid': '7213561',
            'token': '66640986fb118dda4334719ac8afbf89',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY',
        }
        mock_method = mock.Mock(return_value=get_value('api3/beta4'))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1000)

    def test_new_register(self):
        username = '13211111'

        url = "register"
        data = {
            "user":username
        }

        #if res['errorCode'] == '10000':


    def test_old_register(self):
        url = "register"
        data = {
            "user":"11111"
        }


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_banner'))
    suite.addTest(ImoocCase('beta4'))
    file_path = base_path+'/Report/report.html'
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is Sen test",description="SenQ")
        runner.run(suite)
    f.close()
