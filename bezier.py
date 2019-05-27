#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 贝塞尔曲线

from config import bezier_step


def bezier(bezier_points):
    """
    贝塞尔通用函数
    :param bezier_points:
    :return:
    """
    # P0和P3是endpoints, P1和P2是control points
    # 所有点的个数P0 P1... Pn
    end = 1
    step_count = int(end / bezier_step)
    points_no = len(bezier_points) - 1
    temp = []
    for t in range(step_count + 1):
        t *= bezier_step
        x, y = 0, 0
        for index, point in enumerate(bezier_points):
            x += point[0] * pow(1 - t, points_no - index) * pow(t, index)
            y += point[1] * pow(1 - t, points_no - index) * pow(t, index)

        temp.append([x, y])
    return temp


def gen_curve(params):
    """
    板头&板尾曲线生成
    :param params:
    :return:
    """
    end_handle = params.get("end_handle")
    transition_handle = params.get("transition_handle")
    nose_length = params.get("nose_length")
    nose_width = params.get("nose_width")
    tail_length = params.get("tail_length")
    tail_width = params.get("tail_width")
    half_nose_width = nose_width / 2
    half_tail_width = tail_width / 2
    running_length = params.get("running_length")

    left_bezier_points = (
        (0, half_nose_width), (0, half_nose_width * end_handle), (nose_length * transition_handle, 0), (nose_length, 0))
    right_bezier_points = (
        (0, half_tail_width), (0, half_tail_width * end_handle), (tail_length * transition_handle, 0), (tail_length, 0))

    upper_left_list = bezier(left_bezier_points)
    # X轴对称变换
    lower_left_list = mirror_path(upper_left_list, 0, half_nose_width)

    temp = bezier(right_bezier_points)
    # Y轴对称变换
    temp2 = mirror_path(temp, tail_length, 0)

    # 平移到对应位置
    offset = running_length + nose_length - tail_length
    upper_right_list = move_path(temp2[::-1], offset, 0)
    lower_right_list = mirror_path(upper_right_list, 0, half_tail_width)
    return upper_left_list[::-1], lower_left_list, upper_right_list[::-1], lower_right_list


def mirror_path(points, width, length):
    """
    生成镜像路径
    :param points: 路径
    :param width: 按Y轴进行轴对称变化, width置0
    :param length: 按X轴进行轴对称变化, length置0
    :return:
    """
    width = int(width)
    length = int(length)
    return [[abs(width * 2 - point[0]), abs(length * 2 - point[1])] for point in points]


def move_path(points, x_offset, y_offset):
    """
    平移函数
    :param points:
    :param x_offset: X坐标偏移量
    :param y_offset: Y坐标偏移量
    :return:
    """
    return [[point[0] + x_offset, point[1] + y_offset] for point in points]
