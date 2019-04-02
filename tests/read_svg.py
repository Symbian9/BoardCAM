#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019-03-06
# Desc: 
from svgpathtools import svg2paths

paths, attributes = svg2paths('sample.svg')
print(paths)
print(attributes)
