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

    def __repr__(self):
        pass


class Material:
    def __init__(self, **kwargs):
        # unit: mm

        # Length corresponds to the Y-axis
        self.length = kwargs.get("material_length")

        # Width corresponds to the X-axis
        self.width = kwargs.get("material_width")

        # Thickness corresponds to the Z-axis
        self.thickness = kwargs.get("material_thickness")

        self.material_type = kwargs.get("material_type")
        self._check()

    def _check(self):
        # TODO 检查材料单位是否符合正常标准并且符合机床的加工区间
        pass

    def __repr__(self):
        return "Material({}): {}mm x {}mm x {}mm.".format(self.material_type, self.length,
                                                          self.width, self.thickness)
