from flask import render_template, redirect, url_for, request, abort

import models.UserModel as UserModel

def index():
    # Execute command to select all from database
    # for example you run : select * from table in SQL and save result in res variable
    users = UserModel.get()
    data = {
        'users' : users
    }
    return render_template('index.html',data=data)

def store():
    name = request.form.get('name')
    data = {
        'name' : name
    }
    return render_template('post.html',data=data)

def show(user_id):
    user = UserModel.getById(user_id)
    print(user)
    data = {
        'user' : user
    }
    return render_template('user.html',data=data)
