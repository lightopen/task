# coding=utf-8
from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import Required


class UploadForm(Form):
    file = FileField("选择图片上传")
    submit = SubmitField("确认上传")


class SearchForm(Form):
    code = StringField("股票代码： ", validators=[Required()])
    submit = SubmitField("search")