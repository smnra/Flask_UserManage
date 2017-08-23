# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request,redirect
from wtforms import Form,StringField,PasswordField,validators
from model import *
app = Flask(__name__)

class LoginForm(Form):
    username = StringField('username',[validators.Required()])
    password = PasswordField('password',[validators.Required()])

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





if __name__ == '__main__':
    app.run(debug=True,port=80)