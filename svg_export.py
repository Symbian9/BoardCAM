#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: SVG生成


def write_code(code):
    with open("test2.svg", mode="a") as file:
        file.write(code)
