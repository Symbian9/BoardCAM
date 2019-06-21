#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 嵌件组生成

from points import Point


class Inserts:
    def __init__(self, height, inner_radius, outer_radius):
        self.height = height
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius


def gen_inserts(params):
    """
    从竖中线向左右两侧生成每个嵌件的坐标
    :param params:
    :return: 每个嵌件的坐标List
    """
    stand_width = params.get("stand_width")
    half_stand_width = stand_width / 2
    stand_setback = params.get("stand_setback")
    inserts_number = params.get("inserts_number")
    horizontal_spacing = params.get("horizontal_spacing")
    vertical_spacing = params.get("vertical_spacing")
    half_vertical_spacing = vertical_spacing / 2
    half_horizontal_spacing = horizontal_spacing / 2
    nose_length = params.get("nose_length")
    nose_width = params.get("nose_width")
    running_length = params.get("running_length")
    half_running_length = running_length / 2

    # 竖直中线
    vertical_mid_line = nose_length + half_running_length

    # 水平中线
    horizontal_mid_line = nose_width / 2

    left_start, right_start = 0, 0
    if inserts_number % 2 == 1:
        # 嵌件个数为奇数
        left_start = vertical_mid_line - half_stand_width - horizontal_spacing * int(inserts_number / 2)
        right_start = vertical_mid_line + half_stand_width - horizontal_spacing * int(inserts_number / 2)
    elif inserts_number % 2 == 0:
        # 嵌件个数为偶数
        left_start = vertical_mid_line - half_stand_width - half_horizontal_spacing - horizontal_spacing * (
                int(inserts_number / 2) - 1)
        right_start = vertical_mid_line + half_stand_width - half_horizontal_spacing - horizontal_spacing * (
                int(inserts_number / 2) - 1)

    insert_coordinate_list = []
    for i in range(inserts_number):
        insert_coordinate_list.append(
            Point(left_start + horizontal_spacing * i + stand_setback, horizontal_mid_line - half_vertical_spacing))
        insert_coordinate_list.append(
            Point(left_start + horizontal_spacing * i + stand_setback, horizontal_mid_line + half_vertical_spacing))
        insert_coordinate_list.append(
            Point(right_start + horizontal_spacing * i + stand_setback, horizontal_mid_line - half_vertical_spacing))
        insert_coordinate_list.append(
            Point(right_start + horizontal_spacing * i + stand_setback, horizontal_mid_line + half_vertical_spacing))

    return insert_coordinate_list
