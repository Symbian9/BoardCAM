#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019-03-22
# Desc: 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
