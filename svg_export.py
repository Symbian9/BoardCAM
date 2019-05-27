#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-07
# Desc: SVG生成

from math import cos, sin, pi, sqrt
from xml.etree import ElementTree

from config import COPYRIGHT, SLOGAN, side_step
from until import value_to_str


def init_svg(params):
    """
    生成辅助线 框架
    :param params:
    :return:
    """
    root = ElementTree.Element("svg")
    root.attrib = {"width": "100%", "height": "100%", "version": "1.1", "xmlns": "http://www.w3.org/2000/svg"}

    half_nose_width = params.get("half_nose_width")
    half_running_length = params.get("half_running_length")
    nose_width = params.get("nose_width")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    overall_length = params.get("overall_length")
    tail_width = params.get("tail_width")

    frame = ElementTree.SubElement(root, "g", {"style": "stroke:#000000;stroke-width:1;", "stroke-dasharray": "5,5"})

    # 板头垂直虚线
    ElementTree.SubElement(frame, "line",
                           value_to_str({"x1": nose_length, "y1": 0 + 5, "x2": nose_length,
                                         "y2": nose_width - 5}))

    # 板尾垂直虚线
    ElementTree.SubElement(frame, "line",
                           value_to_str({"x1": nose_length + running_length, "y1": 0 + 5,
                                         "x2": nose_length + running_length, "y2": tail_width - 5}))

    # 水平中线虚线
    ElementTree.SubElement(frame, "line",
                           value_to_str({"x1": 0, "y1": half_nose_width,
                                         "x2": overall_length, "y2": half_nose_width}))
    # 板腰垂直虚线
    ElementTree.SubElement(frame, "line",
                           value_to_str({"x1": nose_length + half_running_length, "y1": 0 + 20,
                                         "x2": nose_length + half_running_length, "y2": nose_width - 20}))

    # 版权信息
    logo_tag = ElementTree.SubElement(root, "g")
    copyright_tag = ElementTree.SubElement(logo_tag, "text",
                                           value_to_str({"x": 800, "y": 200, "fill": "black", "fill-opacity": 0.6}))
    copyright_tag.text = COPYRIGHT

    # slogan
    slogan_tag = ElementTree.SubElement(logo_tag, "text",
                                        value_to_str({"x": 805, "y": 215, "fill": "black", "font-size": 9,
                                                      "font-family": "Times-Italic"}))
    slogan_tag.text = SLOGAN

    # 比例尺 TODO 要找一个合适位置放置
    scale_group = ElementTree.SubElement(root, "g", {"style": "stroke:black;stroke-width:0.3"})
    scale_text = ElementTree.SubElement(scale_group, "text",
                                        value_to_str({"x": 12, "y": 8, "fill": "black", "font-size": 3}))
    scale_text.text = "1cm"
    ElementTree.SubElement(scale_group, "line",
                           value_to_str({"x1": 10, "y1": 8, "x2": 10, "y2": 12}))
    ElementTree.SubElement(scale_group, "line",
                           value_to_str({"x1": 10, "y1": 10, "x2": 20, "y2": 10, "stroke-width": 0.8}))
    ElementTree.SubElement(scale_group, "line",
                           value_to_str({"x1": 20, "y1": 8, "x2": 20, "y2": 12}))

    return root


def gen_circle(root, insert_coordinate_list):
    """
    圆形生成
    :param root: 根节点
    :param insert_coordinate_list: 每个嵌件位置的坐标
    :return:
    """
    inserts_group = ElementTree.SubElement(root, "g", {"style": "stroke-width:1;stroke:black", })
    for insert in insert_coordinate_list:
        cx, cy = insert
        for r in ["0.5", "10", "18"]:
            ElementTree.SubElement(inserts_group, "circle",
                                   value_to_str({"cx": cx, "cy": cy, "r": r, "style": "fill:blue;fill-opacity:0.25"}))
    return root


def export_svg(params, points, insert_coordinate_list):
    """

    :param params:
    :param points:
    :param insert_coordinate_list
    :return:
    """
    root = init_svg(params)

    polyline_path = " ".join(["{},{}".format(point[0], point[1]) for point in points])
    ElementTree.SubElement(root, "polyline",
                           {"style": "fill:none;stroke:black;stroke-width:1", "points": polyline_path})
    # 嵌件路径生成
    gen_circle(root, insert_coordinate_list)

    # 生成SVG
    tree = ElementTree.ElementTree(root)
    tree.write("board_profile.svg", xml_declaration=True, encoding="UTF-8")


def gen_circle_path(params):
    """
    生成圆弧方程
    :param params:
    :return:
    """
    tip_radius = params.get("tip_radius")
    nose_length = params.get("nose_length")
    running_length = params.get("running_length")
    half_running_length = running_length / 2
    camber = params.get("camber")

    # r^2 = (r-15)^2 + (half_running_length)^2
    camber_radius = (pow(half_running_length, 2) + pow(camber, 2)) / camber * 2

    root = ElementTree.Element("svg")
    root.attrib = {"width": "100%", "height": "100%", "version": "1.1", "xmlns": "http://www.w3.org/2000/svg"}

    points = []
    cx, cy = 0, 0
    for angle in range(45, 90 + 1):
        x = cx + tip_radius * cos(angle * pi / 180)
        y = cy + tip_radius * sin(angle * pi / 180)
        points.append([x, y])

    camber_list = []
    for x1 in range(nose_length, nose_length + running_length + side_step, side_step):
        y1 = sqrt(pow(camber_radius, 2) - pow(180 + 1160 / 2 - x1, 2))
        y1 = camber_radius - y1
        camber_list.append([x1, y1 + 200])

    # 上翘弧线宽度
    width = abs(points[0][0] - points[-1][0])
    left_points = [[abs(point[0] - width), point[1]] for point in points]
    left_points = move(camber_list[0][0], camber_list[0][1], left_points[::-1])
    right_points = move(camber_list[-1][0], camber_list[-1][1], points[::-1])

    tail_tip_path = " ".join(["{},{}".format(point[0], point[1]) for point in right_points])
    nose_tip_path = " ".join(["{},{}".format(point[0], point[1]) for point in left_points])
    bottom_camber_path = " ".join(["{},{}".format(point[0], point[1]) for point in camber_list])

    ElementTree.SubElement(root, "polyline",
                           {"style": "fill:none;stroke:black;stroke-width:1", "points": nose_tip_path})
    ElementTree.SubElement(root, "polyline",
                           {"style": "fill:none;stroke:black;stroke-width:1", "points": bottom_camber_path})
    ElementTree.SubElement(root, "polyline",
                           {"style": "fill:none;stroke:black;stroke-width:1", "points": tail_tip_path})

    tree = ElementTree.ElementTree(root)
    tree.write("flex.svg", xml_declaration=True, encoding="UTF-8")


def move(x, y, points):
    """
    将线段平移到某一点上
    :param x:
    :param y:
    :param points:
    :return:
    """
    x_diff = points[0][0] - x
    y_diff = points[0][1] - y

    return [[point[0] - x_diff, point[1] - y_diff] for point in points]
