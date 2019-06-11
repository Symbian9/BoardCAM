#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-11
# Desc: 


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def offset(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)
