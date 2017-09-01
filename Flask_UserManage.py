# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request,redirect
from wtforms import Form,TextAreaField,StringField,PasswordField,validators
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from model import *





app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(Form):                                          #定义前端form表单
    username = StringField('username',[validators.Required()])
    password = PasswordField('password',[validators.Required()])
class EntryForm(Form):                                          #定义前端form表单
    content = TextAreaField('content',[validators.Required()])
    sender = StringField('sender',[validators.Required()])


@app.route('/login',methods = ['GET','POST'])
def login():
    myform = LoginForm(request.form)
    if request.method =='POST':
        us = User(myform.username.data,myform.password.data)
        if (us.isExisted()):
            return render_template('user.html',form = myform)
        else:
            return render_template('login.html',message = '用户名或密码错误!',message2 = '登陆', form = myform)
    return render_template('login.html',message2 = '登陆',form = myform)


@app.route('/register',methods = ['GET','POST'])
def register():
    myform = LoginForm(request.form)
    if request.method == 'POST':
        us = User(myform.username.data,myform.password.data)
        us.add()
        return render_template('login.html',message = "注册成功!", message2 = '注册', form = myform)
    return render_template('login.html',message2 = '注册',form = myform)

@app.route('/entry',methods = ['GET', 'POST'])
def entry():
    myForm = EntryForm(request.form)
    entryList = getAllEntry()
    if request.method == 'POST':
        e = Entry(myForm.content.data, myForm.sender.data)
        e.add()
        return  render_template('entry.html',entries = entryList, form = myForm)
    return  render_template('entry.html',entries = entryList, form = myForm )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500










if __name__ == '__main__':
    app.run(debug=True,port=80)