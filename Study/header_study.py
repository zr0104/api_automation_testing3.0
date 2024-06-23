# coding=utf-8
import requests
import json
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_4073b7a3908263ba859ba85f4867a37a=1616902644,1616939912,1617457614,1617511921; nb-referrer-hostname=test.wbfwtop.com; sessionId=98AF09DC9F10479CA75592A91072F88A; Hm_lpvt_4073b7a3908263ba859ba85f4867a37a=1617524753; nb-start-page-url=https%3A%2F%2Ftest.wbfwtop.com%2Findex.html',
    'Host':'test.wbfwtop.com',
    'Referer':'https://test.wbfwtop.com/pages/view/service-detail.html?productCode=pd_28953652',
    'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
res = requests.get("https://test.wbfwtop.com/pages/user-center/order-confirm.html?checkoutCode=C1617524770503849429&operation=create",headers=header,verify=False).json()
print(res)