#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-13
# Desc: 

from utils.math_tools import INCH


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

    def __repr__(self):
        return "<CNCRouter>"


class RouterBits:
    def __init__(self, diameter, desc=""):
        if diameter[-2:] == "in":
            self.diameter = self.inch_to_mm(self.to_float(diameter[:-2]))
        elif diameter[-4:] == "inch":
            self.diameter = self.inch_to_mm(self.to_float(diameter[:-4]))
        elif diameter[-2:] == "mm":
            self.diameter = self.to_float(diameter[:-2])
        elif diameter[-2:] == "cm":
            self.diameter = self.to_float(diameter[:-2]) * 10
        else:
            raise ValueError("diameter variable must specify the unit. (support inch、in、cm、mm)")
        self.description = desc

        # 刃有关
        self.blade_length = None
        self.blade_number = 1

    @property
    def radius(self):
        return self.diameter / 2

    @staticmethod
    def to_float(value):
        return float(eval(value))

    @staticmethod
    def inch_to_mm(inch_value):
        """

        :param inch_value:
        :return: mm
        """
        return inch_value * INCH

    def __repr__(self):
        return "bit: ⌀{}mm.".format(self.diameter)
