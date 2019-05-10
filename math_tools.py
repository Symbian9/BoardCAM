#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 常用数学函数封装

from math import sqrt, pow


def cal_waist_width(running_length, sidecut_radius):
    """
    根据侧切半径和行程长度计算板腰宽度和有效边刃
    :param running_length: 行程长度
    :param sidecut_radius: 侧切半径
    :return:
    """
    # TODO 增加板头板尾的宽度控制
    # print(waist_remain)
    # waist_width = nose_width - waist_remain * 2
    # print(round(waist_width, 3))
    return sqrt(pow(sidecut_radius, 2) - pow(running_length / 2, 2))


def cal_radius(running_length, camber):
    """

    :param running_length:
    :param camber:
    :return:
    """
    half_running_length = running_length / 2
    print(half_running_length)

    radius = (pow(half_running_length, 2) - pow(camber, 2)) / (2 * camber)
    # print(radius)
    return radius


if __name__ == "__main__":
    from svg_export import pack_svg
    r = cal_radius(1260, 12)

    SVG_code = """<circle cx="{}" cy="{}" r="{}" stroke="black" fill="blue" fill-opacity="0.25" />""".format(630,
                                                                                                             300 + r, r)
    pack_svg(SVG_code)

