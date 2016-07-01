# coding=utf-8
from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField, PasswordField
from wtforms.validators import Required


class UploadForm(Form):
    file = FileField("选择图片上传")
    submit = SubmitField("确认上传")


class SearchForm(Form):
    code = StringField("股票代码： ", validators=[Required()])
    submit = SubmitField("search")
    
    
class SignupForm(Form):
    username = StringField("用户名：")
    
    id = StringField("身份证号：")
    phone = StringField("手机号：")
    password = PasswordField("密码：")
    submit = SubmitField("注册：")