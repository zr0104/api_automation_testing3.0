# coding=utf-8
import requests
import json
url = 'https://www.imooc.com/apiw/logo?callback=jQuery2100784114534733817_1560664870423&_=1560664870424'
data = {
    'v':'5.1.2',
    'v_code':'5120',
    'token':'5c1d2b3f9ac501dc8a5c2345bd7b9603',
    'uuid':'41b650ef846688193728ff7381eb6c1c',
    'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiZTIxNmY0OWMzZGQ2NmQwZTVjNzNiZDE4ZDI2MmJjOTciLCJkZXZpY2UiOiJtb2JpbGUifQ.gm0p9UKTfosbv4buUlD1u5d0-T2EtXNd5QQUe9ZlHe0',
    'app_id':'1',
    'plat_id':'2',
    'timestamp':'1560660339989',
    'uid':'7213561',
    'type':'0'
}
res_text = requests.get(url,verify=False).text


download_url = 'http://www.imooc.com/user/postpic'
file = {
    "fileField":("test.jpg",open("D:/Sen/test.jpg","rb"),"image/jpg"),
    "type":"1"
}
res = requests.post(url=download_url,files=file,verify=False).text
#print(res)

try:
    #res_text = json.loads(res_text)
    res = json.loads(res)
    print("----------->",type(res))
except:
    print("解析失败")

    #print(res_text)
    print("----------------------------")
    print(res)