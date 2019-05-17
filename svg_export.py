#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: SVG生成

from xml.etree import ElementTree

from config import COPYRIGHT, SLOGAN


def write_code(code):
    with open("board_profile.svg", mode="a", encoding="utf-8") as file:
        file.write(code)


def init_svg(params):
    """
    生成辅助线 框架
    :param params:
    :return:
    """
    root = ElementTree.Element("svg")
    root.attrib = {"width": "100%", "height": "100%", "version": "1.1", "xmlns": "http://www.w3.org/2000/svg"}

    half_nose_width = params.get("half_nose_width")
    half_overall_length = params.get("half_overall_length")
    nose_width = params.get("nose_width")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    overall_length = params.get("overall_length")
    tail_width = params.get("tail_width")

    frame = ElementTree.SubElement(root, "g", {"style": "stroke:#000000;stroke-width:1;", "stroke-dasharray": "5,5"})

    # 板头虚线
    ElementTree.SubElement(frame, "line", {"x1": str(nose_length), "y1": str(0 + 5), "x2": str(nose_length),
                                           "y2": str(nose_width - 5)})

    # 板尾虚线
    ElementTree.SubElement(frame, "line",
                           {"x1": str(nose_length + running_length), "y1": str(0 + 5),
                            "x2": str(nose_length + running_length), "y2": str(tail_width - 5)})

    # TODO 超过部分裁剪掉
    # 水平中线虚线
    ElementTree.SubElement(frame, "line",
                           {"x1": str(0), "y1": str(half_nose_width),
                            "x2": str(overall_length), "y2": str(half_nose_width)})
    # 竖直中线虚线
    ElementTree.SubElement(frame, "line",
                           {"x1": str(half_overall_length), "y1": str(0 + 20),
                            "x2": str(half_overall_length), "y2": str(nose_width - 20)})
    # 版权信息
    copyright_tag = ElementTree.SubElement(root, "text",
                                           {"x": "800", "y": "200", "fill": "black", "fill-opacity": "0.6"})
    copyright_tag.text = COPYRIGHT

    # 比例尺
    scale = ElementTree.SubElement(root, "g", {"style": "stroke:black;stroke-width:0.3"})
    scale_text = ElementTree.SubElement(scale, "text", {"x": "12", "y": "8", "fill": "black", "font-size": "3"})
    scale_text.text = "1cm"
    ElementTree.SubElement(scale, "line", {"x1": "10", "y1": "8", "x2": "10", "y2": "10"})
    ElementTree.SubElement(scale, "line", {"x1": "10", "y1": "12", "x2": "10", "y2": "10"})
    ElementTree.SubElement(scale, "line", {"x1": "10", "y1": "10", "x2": "20", "y2": "10"})
    ElementTree.SubElement(scale, "line", {"x1": "20", "y1": "8", "x2": "20", "y2": "10"})
    ElementTree.SubElement(scale, "line", {"x1": "20", "y1": "12", "x2": "20", "y2": "10"})

    # Slogan
    slogan_tag = ElementTree.SubElement(root, "text", {"x": "805", "y": "215", "fill": "black", "font-size": "9",
                                                       "font-family": "Times-Italic"})
    slogan_tag.text = SLOGAN

    return root


def gen_circle(root, insert_coordinate_list):
    """

    :param root:
    :param insert_coordinate_list: 每个嵌件位置的坐标
    :return:
    """
    insert_group = ElementTree.SubElement(root, "g", {"style": "stroke-width:1;stroke:black;"})
    content = """<g style="stroke-width:1;stroke:black;">"""
    for insert in insert_coordinate_list:
        cx, cy = insert
        for r in ["0.5", "10", "18"]:
            ElementTree.SubElement(insert_group, "circle",
                                   {"cx": str(cx), "cy": str(cy), "r": str(r), "style": "fill:blue;fill-opacity:0.25"})
            content += (
                """<circle cx="{}" cy="{}" r="{}" style="fill:blue;fill-opacity:0.25" />""".format(cx, cy, r))
    content += "</g>"
    return root


def draw_svg(params, points, insert_coordinate_list):
    """

    :param params:
    :param points:
    :param insert_coordinate_list
    :return:
    """
    polyline_path = []
    for point in points:
        x, y = point
        polyline_path.append("{},{}".format(x, y))

    root = init_svg(params)

    polyline_path = " ".join(polyline_path)
    ElementTree.SubElement(root, "polyline",
                           {"style": "fill:none;stroke:black;stroke-width:1", "points": polyline_path})
    # 嵌件路径生成
    gen_circle(root, insert_coordinate_list)
    tree = ElementTree.ElementTree(root)
    tree.write("board_profile.svg", xml_declaration=True, encoding="UTF-8")
