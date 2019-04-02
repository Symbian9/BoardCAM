#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019-03-21
# Desc: 
import requests

url = "https://asia-northeast1-boardcam.cloudfunctions.net/say_hello"

data = {
    "message": "郑翔"
}

resp = requests.post(url, json=data)
print(resp.text)
