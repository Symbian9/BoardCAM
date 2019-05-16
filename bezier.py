#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: 贝塞尔曲线点


def gen_bezier(params):
    """
    P0和P3是endpoints, P1和P2是control points
    参考通用贝塞尔通用计算公式
    :param params:
    :return:
    """
    points = params.get("bezier_points")
    nose_width = params.get("nose_width")
    nose_length = params.get("nose_length")
    overall_length = params.get("overall_length")
    upper_left_list = []
    lower_left_list = []
    upper_right_list = []
    lower_right_list = []
    # 计算步骤
    step = 0.01
    end = 1
    step_count = int(end / step)

    # 所有点的个数P0 P1... Pn
    points_no = len(points) - 1
    for t in range(step_count + 1):
        t *= step
        x, y = 0, 0
        for index, point in enumerate(points):
            x_value = point[0] * pow(1 - t, points_no - index) * pow(t, index)
            x += x_value
            y_value = point[1] * pow(1 - t, points_no - index) * pow(t, index)
            y += y_value

        print("Step{}: {} {}".format(step_count, x, y))
        # 分别进行X轴 y轴变换
        upper_left_list.append([x, y])
        lower_left_list.append([x, nose_width - y])
        upper_right_list.append([nose_length - x + overall_length-nose_length, y])
        lower_right_list.append([nose_length - x + overall_length-nose_length, nose_width - y])

    return upper_left_list, lower_left_list, upper_right_list, lower_right_list
