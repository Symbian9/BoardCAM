#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019-03-11
# Desc:

import svgwrite

import svgwrite

dwg = svgwrite.Drawing('hahah.svg', profile='full')

dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2)))
dwg.save()