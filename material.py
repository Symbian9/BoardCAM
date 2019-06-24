#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-06-23
# Desc:


class Unit:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


class Material:
    def __init__(self, length, width, thickness, material_type):
        # unit: mm

        # Length corresponds to the Y-axis
        self.length = length

        # Width corresponds to the X-axis
        self.width = width

        # Thickness corresponds to the Z-axis
        self.thickness = thickness

        self.material_type = material_type
        self.check()

    def check(self):
        # TODO 检查材料单位是否符合正常标准并且符合机床的加工区间
        pass

    def __str__(self):
        return "Material({}): {}mm x {}mm x {}mm.".format(self.material_type, self.length,
                                                          self.width, self.thickness)


if __name__ == '__main__':
    m = Material(1600, 400, 10, "Poplar")

    a = Unit(5)
    b = Unit(2)
    print(a * b)
