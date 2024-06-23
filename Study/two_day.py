#coding=utf-8
import requests
import json
#上传文件
#url = 'https://www.imooc.com/user/postpic'
download_url = 'https://www.imooc.com/mobile/downcount?source=web&type=android&r=1617522731213'
file = {
    "fileField":("test001.png",open("E:/python_data/image/test001.png","rb"),"image/png"),
    "type":"1"
}
cookie = {
    "apsid":"gyZDEwMzVmYjQzN2ZhNjhmZmNjZTg1NDgzNzY4NTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTIxNzEyMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4NzM4OTIzMjVAcXEuY29tAAAAAAAAAAAAAAAAAAAAADQxYWMyNjdmZWIwMDdkOTE0MWVlMDBlN2ZlZTQxYTYxvdllYL3ZZWA%3DZj"
}
res = requests.get(download_url)
with open("mukewang.apk","wb") as f:
    f.write(res.content)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)