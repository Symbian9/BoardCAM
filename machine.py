#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-13
# Desc: 

from math_tools import INCH


class CNCRouter:
    def __init__(self, name, unit):
        self.name = name
        self.control = "arduino grbl"
        self.unit = unit
        self.z_axis_safety_height = 5.0
        self.max_x = None
        self.max_y = None
        self.spindle_speed = None
        self.feed_rate = None
        self.drilling_speed = None

        # 单层铣削厚度
        self.layer_thickness = 2

        # 单层步距

    def __str__(self):
        return "<CNCRouter>"


class RouterBits:
    def __init__(self, diameter, desc=None):
        if diameter[-2:] == "in":
            self.diameter = self.inch_to_mm(float(eval(diameter[:-2])))
        elif diameter[-4:] == "inch":
            self.diameter = self.inch_to_mm(float(eval(diameter[:-4])))
        elif diameter[-2:] == "mm":
            self.diameter = float(eval(diameter[:-2]))
        elif diameter[-2:] == "cm":
            self.diameter = float(eval(diameter[:-2])) * 10
        else:
            raise ValueError("diameter variable must specify the unit. (support inch、in、cm、mm)")
        self.radius = self.cal_radius()
        self.description = desc
        self.blade_length = None
        self.blade_number = 1

    def cal_radius(self):
        return self.diameter / 2

    @staticmethod
    def inch_to_mm(inch_value):
        """

        :param inch_value:
        :return: mm
        """
        return inch_value * INCH

    def __str__(self):
        return "bit: ⌀{}mm.".format(self.diameter)


if __name__ == '__main__':
    # cnc = CNCRouter("TigerCNC", "metric")
    bit = RouterBits("1/4inch", "1/4英寸螺旋向上双刃铣刀")
    print(bit)
