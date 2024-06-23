#coding=utf-8
import sys
import os
import schedule
basePath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(basePath)
import time
import datetime
import unittest
from Util import HTMLTestRunner
from Base.send_email import send_email
from Util.handle_files import HandleFiles

# 获取当前py文件的绝对路径
basePath1 = os.path.abspath(os.path.join(os.path.dirname(__file__)))
tempPath = "/tmp/auto_check_report"
# print(basePath1,tempPath)

# 1: 加载测试用例
def all_test():
    case_path = os.path.join(basePath1, "Run")
    suite = unittest.TestLoader().discover(start_dir=case_path, pattern="run_case_*.py", top_level_dir=None)
    return suite


# 2:执行测试用例
def run():
    now = time.strftime("%Y-%m-%d")
    #  测试报告路径
    file_name = os.path.join(basePath1, "Report") + "/" + now + "_report.html"
    with open(file_name, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Sen接口自动化测试报告", description="环境：window 10 浏览器：chrome")
        runner.run(all_test())
    f.close()

# def run():
#     now = time.strftime("%Y-%m-%d")
#     #  测试报告路径
#     if not os.path.exists(tempPath):
#         os.makedirs(tempPath)
#     file_name = os.path.join(tempPath) + "/" + now + "_report.html"
#     with open(file_name, "wb") as f:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Sen接口自动化测试报告", description="环境：window 10 浏览器：chrome")
#         runner.run(all_test())
#     f.close()


# 3:获取最新的测试报告
def get_report(report_path):
    list = os.listdir(report_path)
    list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
    print("测试报告：", list[-1])
    report_file = os.path.join(report_path, list[-1])
    return report_file

# def get_report(tempPath):
#     list = os.listdir(tempPath)
#     list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
#     print("测试报告：", list[-1])
#     report_file = os.path.join(tempPath, list[-1])
#     return report_file

def run_case():
    run()
    
def handle_report():
    handle_file = HandleFiles()
    # filenameLog = os.path.join(basePath + "/logs/")
    # filenameReport = os.path.join(basePath + "/Report/")
    # # print(filenameLog,filenameReport)
    # handle_file.delete_files(filenameLog)
    # handle_file.delete_files(filenameReport)

    handle_file.delete_files(tempPath)

# 4:发送邮件
def send_mail(subject, report_file, file_name):
    #  读取测试报告内容，作为邮件的正文内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    send_mail(subject, mail_body, file_name)

def get_email_body(report_file):
    #  读取测试报告内容，作为邮件的正文内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    return mail_body

def send_report_to_email():
    report_path = os.path.join(basePath1, "Report")  # 测试报告路径
    report_file = get_report(report_path)  # 测试报告文件
    email_body = get_email_body(report_file)
    subject = "Sen-接口测试报告"  # 邮件主题
    file_names = [report_file]  # 邮件附件
    # 发送邮件
    send_email(subject, email_body, file_names)

if __name__ == "__main__":
    # run()
    # report_path = os.path.join(basePath1, "Report")  # 测试报告路径
    # report_file = get_report(report_path)  # 测试报告文件
    # email_body = get_email_body(report_file)
    # subject = "Sen-接口测试报告"  # 邮件主题
    # file_names = [report_file]  # 邮件附件
    # # 发送邮件
    # send_email(subject, email_body, file_names)

    # run job every 1 days
    start_timestamp = datetime.datetime.now() + datetime.timedelta(minutes=1)
    start_timestamp = datetime.datetime.strftime(start_timestamp, '%H:%M:%S')
    schedule.every().day.at(start_timestamp).do(run_case)

    # start_timestamp1 = datetime.datetime.now() + datetime.timedelta(days=10)
    # start_timestamp1 = datetime.datetime.strftime(start_timestamp1, '%H:%M:%S')
    # schedule.every().day.at(start_timestamp1).do(handle_report)

    # start_timestamp2 = datetime.datetime.now() + datetime.timedelta(minutes=1)
    # start_timestamp2 = datetime.datetime.strftime(start_timestamp2, '%H:%M:%S')
    # schedule.every().day.at(start_timestamp2).do(send_report_to_email)

    while True:
        schedule.run_pending()


