#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, Response
app = Flask(__name__)

def root_dir():  # pragma: no cover
  return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
  try:
    src = os.path.join(root_dir(), filename)
    return open(src).read()
  except IOError as exc:
    return str(exc)

def count(start=0):
  while True:
    yield start
    start += 1
counter = count().next 

@app.route('/')
def hello_world():
  content = get_file('data/index.html')
  return Response(content, mimetype="text/html")

@app.route('/version')
def return_version():
  return os.environ['ENV']

@app.route('/healthz')
def return_healhz():
  return 'OK'

@app.route('/readinessz')
def return_readinessz():
  return 'OK'

@app.route('/metrics')
def return_next():
  return str(counter())

if __name__ == '__main__':
  try:
    env = os.environ['ENV']
    if len(env) > 0:
      app.run(debug=True,host='0.0.0.0')
    else:
      print('ENV variable is empty')
  except KeyError as exc:
    print('ENV variable is not found on system')
