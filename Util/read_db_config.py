# coding:utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
from pymysql import connect,cursors
from pymysql.err import OperationalError

#  读取DB数据库
# os.path.realpath(__file__):返回当前的绝对路径
# os.path.dirname(): 返回 () 所在目录
configPath = os.path.join((base_path+"/Config/db_config.ini"))  # 路径拼接 /config/db_config.ini
#print(configPath)
conf = configparser.ConfigParser()
conf.read(configPath, encoding="UTF-8")

host = conf.get("mysqlconf", "host")
port = conf.get("mysqlconf","port")
user = conf.get("mysqlconf", "user")
password = conf.get("mysqlconf","password")
port = conf.get("mysqlconf", "port")
