# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:10300@192.168.3.74:50014/temp'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class User(db.Model):
    #__tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(32),unique = True)
    password = db.Column(db.String(32))

    def __init__(self,username, password):
        self.username = username
        self.password = password

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def isExisted(self):
        #tempUser = User.query(User).filter(username = self.username,password = self.password).first()
        tempUser = db.session.query(User).filter(User.username == self.username,User.password == self.password).first()
        if tempUser == None:
            return 0
        else:
            return 1


class Entry(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text)
    sender = db.Column(db.String(32))
    def __init__(self,content,sender):
        self.content = content
        self.sender = sender

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

def getAllEntry():
    Entlist = []
    Entlist = Entry.query.filter_by().all()
    #Entlist = db.session.query(Entry).filter().all()
    return  Entlist