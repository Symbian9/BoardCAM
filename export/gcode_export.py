#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

import os
from datetime import datetime
from io import StringIO

from __version__ import __version__, __title__
from geometry.circle import Circle
from until.machine import CNCRouter, RouterBits


class Gcode:
    def __init__(self, filename):
        self.__filename = filename
        self.__buffer = StringIO()
        self.cnc = CNCRouter(name="TigerCNC", unit="毫米")
        self.bit = RouterBits
        self.__last_line = None

    def close(self):
        self._finish_code()
        with open(self.__filename, mode="w", encoding="utf-8") as f:
            f.write(self.__buffer.getvalue())

    def _write(self, line=""):
        self.__last_line = line
        self.__buffer.write("{}\n".format(line))

    def start_code(self):
        self._comment()             # 写入程序注释
        self._write("G40")          # 关闭刀具补偿
        self._write("G49")          # 禁用刀具长度补偿
        self._write("G80")          # 取消模态动作
        self._write("G54")          # 选择坐标系1
        self._write("G90")          # 禁用增量移动
        self._write("G21")          # 使用公制长度单位
        self._write("G61")          # 确切的路径模式
        self._write("F1000.00000")  # 设定进给率
        self._write("S1000.00000")  # 设置主轴转速

    def _finish_code(self):
        self._write("M05 M09")      # 主轴停,冷却液泵马达停
        self._write("G0 X0 Y0 Z5")  # 快速回到坐标原点
        self._write("M2")           # 结束程序  # TODO 比较M2和M30区别

    def lift_bit(self):
        """
        抬起刀具
        :return:
        """
        # TODO 需要获取buffer(self.__last_line)里最后g代码
        self._write("G0 Z5")        # Z轴抬升至安全加工距离

    def down_bit(self):
        """
        下刀
        :return:
        """
        pass

    def rapid_move(self, code):
        # 快速移动 G0
        self._write("G0 {}".format(code))

    def linear_move(self, code):
        # 线性移动 G1
        self._write("G1 {}".format(code))

    def _comment(self):
        # TODO 还需要优化整齐注释的排版
        self._write("({})".format(50 * "-"))
        self._write("(文件名··················· {})".format(os.path.basename(self.__filename)))
        self._write("(最后修订日期··················· {})".format(datetime.now().strftime("%Y-%m-%d")))
        self._write("(最后修订时间··················· {})".format(datetime.now().strftime("%X")))
        self._write("(软件名称··················· {} v{})".format(__title__, __version__))
        self._write("(程序员··················· Zheng)")
        self._write("(机床··················· {})".format(self.cnc.name))
        self._write("(控制器··················· {})".format(self.cnc.control))
        self._write("(单位··················· {})".format(self.cnc.unit))
        self._write("(加工编号··················· 01)")
        self._write("(操作··················· 铣削-钻孔)")
        self._write("(毛坯材料··················· 杨木)")
        self._write("(材料尺寸··················· 165cm*40cm*1cm)")
        self._write("(程序原点··················· X0 -- 左边)")
        self._write("(                           Y0 -- 底边)")
        self._write("(                           Z0 --上表面)")
        self._write("(状态··················· 未校验)")
        self._write("(铣刀····················· 6mm螺旋向上双刃铣刀)")
        self._write("({})".format(50 * "-"))
        self._write()

    # TODO 使用with语句，前提代码不要超过3层缩进
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type and not exc_val and not exc_tb:
            self.close()

    def __repr__(self):
        return "Gcode: {}".format(self.__filename)


def export_gcode(points, insert_coordinate_list, profile_points):
    """
    生成G-code程序
    :param points: 轮廓路径
    :param insert_coordinate_list: 嵌件坐标
    :param profile_points:
    :return:
    """

    export_profile(profile_points)
    # TODO 连接桥的开发 和彻底钻孔算法
    safety_height = 5.0
    filename = "./output/board_profile.gcode"
    g = Gcode(filename)
    g.start_code()
    g.lift_bit()

    # 外轮廓铣削
    # 快速移动 (Z轴抬升至安全加工距离)
    g.rapid_move("X{} Y{} Z{}".format(points[0].y, points[0].x, safety_height))
    # g.down_bit()
    for i, point in enumerate(points):
        g.linear_move("X%.3f Y%.3f Z-9" % (point.y, point.x))

    g.lift_bit()
    # 嵌件铣削
    for i, point in enumerate(sorted(insert_coordinate_list)):
        # TODO 嵌件的圆周偏置需要建立算法
        export_points = Circle(point.x, point.y, 6).draw_path()
        export_points += Circle(point.x, point.y, 3).draw_path()
        for j, p in enumerate(export_points):
            if j == 0:
                g.rapid_move("X%.3f Y%.3f Z%d" % (p.y, p.x, safety_height))
                g.linear_move("X%.3f Y%.3f Z-1" % (p.y, p.x))
            else:
                g.linear_move("X%.3f Y%.3f" % (p.y, p.x))

        g.linear_move("X%.3f Y%.3f Z%d" % (export_points[-1].y, export_points[-1].x, safety_height))

    g.close()


def export_profile(profile_points):
    """
    模具gcode
    :param profile_points:
    :return:
    """
    # TODO 需要把模具切出边缘，过厚就需要重复步骤
    filename = "./output/profile.gcode"
    with Gcode(filename) as g:
        g.start_code()
        safety_height = 5.0
        g.rapid_move("X{} Y{} Z{}".format(profile_points[0].y, profile_points[0].x, safety_height))
        for i, p in enumerate(profile_points):
            g.linear_move("X%.3f Y%.3f Z-9" % (p.y, p.x))
        g.lift_bit()
