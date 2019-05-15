#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 


__author__ = 'xua'

import xml.etree.ElementTree as ET

# 创建根节点
a = ET.Element("root")
# 创建子节点，并添加属性
b = ET.SubElement(a, "sub1")
b.attrib = {"name": "name attribute"}
# 创建子节点，并添加数据
c = ET.SubElement(a, "sub2")
c.text = "test"

# 创建elementtree对象，写文件
tree = ET.ElementTree(a)
tree.write("test.svg")
