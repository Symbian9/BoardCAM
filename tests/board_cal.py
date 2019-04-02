#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zhengxiang@boardcam.org>
# Desc board param calculator

import math


def cal_waist_width(running_length, sidecut_radius):
    """
    根据侧切半径和行程长度计算板腰宽度和有效边刃
    :param running_length: 行程长度
    :param sidecut_radius: 侧切半径
    :return:
    """
    # TODO 增加板头板尾的宽度控制
    waist_remain = sidecut_radius - math.sqrt(math.pow(sidecut_radius, 2) - math.pow(running_length / 2, 2))
    # print(waist_remain)
    # waist_width = nose_width - waist_remain * 2
    # print(round(waist_width, 3))
    return waist_remain


def cal_x():
    pass


if __name__ == "__main__":
    # millimeter
    print(cal_waist_width(1145, 7800))
    pass
