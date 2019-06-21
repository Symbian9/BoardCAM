#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

from datetime import datetime

from __version__ import __version__, __title__
from circle import draw_circle_path


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
        self.write_code("F2000.00000\n")  # 设定进给率
        self.write_code("S1000.00000\n")  # 设置主轴速度

    def end_gcode(self):
        self.write_code("G0 Z5\n")
        self.write_code("G0 Z5\n")
        self.write_code("M2\n")  # 结束程序

    def lift_up(self):
        """
        抬起刀具
        :return:
        """
        pass


filename = "board_profile.gcode"


def write_line(line):
    """

    :param line:
    :return:
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(line)


def lift_up(self):
    """
    抬起刀具
    :return:
    """
    pass


def export_gcode(points, insert_coordinate_list):
    """
    生成G-code程序
    :param points: 轮廓路径
    :param insert_coordinate_list: 嵌件坐标
    :return:
    """
    safety_height = 5
    write_line("({})\n".format(48 * "-"))
    write_line("(文件名··················· {})\n".format(filename))
    write_line("(最后修订日期··················· {})\n".format(datetime.now().strftime("%Y-%m-%d")))
    write_line("(最后修订时间··················· {})\n".format(datetime.now().strftime("%X")))
    write_line("(软件名称··················· {} v{})\n".format(__title__, __version__))
    write_line("(程序员··················· Zheng)\n")
    write_line("(机床··················· TigerCNC)\n")
    write_line("(控制器··················· arduino grbl)\n")
    write_line("(单位··················· 毫米)\n")
    write_line("(加工编号··················· 01)\n")
    write_line("(操作··················· 铣削-钻孔)\n")
    write_line("(毛坯材料··················· 杨木)\n")
    write_line("(材料尺寸··················· 165cm*40cm*1cm)\n")
    write_line("(程序原点··················· X0 -- 左边)\n")
    write_line("(                           Y0 -- 底边)\n")
    write_line("(                         Z0 -- 上表面)\n")
    write_line("(状态··················· 未校验)\n")
    write_line("(铣刀····················· 6mm螺旋向上双刃)\n")
    write_line("({})\n".format(48 * "-"))

    write_line("\n")

    write_line("G40\n")  # 关闭刀具补偿
    write_line("G49\n")  # 禁用刀具长度补偿
    write_line("G80\n")  # 取消模态动作
    write_line("G54\n")  # 选择坐标系1
    write_line("G90\n")  # 禁用增量移动(绝对指令)
    write_line("G21\n")  # 使用毫米长度单位(公制)
    write_line("G61\n")  # 确切的路径模式
    write_line("F1000.00000\n")  # 设定进给率
    write_line("S1000.00000\n")  # 设置主轴速度

    write_line("G0 Z{}\n".format(safety_height))  # 快速移动 (Z轴抬升至安全加工距离)
    write_line("G0 X{} Y{}\n".format(points[0].y, points[0].x))

    path = []
    for i, point in enumerate(points):
        if i == 0:
            path.append("G01 X%.3f Y%.3f Z-9" % (point.y, point.x,))
        if i == len(points) - 1:
            path.append(" X%.3f Y%.3f" % (point.y, point.x,))
            path.append("G01 X%.3f Y%.3f Z%d" % (point.y, point.x, safety_height))
        else:
            path.append(" X%.3f Y%.3f" % (point.y, point.x,))

    for i, point in enumerate(sorted(insert_coordinate_list)):
        export_points = draw_circle_path(point.x, point.y, 9)
        for j, p in enumerate(export_points):
            if j == 0:
                path.append("G00 X%.3f Y%.3f Z%d" % (p.y, p.x, safety_height))
                path.append("G01 X%.3f Y%.3f Z-9" % (p.y, p.x))
            else:
                path.append(" X%.3f Y%.3f" % (p.y, p.x))

        path.append("G01 X%.3f Y%.3f Z%d" % (export_points[-1].y, export_points[-1].x, safety_height))

    write_line("\n".join(path))
    write_line("\n")
    write_line("G0 X0 Y0 Z{}\n".format(points[0].x, points[0].y, safety_height))
    write_line("M2\n")  # 结束程序
