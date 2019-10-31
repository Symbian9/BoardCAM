#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-10-10
# Desc: 


class Board:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Board: {}".format(self.name)


if __name__ == '__main__':
    b = Board("Zheng's snowboard")
    print(b)
