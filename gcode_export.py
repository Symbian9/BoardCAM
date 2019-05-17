#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

filename = "demo.nc"


def write_line(line):
    with open(filename, "a") as file:
        file.write(line)


def gen_gcode(points):
    """

    :param points:
    :return:
    """
    write_line("G40\n")  # 关闭刀具补偿
    write_line("G49\n")  # 禁用刀具长度补偿
    write_line("G80\n")  # 取消模态动作
    write_line("G54\n")  # 选择坐标系1
    write_line("G90\n")  # 禁用增量移动
    write_line("G21\n")  # 使用毫米长度单位
    write_line("G61\n")  # 确切的路径模式
    write_line("F200.00000\n")  # 设定进给率
    write_line("S1000.00000\n")  # 设置主轴速度

    write_line("#2=-1.5\n")
    write_line("T1 M6\n")
    write_line("G0 Z5\n")  # 快速移动
    write_line(" X{} Y{}\n".format(points[0][0], points[0][1]))
    write_line("G1 Z#2\n")
    path = []
    for point in points:
        x, y = point
        path.append(" X{} Y{}".format(x, y))

    write_line("\n".join(path))

    write_line("G0 Z5\n")
    write_line("G0 Z5\n")
    write_line("M2\n")  # 结束程序


