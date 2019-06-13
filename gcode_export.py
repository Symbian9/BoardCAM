#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

from datetime import datetime

from config import WEBSITE, COPYRIGHT


class Gcode:
    def __init__(self, _filename):
        self.filename = _filename
        self.file = self.open_file()

    def open_file(self):
        return open(self.filename, mode="a", encoding="utf-8")

    def close_file(self):
        self.file.close()

    def write_code(self, line):
        self.file.write(line)

    def write_comment(self, line):
        self.write_code(line)

    def start_gcode(self):
        self.write_code("G40\n")  # 关闭刀具补偿
        self.write_code("G49\n")  # 禁用刀具长度补偿
        self.write_code("G80\n")  # 取消模态动作
        self.write_code("G54\n")  # 选择坐标系1
        self.write_code("G90\n")  # 禁用增量移动
        self.write_code("G21\n")  # 使用毫米长度单位
        self.write_code("G61\n")  # 确切的路径模式
        self.write_code("F200.00000\n")  # 设定进给率
        self.write_code("S1000.00000\n")  # 设置主轴速度

    def end_gcode(self):
        self.write_code("G0 Z5\n")
        self.write_code("G0 Z5\n")
        self.write_code("M2\n")  # 结束程序


filename = "board_profile.gcode"


def write_line(line):
    """

    :param line:
    :return:
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(line)


def export_gcode(points):
    """
    生成G-code程序
    :param points: 轮廓路径
    :return:
    """
    write_line("( {} - {} )\n".format(COPYRIGHT, WEBSITE))
    write_line("( Create Time: {} )\n".format(datetime.now().strftime("%Y-%m-%d %X")))
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
    write_line(" X{} Y{}\n".format(points[0].x, points[0].y))
    write_line("G1 Z#2\n")
    path = []
    for point in points:
        path.append(" X{} Y{}".format(point.x, point.y))

    write_line("\n".join(path))

    write_line("G0 Z5\n")
    write_line("G0 Z5\n")
    write_line("M2\n")  # 结束程序
