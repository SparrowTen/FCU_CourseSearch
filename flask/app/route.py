from flask import render_template

def hello_world():
    return "Hello, MVC框架!"

def index():
    return render_template('index.html') 

def login():
    return render_template('login.html')

def register():
    return render_template('register.html')