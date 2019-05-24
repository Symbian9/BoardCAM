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
    tail_length = params.get("tail_length")
    half_nose_width = params.get("half_nose_width")
    half_tail_width = params.get("half_tail_width")
    running_length = params.get("running_length")

    left_bezier_points = (
        (0, half_nose_width), (0, half_nose_width * end_handle), (nose_length * transition_handle, 0), (nose_length, 0))
    right_bezier_points = (
        (0, half_tail_width), (0, half_tail_width * end_handle), (tail_length * transition_handle, 0), (tail_length, 0))

    upper_left_list = bezier(left_bezier_points)
    # X轴对称变换
    lower_left_list = mirror_path(0, half_nose_width, upper_left_list)

    temp = bezier(right_bezier_points)
    # Y轴对称变换
    temp2 = mirror_path(tail_length, 0, temp)

    # 平移到对应位置
    offset = running_length + nose_length - tail_length
    upper_right_list = move(temp2[::-1], offset, 0)
    lower_right_list = mirror_path(0, half_tail_width, upper_right_list)
    return upper_left_list, lower_left_list, upper_right_list[::-1], lower_right_list


def mirror_path(width, length, points):
    """
    生成镜像路径
    :param width: 按Y轴进行轴对称变化 width置0
    :param length: 按X轴进行轴对称变化, length置0
    :param points: 路径
    :return:
    """
    new_point = []
    width = int(width)
    length = int(length)
    for point in points:
        x, y = point
        new_point.append([abs(width * 2 - x), abs(length * 2 - y)])

    return new_point


def move(points, x_offset, y_offset):
    """
    平移函数
    :param points:
    :param x_offset: X坐标偏移量
    :param y_offset: Y坐标偏移量
    :return:
    """
    new_point = []
    for point in points:
        x, y = point
        new_point.append([x + x_offset, y + y_offset])

    return new_point
