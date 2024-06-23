#-*- coding=utf8 -*-

# @author:sololi

# date: 2020/11/3

# 文件说明 :

import sys

def register(username,password):#登录功能，且与存储用户表的文本文件进行比较

#验证用户名

shuju=readfile()

jg1 = 0

i = 0

while (i < len(shuju)):

    if (username == shuju[i]["用户名"]):

        print("用户名正确")

        jg1 = 1

        break

    i += 1

    # 用户名错误将不再验证密码

    if (jg1 != 1):

        print("用户名错误")

    # 验证密码

    if (jg1 == 1):

        jg2 = 0

        i = 0

while (i < len(shuju)):

    if (password == shuju[i]["密码"]):

        print("密码正确")

        jg2 = 1

        break

    i += 1

    if (jg2 != 1):

        print("密码错误")

        def logon(username):#注册功能，且以正确格式存入文本文件

        shuju=readfile()

        jg3 = 0

    i = 0

while (i < len(shuju)):

    if (username == shuju[i]["用户名"]):

        print("用户名已经存在")

    jg3 = 1

    break

    i += 1

    if(jg3 == 0):

while True:

password = input("请输入注册的密码(密码不能小于6位，且不能为纯数字)")

if (str.isdigit(password)==1) or (len(password)<6):

print("密码格式错误")

else:

break

passwordagain=input("请再次确认密码")

while True:

if(password==passwordagain):

break

else:

print("两次密码不一致")

passwordagain = input("请再次确认密码")

# 将注册的用户信息存储到文本文件中

f = open("data", mode='a+', encoding="utf8")

if shuju == []:

f.write("用户名:{},密码:{}".format(username, password))

if shuju != []:

f.write("\n用户名:{},密码:{}".format(username, password))

print("注册成功")

f.close()

def readfile():#将数据转换成列表字典形式，放在data.txt中便于后面登录与注册存放数据

f = open('data', "r+", encoding="utf8")

shuju = []

b = []

aa = {}

for line in f.readlines():

line = line.strip('\n')

a = line.split(' ')

i = 0

while i < len(a):

b = a[i].split(',')

i += 1

j = 0

while j < len(b):

if b == " ":

break

c = b[j].split(':', 1)

aa[c[0]] = c[1]

i += 1

j += 1

shuju.append(aa.copy()) # copy是为了防止添加是数据类型不同出错

f.close()

return shuju

while True:

    choice=input("登录输入1,注册输入2,其他任意键退出")

    if choice=="1":

        id=input("输入您的账号")

        pw=input("输入您的密码")

        register(id,pw)

        break

    if choice=="2":

        id=input("输入你注册的账号")

        logon(id)

        continue

    else:

        print("退出成功")

    sys.exit(0)