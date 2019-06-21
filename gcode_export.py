#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-17
# Desc: gcode
# Preview: https://ncviewer.com/

from io import StringIO

from circle import draw_circle_path


class Gcode:
    def __init__(self, _filename):
        self.filename = _filename
        self.buffer = StringIO()
        self.start()

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
        self.write("G0 X0 Y0 Z5")
        self.write("M2")  # 结束程序

    def lift_up(self):
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
    safety_height = 5
    # write_line("({})\n".format(48 * "-"))
    # write_line("(文件名··················· {})\n".format(filename))
    # write_line("(最后修订日期··················· {})\n".format(datetime.now().strftime("%Y-%m-%d")))
    # write_line("(最后修订时间··················· {})\n".format(datetime.now().strftime("%X")))
    # write_line("(软件名称··················· {} v{})\n".format(__title__, __version__))
    # write_line("(程序员··················· Zheng)\n")
    # write_line("(机床··················· TigerCNC)\n")
    # write_line("(控制器··················· arduino grbl)\n")
    # write_line("(单位··················· 毫米)\n")
    # write_line("(加工编号··················· 01)\n")
    # write_line("(操作··················· 铣削-钻孔)\n")
    # write_line("(毛坯材料··················· 杨木)\n")
    # write_line("(材料尺寸··················· 165cm*40cm*1cm)\n")
    # write_line("(程序原点··················· X0 -- 左边)\n")
    # write_line("(                           Y0 -- 底边)\n")
    # write_line("(                         Z0 -- 上表面)\n")
    # write_line("(状态··················· 未校验)\n")
    # write_line("(铣刀····················· 6mm螺旋向上双刃)\n")
    # write_line("({})\n".format(48 * "-"))

    filename = "board_profile.gcode"
    g = Gcode(filename)
    g.write("G0 Z{}".format(safety_height))  # 快速移动 (Z轴抬升至安全加工距离)
    g.write("G0 X{} Y{}".format(points[0].y, points[0].x))

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
                g.write("G01 X%.3f Y%.3f Z-9" % (p.y, p.x))
            else:
                g.write(" X%.3f Y%.3f" % (p.y, p.x))

        g.write("G01 X%.3f Y%.3f Z%d" % (export_points[-1].y, export_points[-1].x, safety_height))

    g.close()
