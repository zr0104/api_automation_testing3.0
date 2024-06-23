#coding=utf-8
#selenium web
import requests
import json
import time
from selenium import webdriver
cookie1 = {
    "apsid":""
}
driver = webdriver.Chrome()
driver.get("https://coding.imooc.com/")
time.sleep(5)
driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.find_element_by_name("email").send_keys("873892325@qq.com")
driver.find_element_by_name("password").send_keys("13457588q")
driver.find_element_by_class_name("moco-btn").click()
time.sleep(3)
cookie = driver.get_cookies()
for i in cookie:
    if i['name'] == 'apsid':
        cookie1['apsid'] = i['value']
print(cookie1)
driver.close()

download_url = 'https://www.imooc.com/user/postpic'
file = {
    "fileField":("imooc2.jpg",open("D:/Sen/imooc2.jpg"),"image/jpg"),
    "type":"1"
}
res = requests.post(url=download_url,files=file,cookies=cookie1,verify=False).text
print(res)
