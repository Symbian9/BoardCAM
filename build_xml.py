#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 


from xml.etree import ElementTree


class SVG:
    def __init__(self):
        """
        创建根节点 初始化SVG文件
        """
        self.svg_root = ElementTree.Element("svg")
        self.svg_root.attrib = {"width": "100%", "height": "100%", "version": "1.1",
                                "xmlns": "http://www.w3.org/2000/svg"}
        self.child_tag = None

    def add_child(self, parent, tag_name, data, text):
        """
        创建子节点，并添加属性
        :param parent:
        :param tag_name:
        :param data:
        :param text:
        :return:
        """
        self.child_tag = ElementTree.SubElement(parent, tag_name)
        self.child_tag.attrib = data
        if text:
            self.child_tag.text = text

        return self.child_tag

    # def add_sub_tag(self, father_tag, tag_name):
    #     ElementTree.SubElement(father_tag, tag_name)

    def write_svg(self, filename):
        """
        创建element tree对象，写文件
        :param filename:
        :return:
        """
        tree = ElementTree.ElementTree(self.svg_root)
        tree.write(filename, xml_declaration=True, encoding="UTF-8")


def init_svg():
    root = ElementTree.Element("svg")
    root.attrib = {"width": "100%", "height": "100%", "version": "1.1",
                   "xmlns": "http://www.w3.org/2000/svg"}
    return root


def draw_logo(parent):
    logo = ElementTree.SubElement(parent, "text", {"x": "800", "y": "200", "fill": "black", "fill-opacity": "0.6"})
    logo.text = "© BoardCAM"

    slogan = ElementTree.SubElement(parent, "text",
                                    {"x": "805", "y": "215", "fill": "black", "fill-opacity": "0.6", "font-size": "9",
                                     "font-family": "Times-Italic"})
    slogan.text = "design it. build it. enjoy it."


if __name__ == "__main__":
    # svg = SVG()
    # # svg.add_child("line", {"x1": "0", "y1": "0",
    # #                        "x2": "300", "y2": "300",
    # #                        "style": "stroke:rgb(99,99,99);stroke-width:2"
    # #                        })
    #
    # g1 = svg.add_child(parent=svg, tag_name="g",
    #                    data={"style": "stroke:#000000;stroke-width:1;stroke-dasharray=5,5"}, text=None)
    #
    # svg.add_child(g1, "line", data={"x1": "11", "y1": "18", "x2": "32", "y2": "35"}, text=None)
    #
    # svg.write_svg(filename="test1.svg")

    svg_root = init_svg()

    # 辅助线
    g1 = ElementTree.SubElement(svg_root, "g", {"style": "stroke:#000000;stroke-width:1;", "stroke-dasharray": "5,5"})
    ElementTree.SubElement(g1, "line", {"x1": "0", "y1": "150", "x2": "1520", "y2": "150"})
    ElementTree.SubElement(g1, "line", {"x1": "180", "y1": "0", "x2": "180", "y2": "300"})
    ElementTree.SubElement(g1, "line", {"x1": "180", "y1": "0", "x2": "180", "y2": "300"})
    ElementTree.SubElement(g1, "line", {"x1": "760", "y1": "0", "x2": "760", "y2": "300"})
    ElementTree.SubElement(g1, "line", {"x1": "1340", "y1": "0", "x2": "1340", "y2": "300"})

    # 版权
    draw_logo(svg_root)

    tree = ElementTree.ElementTree(svg_root)
    tree.write("test.svg", xml_declaration=True, encoding="UTF-8")
