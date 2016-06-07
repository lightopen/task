from flask import render_template, url_for, flash
from .. import db
from . import spider
from ..forms import *
from ..models import *
from .info import get_info, for_model



@spider.route("/", methods=["GET", "POST"])
def search():
    form = SearchForm()
    info_list = {}
    code = ''
    image = ""
    if form.validate_on_submit():
        info_list, code, image= get_info(form.code.data)
        if info_list:
            for_model_d = for_model(info_list)
            print(len(for_model_d))
            value = Value(code=code, image=image, **for_model_d)
            db.session.add(value)
            db.session.commit()
            flash('查找成功')
        else:
            flash("查找失败")
    return render_template('spider/search.html', form=form, info_list=info_list, code=code, image=image)




