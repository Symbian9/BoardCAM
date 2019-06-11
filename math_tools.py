#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 常用数学函数封装

from math import sqrt, pow, pi

ZERO_ANGLE = 0
RIGHT_ANGLE = 90
STRAIGHT_ANGLE = 180
FULL_ANGLE = 360


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
    return sidecut_radius - sqrt(pow(sidecut_radius, 2) - pow(running_length / 2, 2))


def cal_radius(running_length, camber):
    """
    r^2 = (r-15)^2 + (half_running_length)^2
    :param running_length: 行程长度
    :param camber: 拱起高度
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


def arc_to_angle(arc_length, radius):
    """
    将弧长转换为圆心角度数
    :param arc_length: 圆心角弧长
    :param radius: 半径
    :return:
    """
    return arc_length / pi / (radius / STRAIGHT_ANGLE)
