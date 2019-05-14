#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 

def dict_str(dict_data):
    if not isinstance(dict_data, dict):
        return None

    data = str(dict_data)
    print(data)
    # 必须将value为int 或者float的转换成字符串
    # # 将值为int的Value转换成字符串
    # data = re.sub(r'(\d+),', repl=dashrepl, string=data)
    # print(data)

    content = data.replace("{", "\n<<\n").replace("}", "\n>>")
    content = content.replace("', '", "\n").replace("'", "").replace(":", "")

    return content


if __name__ == "__main__":
    n = {"/Rotate": "17", "/Parent": "1 0 R",
         "/Resources": {"/Font": {"/F0": {"/BaseFont": "/Times-Italic", "/Subtype": "/Type1", "/Type": "/Font"}}}}
    # print(dict_str(n))

    obj1 = """/Kids [2 0 R]\n/Count 1\n/Type /Pages"""
    a = {"/Kids": "[2 0 R]", "/Count": "1", "/Type": "/Pages"}
    # print(dict_str(a))

    obj2 = """/Rotate 0\n/Parent 1 0 R\n/Resources 3 0 R\n/MediaBox [0 0 792 612]\n/Contents [4 0 R]\n/Type /Page"""
    b = {"/Rotate": "0", "/Parent": "1 0 R", "/Resources": "3 0 R", "/MediaBox": "[0 0 792 612]",
         "/Contents": "[4 0 R]", "/Type": "/Page"}
    # print(dict_str(b))

    obj3 = """/Font \n<<\n/F0 \n<<\n/BaseFont /Times-Italic\n/Subtype /Type1\n/Type /Font\n>>\n>>"""
    c = {"/Font": {"/F0": {"/Type": "/Font", "/BaseFont": "/Times-Italic", "/Subtype": "/Type1"}}}
    # print(dict_str(c))

    # Length为stream 和endstream之间的长度
    stream = """/Length {}\n>>\nstream\n200 150 m 600 450 l S \n\nendstream """
    d = {"/Length": "23"}
    # print(dict_str(d))

    obj5 = """/Pages 1 0 R\n/Type /Catalog"""
    e = {"/Pages": "1 0 R", "/Type": "/Catalog"}
    print(dict_str(e))
