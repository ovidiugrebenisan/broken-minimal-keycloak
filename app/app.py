#!/usr/bin/env python3

import os
from flask import Flask, redirect
from waitress import serve

app = Flask(__name__)

try:
    AUTH_URL = os.environ["AUTH_URL"]
except Exception as ex:
    raise

@app.route('/')
def index():
    return 'Hello world!'

@app.route("/login")
def login():
    return redirect(AUTH_URL, code=302)

@app.route("/auth/callback")
def custom_callback():
    return "Logged in!"

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
