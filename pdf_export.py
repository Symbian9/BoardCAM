#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-10
# Desc: PDF

import io
import math

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as c

from config import border
from math_tools import mm_to_dpi
from path import move, move_path
from points import Point
from until import list_to_str

filename = "board_profile.pdf"


def draw_insert(canvas, x, y):
    """
    绘制嵌件位置
    :param canvas:
    :param x: 圆心X坐标
    :param y: 圆心Y坐标
    :return:
    """
    # r=0.5作为圆心
    radius = [0.5, 10, 18]
    for r in radius:
        canvas.circle(x * mm, y * mm, r * mm)
    return canvas


def draw_profile(points, height):
    """
    绘制模具轮廓
    :param points: 轮廓的点
    :param height: 上翘圆弧的高度
    :return:
    """
    width = abs(points[0].x - points[-1].x)
    height = math.ceil(height)
    width = math.ceil(width)
    buffer = io.BytesIO()
    pagesize = [width + border * 2, height + border * 2]
    canvas = c.Canvas(buffer, pagesize=(pagesize[0] * mm, pagesize[1] * mm))
    canvas.setLineWidth(4)

    # 设置不压缩PDF stream
    canvas.setPageCompression(0)
    canvas._filename = "profile.pdf"

    # 水平翻转
    points = [Point(point.x, height * 2 - point.y) for point in points]
    points = move(border, height + border, points)
    path = canvas.beginPath()
    for index, point in enumerate(points, start=1):
        if index == 1:
            path.moveTo(point.x * mm, point.y * mm)
        else:
            path.lineTo(point.x * mm, point.y * mm)

    canvas.setDash()
    canvas.setStrokeAlpha(1)
    canvas.setLineWidth(1)
    canvas.drawPath(path, stroke=1, fill=0)

    canvas.showPage()
    canvas.save()


def export_pdf(params, points, insert_coordinate_list):
    """
    绘制PDF
    :param params:
    :param points:
    :param insert_coordinate_list:
    :return:
    """
    nose_width = params.get("nose_width")
    tail_width = params.get("tail_width")
    max_width = max(nose_width, tail_width)
    half_max_width = max_width / 2
    nose_length = params.get("nose_length")
    tail_length = params.get("tail_length")
    running_length = params.get("running_length")
    overall_length = nose_length + running_length + tail_length
    waist_line = running_length / 2 + nose_length
    tail_line = nose_length + running_length

    buffer = io.BytesIO()
    pagesize = [overall_length + border * 2, max_width + border * 2]
    canvas = c.Canvas(buffer, pagesize=(pagesize[0] * mm, pagesize[1] * mm))
    canvas.setLineWidth(4)

    # 设置不压缩PDF stream
    canvas.setPageCompression(0)
    canvas._filename = filename

    # 设置辅助线 点距
    canvas.setDash(10, 3)

    # 设置辅助线透明度
    canvas.setStrokeAlpha(0.4)
    canvas.setLineWidth(0.5)

    # 虚线辅助线
    canvas.line(0, (half_max_width + border) * mm, (overall_length + 2 * border) * mm, (half_max_width + border) * mm)
    canvas.line((nose_length + border) * mm, 0 * mm, (nose_length + border) * mm, (nose_width + 2 * border) * mm)
    canvas.line((waist_line + border) * mm, 0 * mm, (waist_line + border) * mm, (max_width + 2 * border) * mm)
    canvas.line((tail_line + border) * mm, 0 * mm, (tail_line + border) * mm, (tail_width + 2 * border) * mm)

    points = move_path(points, border, border)

    path = canvas.beginPath()
    for index, point in enumerate(points, start=1):
        # x, y = point
        if index == 1:
            path.moveTo(point.x * mm, point.y * mm)
        else:
            path.lineTo(point.x * mm, point.y * mm)

    canvas.setDash()
    canvas.setStrokeAlpha(1)
    canvas.setLineWidth(1)
    canvas.drawPath(path, stroke=1, fill=0)

    # 嵌件路径生成
    for insert in insert_coordinate_list:
        x, y = insert
        draw_insert(canvas, x + border, y + border)

    canvas.showPage()
    canvas.save()


def find_offset(mark):
    """
    标记
    :param mark:
    :return:
    """
    with open(filename, mode="rb") as file:
        data = file.read()
        return data.find(mark)


def write_pdf(content):
    with open(filename, mode="ab") as file:
        file.write(content.encode())


def cal_length(stream_data):
    """
    计算PDF stream 字节长度
    :param stream_data:
    :return:
    """
    keyword_start = stream_data.find("stream\n")
    keyword_end = stream_data.find("\nendstream")
    stream_length = keyword_end - keyword_start - 7
    return stream_length


def cal_xref_trailer(objs):
    """
    开始写入交叉引用表
    :param objs:
    :return:
    """
    write_pdf("xref\n")
    obj_no = len(objs)
    write_pdf("0 {}\n".format(obj_no + 1))
    write_pdf("0000000000 65535 f \n")
    for i in range(1, obj_no + 1):
        mark = "{} 0 obj".format(i)
        offset = find_offset(mark.encode())
        write_pdf("{} 00000 n \n".format(str(offset).zfill(10)))

    write_pdf("\n")

    # 开始写入trailer
    offset = find_offset("xref".encode())
    write_pdf("trailer")
    trailer = {"/Root": "{} 0 R".format(len(objs)), "/Size": "{}".format(len(objs) + 1)}
    data = str(trailer)
    content = data.replace("{", "\n<<\n").replace("}", "\n>>")
    content = content.replace("', '", "\n").replace("'", "").replace(":", "")
    write_pdf(content)
    write_pdf("\n")
    write_pdf("\nstartxref\n{}\n%%EOF\n".format(offset))


def pack_objs(objects):
    """
    将obj按照一定规则组合起来
    :param objects:
    :return:
    """
    result = ""

    for index, obj in enumerate(objects, start=1):
        data = obj.get("data")
        stream_data = obj.get("stream")
        if stream_data:
            data.update({"/Length": str(cal_length(stream_data))})

        data = str(data)
        content = data.replace("{", "\n<<\n").replace("}", "\n>>")
        content = content.replace("', '", "\n").replace("'", "").replace(":", "")

        if stream_data:
            result += "{} 0 obj".format(index) + content + "\n" + stream + "\nendobj\n"
        else:
            result += "{} 0 obj".format(index) + content + "\nendobj\n"

        result += "\n"

    return result


if __name__ == "__main__":
    # step1: 写入文件头
    pdf_version = "%PDF-1.1\n"

    header = """%PDF-1.1\n%âãÏÓ\n"""
    write_pdf(header)
    write_pdf("\n")

    # step2: 顺序写入obj
    objects = []

    obj1 = {"/Kids": "[2 0 R]", "/Count": "1", "/Type": "/Pages"}
    objects.append({"data": obj1})

    width = 300
    height = 250
    media_box = [0, 0, mm_to_dpi(width), mm_to_dpi(height)]

    obj2 = {"/Rotate": "0", "/Parent": "1 0 R", "/Resources": "3 0 R", "/MediaBox": list_to_str(media_box),
            "/Contents": "[4 0 R]", "/Type": "/Page"}
    objects.append({"data": obj2})

    obj3 = {"/Font": {"/F0": {"/Type": "/Font", "/BaseFont": "/Times-Italic", "/Subtype": "/Type1"}}}
    objects.append({"data": obj3})

    stream = """stream\n200 150 m 600 450 l S \nendstream"""
    obj4 = {"/Length": ""}
    objects.append({"data": obj4, "stream": stream})

    obj5 = {"/Pages": "1 0 R", "/Type": "/Catalog"}
    objects.append({"data": obj5})

    write_pdf(pack_objs(objects))
    cal_xref_trailer(objects)
