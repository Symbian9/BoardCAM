#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc:

from xml.etree import ElementTree


# # 创建根节点
# svg_root = ElementTree.Element("svg")
# svg_root.attrib = {"width": "100%", "height": "100%", "version": "1.1", "xmlns": "http://www.w3.org/2000/svg"}
#
# # 创建子节点，并添加属性
# child_tag = ElementTree.SubElement(svg_root, "line")
# child_tag.attrib = {"x1": "0", "y1": "0", "x2": "300", "y2": "300", "style": "stroke:rgb(99,99,99);stroke-width:2"}
# # child_tag.text = "hh"
#
# # 创建element tree对象，写文件
# tree = ElementTree.ElementTree(svg_root)
# tree.write("test.svg", xml_declaration=True, encoding="UTF-8")


class SVG:
    def __init__(self):
        """
        创建根节点 初始化文件
        """
        self.svg_root = ElementTree.Element("svg")
        self.svg_root.attrib = {"width": "100%", "height": "100%", "version": "1.1",
                                "xmlns": "http://www.w3.org/2000/svg"}

    def add_child(self, tag_name, data):
        """
        创建子节点，并添加属性
        :param tag_name:
        :param data:
        :return:
        """
        child_tag = ElementTree.SubElement(self.svg_root, tag_name)
        child_tag.attrib = data

    def add_sub_tag(self, father_tag, tag_name):
        ElementTree.SubElement(father_tag, tag_name)

    def write_svg(self, filename):
        """
        创建element tree对象，写文件
        :param filename:
        :return:
        """
        tree = ElementTree.ElementTree(self.svg_root)
        tree.write(filename, xml_declaration=True, encoding="UTF-8")


if __name__ == "__main__":
    svg = SVG()
    svg.add_child("line", {"x1": "0", "y1": "0",
                           "x2": "300", "y2": "300",
                           "style": "stroke:rgb(99,99,99);stroke-width:2"
                           })

    svg.write_svg(filename="test1.svg")
