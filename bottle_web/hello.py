# -*- coding:utf-8 -*-

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

# http://localhost:8080/hello/aaa

