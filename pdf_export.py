#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-10
# Desc: PDF

import io

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as c

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


def draw_pdf(params, points, insert_coordinate_list):
    """

    :param params:
    :param points:
    :param insert_coordinate_list:
    :return:
    """
    overall_length = params.get("overall_length")

    buffer = io.BytesIO()
    canvas = c.Canvas(buffer, pagesize=(overall_length * mm, 330 * mm))
    canvas.setLineWidth(4)
    canvas.setPageCompression(0)
    canvas._filename = filename
    canvas.setDash(10, 3)
    canvas.setStrokeAlpha(0.3)
    canvas.setLineWidth(0.5)

    # 虚线辅助线
    canvas.line(0, 150 * mm, overall_length * mm, 150 * mm)
    canvas.line(180 * mm, 0 * mm, 180 * mm, 300 * mm)
    canvas.line(760 * mm, 0 * mm, 760 * mm, 300 * mm)
    canvas.line(1340 * mm, 0 * mm, 1340 * mm, 300 * mm)

    path = canvas.beginPath()
    for index, point in enumerate(points, start=1):
        x = point[0]
        y = point[1]
        if index == 1:
            path.moveTo(x * mm, y * mm)
        else:
            path.lineTo(x * mm, y * mm)

    canvas.setDash()
    canvas.setStrokeAlpha(1)
    canvas.setLineWidth(1)
    canvas.drawPath(path, stroke=1, fill=0)

    # 嵌件路径生成
    for insert in insert_coordinate_list:
        x, y = insert
        draw_insert(canvas, x, y)

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

    :param stream_data:
    :return:
    """
    offset1 = stream_data.find("stream\n")
    offset2 = stream_data.find("\nendstream")
    offset = offset2 - offset1 - 7
    print(offset2 - offset1 - 7)
    return offset


def cal_xref_trailer(objs):
    # 开始写入交叉引用表
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
    header = """%PDF-1.1\n%âãÏÓ\n"""
    write_pdf(header)
    write_pdf("\n")

    # step2: 顺序写入obj
    objects = []

    obj1 = {"/Kids": "[2 0 R]", "/Count": "1", "/Type": "/Pages"}
    objects.append({"data": obj1})

    obj2 = {"/Rotate": "0", "/Parent": "1 0 R", "/Resources": "3 0 R", "/MediaBox": "[0 0 792 612]",
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
