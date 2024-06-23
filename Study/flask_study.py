#f coding=utf-8
from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route('/')
def Home():
    data = json.dumps({
        "username":"13246821387",
        "password":"12345678"
    })

    return data
@app.route('/passport/user/login',methods=['GET'])
def Login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:

        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.wbfwtop.com"
        })
    else:
        data = json.dumps({
            "message":"请传递参数"
        })
    return data

@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登陆成功",
            "info":"www.test.wbfwtop.com"
        })
        # return data
    else:
        data = json.dumps({
            "message":"请求不合法"
        })
        # return data
    return data

#https://coding.imooc.com/passport/user/login?username=13246821387&password=12345678
#https://test.wbfwtop.com/security/commonLogin?userword=13246821387&password=12345678
if __name__ == '__main__':
    app.run()
