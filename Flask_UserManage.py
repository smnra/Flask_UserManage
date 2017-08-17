# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request,redirect
from wtforms import Form,TextField,PasswordField,validators
from db import *
app = Flask(__name__)

class LoginForm(Form):
    username = TextField('username',[validators.Required()])
    password = PasswordField('password',[validators.Required()])
@app.route('/login',methods = ['GET','POST'])
def login():
    myform = LoginForm(request.form)
    if request.method =='POST':
        if myform.username.data == 'SMnRa' and myform.password.data == '123456' and myform.validate():
            return render_template('user.html',form = myform)
        else:
            return render_template('login.html',message = '用户名或密码错误!',form = myform)
    return render_template('login.html',form = myform)


@app.route('/register',methods = ['GET','POST'])
def register():
    myform = LoginForm(request.form)
    if request.method == 'POST':
        addUser(myform.username.data,myform.password.data)
        return render_template('login.html',message = "注册成功!",form = myform)
    return render_template('login.html',form = myform)





if __name__ == '__main__':
    app.run(debug=True,port=80)