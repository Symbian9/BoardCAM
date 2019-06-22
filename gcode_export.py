#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

from datetime import datetime
from io import StringIO

from __version__ import __version__, __title__
from circle import draw_circle_path


class Gcode:
    def __init__(self, _filename):
        self.filename = _filename
        self.buffer = StringIO()

    def close(self):
        self.end()
        with open(self.filename, mode="w", encoding="utf-8") as file:
            file.write(self.buffer.getvalue())

    def write(self, line):
        self.buffer.write("{}\n".format(line))

    def start(self):
        self.write("G40")  # 关闭刀具补偿
        self.write("G49")  # 禁用刀具长度补偿
        self.write("G80")  # 取消模态动作
        self.write("G54")  # 选择坐标系1
        self.write("G90")  # 禁用增量移动
        self.write("G21")  # 使用毫米长度单位
        self.write("G61")  # 确切的路径模式
        self.write("F2000.00000")  # 设定进给率
        self.write("S1000.00000")  # 设置主轴速度

    def end(self):
        self.write("M05 M09")   # 主轴停 冷却液泵马达停
        self.write("G0 X0 Y0 Z5")  # 快速回到坐标原点
        self.write("M2")  # 结束程序  # TODO 比较M2和M30区别

    def lift_bit(self):
        """
        抬起刀具
        :return:
        """
        self.write("G0 Z5")


def export_gcode(points, insert_coordinate_list):
    """
    生成G-code程序
    :param points: 轮廓路径
    :param insert_coordinate_list: 嵌件坐标
    :return:
    """

    # TODO 连接桥的开发 和彻底钻孔
    safety_height = 5
    filename = "board_profile.gcode"
    g = Gcode(filename)
    g.write("({})".format(50 * "-"))
    g.write("(文件名··················· {})".format(filename))
    g.write("(最后修订日期··················· {})".format(datetime.now().strftime("%Y-%m-%d")))
    g.write("(最后修订时间··················· {})".format(datetime.now().strftime("%X")))
    g.write("(软件名称··················· {} v{})".format(__title__, __version__))
    g.write("(程序员··················· Zheng)")
    g.write("(机床··················· TigerCNC)")
    g.write("(控制器··················· arduino grbl)")
    g.write("(单位··················· 毫米)")
    g.write("(加工编号··················· 01)")
    g.write("(操作··················· 铣削-钻孔)")
    g.write("(毛坯材料··················· 杨木)")
    g.write("(材料尺寸··················· 165cm*40cm*1cm)")
    g.write("(程序原点··················· X0 -- 左边)")
    g.write("(                           Y0 -- 底边)")
    g.write("(                         Z0 -- 上表面)")
    g.write("(状态··················· 未校验)")
    g.write("(铣刀····················· 6mm螺旋向上双刃)")
    g.write("({})".format(50 * "-"))
    g.write("G0 Z{}".format(safety_height))  # 快速移动 (Z轴抬升至安全加工距离)
    g.write("G0 X{} Y{}".format(points[0].y, points[0].x))

    g.start()

    for i, point in enumerate(points):
        if i == 0:
            g.write("G01 X%.3f Y%.3f Z-9" % (point.y, point.x,))
        if i == len(points) - 1:
            g.write(" X%.3f Y%.3f" % (point.y, point.x,))
            g.write("G01 X%.3f Y%.3f Z%d" % (point.y, point.x, safety_height))
        else:
            g.write(" X%.3f Y%.3f" % (point.y, point.x,))

    for i, point in enumerate(sorted(insert_coordinate_list)):
        export_points = draw_circle_path(point.x, point.y, 9)
        for j, p in enumerate(export_points):
            if j == 0:
                g.write("G00 X%.3f Y%.3f Z%d" % (p.y, p.x, safety_height))
                g.write("G01 X%.3f Y%.3f Z-1" % (p.y, p.x))
            else:
                g.write(" X%.3f Y%.3f" % (p.y, p.x))

        g.write("G01 X%.3f Y%.3f Z%d" % (export_points[-1].y, export_points[-1].x, safety_height))

    g.close()
