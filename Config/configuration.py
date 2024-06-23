import logging
import configparser
from pytz import timezone


class Config(object):
    LOGIN_KEY = "'OTBQDg8NDtSNtGGw35IKevckBrigRBR6a4qpn5WWq6s='"
    LOGIN_USERNAME = "'gAAAAABkL8LgsC6naquVyXsTPVS8NxvcnFsflh33G7LYaALc6DA8pRU1S8ZxuwCsWe-pLUO9gUtc1N0ujoYJvLDa_whKUjPMTQ=='"
    LOGIN_PASSWORD = "'gAAAAABkL8dd-YJ_CPuwZpt0sI25GL1sLTRA_fqSzKgEb5aaww8_Pllz9LXXPTj1BALbUpGa-icWppeo2G8hWEi6QsdaJFra5Q=='"


class MXConfig(Config):
    COOKIE_METHOD = 'yes'
    DATA_FILE = "icash_MX_api_testcase.xlsx"
    HOST = "https://icash-mexico-dev-cloud-gcp.mx.hsbc"
    LOGIN_URL = "https://icash-mexico-dev-cloud-gcp.mx.hsbc/icash-mexico/login"
    HEADER = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization": "Base NDUxNjk5NDg6shnIYOAYmdizMDI",
        "Host": "icash-mexico-dev-cloud-gcp.mx.hsbc",
        "appId":"5443534543",
        "applicationId": "BBDM"
      }


class HKConfig(Config):
    COOKIE_METHOD = 'yes'
    DATA_FILE = "icash_HK_api_testcase.xlsx"
    HOST = "https://icash-hk-sit.gcp.cloud.hk.hsbc"
    LOGIN_URL = "https://icash-hk-sit.gcp.cloud.hk.hsbc/login"
    HEADER = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization": "Base NDUxNjk5NDg6shnIYOAYmdizMDI",
        "Host": "icash-mexico-dev-cloud-gcp.mx.hsbc",
        "appId":"5443534543",
        "applicationId": "BBDM"
      }


class ASPConfig(Config):
    COOKIE_METHOD = 'yes'
    DATA_FILE = "icash_ASP_api_testcase.xlsx"
    HOST = "https://icash-mexico-dev-cloud-gcp.mx.hsbc"
    LOGIN_URL = "https://icash-mexico-dev-cloud-gcp.mx.hsbc/icash-mexico/login"
    HEADER = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization": "Base NDUxNjk5NDg6shnIYOAYmdizMDI",
        "Host": "icash-mexico-dev-cloud-gcp.mx.hsbc",
        "appId":"5443534543",
        "applicationId": "BBDM"
      }