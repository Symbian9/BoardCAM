#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 嵌件组生成


def gen_inserts(params):
    """
    从竖中线向左右两侧生成嵌件位置
    :param params:
    :return: 每个嵌件的坐标List
    """
    stand_width = params.get("stand_width")
    half_stand_width = stand_width / 2
    stand_setback = params.get("stand_setback")
    inserts_number = params.get("inserts_number")
    spacing = params.get("spacing")
    half_spacing = spacing / 2

    # 竖直中线
    vertical_mid_line = params.get("half_overall_length")

    # 水平中线
    horizontal_mid_line = params.get("half_nose_width")

    insert_coordinate_list = []

    left_start, right_start = 0, 0
    if inserts_number % 2 == 1:
        # 嵌件个数为奇数
        left_start = vertical_mid_line - half_stand_width - spacing * int(inserts_number / 2)
        right_start = vertical_mid_line + half_stand_width - spacing * int(inserts_number / 2)
    elif inserts_number % 2 == 0:
        # 嵌件个数为偶数
        left_start = vertical_mid_line - half_stand_width - half_spacing - spacing * (int(inserts_number / 2) - 1)
        right_start = vertical_mid_line + half_stand_width - half_spacing - spacing * (int(inserts_number / 2) - 1)

    for i in range(inserts_number):
        insert_coordinate_list.append([left_start + spacing * i + stand_setback, horizontal_mid_line - half_spacing])
        insert_coordinate_list.append([left_start + spacing * i + stand_setback, horizontal_mid_line + half_spacing])
        insert_coordinate_list.append([right_start + spacing * i + stand_setback, horizontal_mid_line - half_spacing])
        insert_coordinate_list.append([right_start + spacing * i + stand_setback, horizontal_mid_line + half_spacing])

    return insert_coordinate_list
