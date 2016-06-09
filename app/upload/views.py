# coding=utf-8
from . import upload
from flask import render_template, url_for, request
from .. import db, bootstrap, basedir
from ..models import Image
from ..forms import UploadForm
import os
from werkzeug.security import gen_salt


folder = os.path.join(basedir, 'static', 'images') # 图片保存的文件夹

# 验证上传文件类型是否为支持格式图片
def file_is_allowed(filename):
    img_type = ['png','jpg','jpeg','gif']
    type = filename.split('.')[-1]
    if type in img_type:
        return True
    return False


# 图片保存在static/images文件夹下，数据表images保存生成的图片名，以备后面图片展示用
@upload.route("/", methods=["GET", "POST"])
def img_upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = request.files['file']
        if file_is_allowed(f.filename):
            # 生成一组十位字符串作为服务器文件名，防止用户图片名重复
            filename = gen_salt(10)+"."+f.filename.split('.')[-1]

            f.save(os.path.join(folder, filename))
            image = Image(filename=filename)
            db.session.add(image)
            db.session.commit()
            return render_template("upload/success.html")
        return render_template("upload/fail.html")
    return render_template('upload/upload.html', form=form)


# 以列表的形式展示已上传的图片，没有链接指向本页面
@upload.route("/show")
def show():
    images = Image.query.all()
    return render_template("upload/show.html", images=images)





