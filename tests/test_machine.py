#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-12-15
# Desc:


from utils.machine import RouterBits


def test_eq():
    # cnc = CNCRouter("TigerCNC", "metric")
    bit = RouterBits("1/4inch", "1/4英寸螺旋向上双刃铣刀")
    assert bit.radius == 3.175
