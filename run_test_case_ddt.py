#coding=utf-8
import sys
import os
import ddt
import json
import urllib3
import time
import datetime
import schedule
import unittest
from Util.handle_excel import excel_data
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Base.base_request import request
from Util.handle_cookie import get_cookie_value,write_cookie
from Util.handle_header import get_header
from Util.codition_data import get_data
from Base.logger import MyLogging
from Base.send_email import send_email
from Util import HTMLTestRunner
from Base.send_email import send_email
from Util.handle_files import HandleFiles
from Util.request_token import GetCookie
from Config.configuration import MXConfig,HKConfig,ASPConfig
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
reportPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "Report"))
runPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "Run"))
sys.path.append(base_path)
http = urllib3.PoolManager(num_pools=50)
log = MyLogging().logger

tempPath = "/tmp/auto_check_report"
env_list = ['mx','hk','asp']
env = os.environ.get("AUTO_ENV", default=None)
# env = 'mx'
# print(env)

if not env or env not in env_list:
    raise ValueError("No correct environment key AUTO_ENV set for application")
if env == 'mx':
    config = MXConfig
elif env == 'hk':
    config = HKConfig
else:
    config = ASPConfig
log.info("application env: {}".format(config))
data = excel_data.get_excel_data(config.DATA_FILE)

@ddt.ddt
class TestCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        case_id = data[0]
        case_name = data[1]
        is_run = data[2]
        log = MyLogging().logger
        i = excel_data.get_rows_number(config.DATA_FILE, case_id)
        if is_run == 'yes' or is_run == "Yes":
            log.info("【Start executing the test case：{}】".format(case_name))
            is_depend = data[3]
            data1 = json.loads(data[7])
            # data1 = json.dumps(data[7]).strip()
            log.info("Request parameters: %s" %data1)

            try:
                if is_depend:
                    '''Get the depend(precondition)'''
                    depend_key = data[4]    #需要更新的依赖key_id
                    depend_data = get_data(is_depend)    #依赖前置分出res_data和rule_data
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]
                is_header = config.HEADER
                expect_method = data[8]
                expect_result = data[9]
                host = config.HOST
                cookie_req = GetCookie().request_cookie(config.HOST,config.HEADER)
                if cookie_req:
                    cookie = cookie_req
                if is_header:
                    header = config.HEADER
                
                res = request.run_main(method,url,data1,host,cookie,get_cookie,header)
                log.info("Return response：%s" % res)

                # #Determine whether the res response msg is equal to the msg of /Config/config.json # #
                if expect_method == 'msg' or expect_method == 'message':
                    res = json.loads(res.text)
                    res = res["{}".format(expect_method)]
                    print("response message >>>>>>", res)
                    expect_result = json.loads(expect_result)
                    expect_result = expect_result["{}".format(expect_method)]
                    print("expect message >>>>>>", expect_result)
                    try:
                        self.assertEqual(res,expect_result)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                        raise e

                # #Determine whether the code of the response result is equal to the code of excel # #
                if expect_method == 'code' or expect_method == 'Code':
                    res = json.loads(res.text)
                    code = res["{}".format(expect_method)]
                    # print("response message >>>>>>", res)
                    expect_result = json.loads(expect_result)
                    expect_result = expect_result["{}".format(expect_method)]
                    # print("expect message >>>>>>", expect_result)
                    print("Check point data{}: {}, return data: {}".format(i, expect_result, code))
                    try:
                        if len(res) or res["code"]:
                            self.assertEqual(expect_result, code)
                            log.info("Check point data{}: {}, return data: {}".format(i, expect_result, code))
                            excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                            excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, code))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                        raise e

                # # Determine wheter the res response code status and the code of excel are equal # #
                if expect_method == 'status_code' or expect_method == 'Status_code' or expect_method == 'Status_Code':
                    status_code = res.status_code # res.status_code
                    expect_result = int(expect_result)
                    res = json.loads(res.text)
                    print("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                    try:
                        self.assertEqual(status_code, expect_result)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                        raise e

                # # for download api judge # #
                if expect_method == 'status_codes' or expect_method == 'Status_codes' or expect_method == 'Status_Codes':
                    status_code = res.status_code  # res.status_code
                    expect_result = int(expect_result)
                    # res = json.loads(res.text)
                    print("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                    try:
                        self.assertEqual(status_code, expect_result)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res.text, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, status_code))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res.text, ensure_ascii=False))
                        raise e

                # # Determine wheter the res response code status and the code of excel are equal # #
                if expect_method == 'true' or expect_method == 'True' or expect_method == 'TRUE':
                    res = json.loads(res.text)
                    print("Return data: {}".format(i, res))
                    try:
                        self.assertTrue(res)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                        raise e

                # # for download api judge # #
                if expect_method == 'trues' or expect_method == 'Trues' or expect_method == 'TRUES':
                    # res = json.loads(res.text)
                    print("Return data: {}".format(i, res.text))
                    try:
                        self.assertTrue(res.text)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res.text))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res.text, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, res.text))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res.text, ensure_ascii=False))
                        raise e

                # # Determine wheter the res response code status and the code of excel are equal # #
                if expect_method == 'json' or expect_method == 'Json' or expect_method == 'JSON':
                    res = json.loads(res.text)
                    expect_result = json.loads(expect_result)
                    result = handle_result_json(expect_result, res)
                    print("Check point data{}: {}, return data: {}".format(res, expect_result, result))
                    try:
                        self.assertTrue(res.text)
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, result))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Pass")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        log.info("Check point data{}: {}, return data: {}".format(i, expect_result, result))
                        excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                        excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(res, ensure_ascii=False))
                        raise e

            except Exception as e:
                excel_data.excel_write_data(config.DATA_FILE, i, 11, "Fail")
                excel_data.excel_write_data(config.DATA_FILE, i, 12, json.dumps(e, ensure_ascii=False))
                raise e

        elif is_run == "no" or is_run == "No" or is_run == "N0":
            log.info("Skip execution testcase: %s" % case_name)
            excel_data.excel_write_data(config.DATA_FILE, i, 11, "Skip")
            self.skipTest("Skip execution testcase!")

    # 1: 加载测试用例
    def run_all_test(self):
        suite = unittest.TestLoader().discover(start_dir=base_path, pattern="run_test_case_*.py", top_level_dir=None)
        now = time.strftime("%Y-%m-%d")
        #  测试报告路径
        # file_name = os.path.join(tempPath) + "/" + now + "_{}_report.html".format(env)
        file_name = os.path.join(reportPath) + "/" + now + "_{}_report.html".format(env)
        # print("filename..................",file_name)
        with open(file_name, "wb") as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="{} Automation Test Report".format(env),
                                                   description="Environment：window 10 Browser：Chrome")
            runner.run(suite)
        f.close()

    # 3:获取最新的测试报告
    def get_report(self,report_path):
        list = os.listdir(report_path)
        list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
        print("Test report：", list[-1])
        report_file = os.path.join(report_path, list[-1])
        return report_file

    # def get_report(self,tempPath):
    #     list = os.listdir(tempPath)
    #     list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
    #     print("测试报告：", list[-1])
    #     report_file = os.path.join(tempPath, list[-1])
    #     return report_file

    def run_case(self):
        TestCaseDdt().run_all_test()

    def handle_report_and_log(self):
        handle_file = HandleFiles()
        filenameLog = os.path.join(base_path + "/logs/")
        # filenameReport = os.path.join(basePath + "/Report/")
        # # print(filenameLog,filenameReport)
        handle_file.delete_files(filenameLog)
        # handle_file.delete_files(filenameReport)

        handle_file.delete_files(tempPath)

    # 4:发送邮件
    def send_mail(self,subject, report_file, file_name):
        #  读取测试报告内容，作为邮件的正文内容
        with open(report_file, "rb") as f:
            mail_body = f.read()
        TestCaseDdt().send_mail(subject, mail_body, file_name)

    def get_email_body(self,report_file):
        #  读取测试报告内容，作为邮件的正文内容
        with open(report_file, "rb") as f:
            mail_body = f.read()
        return mail_body

    def send_report_to_email(self):
        report_path = os.path.join(base_path, "Report")  # 测试报告路径
        report_file = TestCaseDdt().get_report(report_path)  # 测试报告文件
        email_body = TestCaseDdt().get_email_body(report_file)
        subject = "{} - api test report".format(env)  # 邮件主题
        file_names = [report_file]  # 邮件附件
        # 发送邮件
        send_email(subject, email_body, file_names)

if __name__ == '__main__':
    '''
    run = TestCaseDdt()
    run.test_main_case(data)
    '''
    start_timestamp = datetime.datetime.now() + datetime.timedelta(minutes=1)
    start_timestamp = datetime.datetime.strftime(start_timestamp, '%H:%M:%S')
    schedule.every().day.at(start_timestamp).do(TestCaseDdt().run_case)
    start_timestamp1 = datetime.datetime.now() + datetime.timedelta(days=15)
    start_timestamp1 = datetime.datetime.strftime(start_timestamp1, '%H:%M:%S')
    schedule.every().day.at(start_timestamp1).do(TestCaseDdt().handle_report_and_log)
    start_timestamp2 = datetime.datetime.now() + datetime.timedelta(minutes=5)
    start_timestamp2 = datetime.datetime.strftime(start_timestamp2, '%H:%M:%S')
    schedule.every().day.at(start_timestamp2).do(TestCaseDdt().send_report_to_email)

    while True:
        schedule.run_pending()


