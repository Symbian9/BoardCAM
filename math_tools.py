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

    radius = (pow(half_running_length, 2) - pow(camber, 2)) / (2 * camber)
    return radius


def mm_to_dpi(mm):
    """
    毫米转换成dpi(web上使用的图片都是72dpi 这存在质疑或过时)
    图像每英寸长度内的像素点数。DPI（Dots Per Inch，每英寸点数）
    :param mm: 毫米
    :return: dpi
    """
    cm = mm * 0.1
    inch = cm / 2.54  # 1in = 2.54cm
    dpi = 72 * inch
    return dpi


if __name__ == "__main__":
    r = cal_radius(1260, 12)
