_RE_MD5 = re.compile(r'^[0-9a-f]{32}$')

@api

@post('/api/users')

def register_user():

    i = ctx.request.input(name='', email='', password='')

    name = i.name.strip()

    email = i.email.strip().lower()

    password = i.password

    if not name:

        raise APIValueError('name')

    if not email or not _RE_EMAIL.match(email):

        raise APIValueError('email')

    if not password or not _RE_MD5.match(password):

        raise APIValueError('password')

    user = User.find_first('where email=?', email)

    if user:

        raise APIError('register:failed', 'email', 'Email is already in use.')

        user = User(name=name, email=email, password=password, image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email).hexdigest())

        user.insert()

        return user

# 注意用户口令是客户端传递的经过MD5计算后的32位Hash字符串，所以服务器端并不知道用户的原始口令。
#
# 接下来可以创建一个注册页面，让用户填写注册表单，然后，提交数据到注册用户的API：

{% extends '__base__.html' %}

{% block title %}注册{% endblock %}

{% block beforehead %}

function check_form() {undefined

$('#password').val(CryptoJS.MD5($('#password1').val()).toString());

return true;

}

{% endblock %}

{% block content %}

# 欢迎注册！
# 名字:
#
# 电子邮件:
#
# 输入口令:
#
# 重复口令:
#
# 注册

{% endblock %}

Try