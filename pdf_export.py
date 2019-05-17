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


def draw_pdf(points, insert_coordinate_list):
    """

    :param points:
    :param insert_coordinate_list:
    :return:
    """

    buffer = io.BytesIO()
    canvas = c.Canvas(buffer, pagesize=(1520 * mm, 330 * mm))
    canvas.setLineWidth(4)
    canvas.setPageCompression(0)
    canvas._filename = filename
    canvas.setDash(10, 3)
    canvas.setStrokeAlpha(0.3)
    canvas.setLineWidth(0.5)

    # 虚线辅助线
    canvas.line(0, 150 * mm, 1520 * mm, 150 * mm)
    canvas.line(180 * mm, 0 * mm, 180 * mm, 300 * mm)
    canvas.line(760 * mm, 0 * mm, 760 * mm, 300 * mm)
    canvas.line(1340 * mm, 0 * mm, 1340 * mm, 300 * mm)

    path = canvas.beginPath()
    for index, point in enumerate(points, start=1):
        print(point)
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


def gen_trailer():
    pass


def gen_xref():
    pass


def write_pdf(content):
    with open(filename, mode="wb") as file:
        file.write(content.encode())


if __name__ == "__main__":
    header = """%PDF-1.1\n%âãÏÓ\n"""
    obj = """1 0 obj 
<<
/Kids [2 0 R]
/Count 1
/Type /Pages
>>
endobj 
"""
    obj += """
2 0 obj 
<<
/Parent 1 0 R
/Resources 3 0 R
/MediaBox [0 0 612 792]
/Contents [4 0 R]
/Type /Page
>>
endobj
"""
    obj += """
3 0 obj 
<<
/Font 
<<
/F0 
<<
/BaseFont /Times-Italic
/Subtype /Type1
/Type /Font
>>
>>
>>
endobj 
"""
    obj += """
4 0 obj 
<<
/Length 65
>>
stream
1. 0. 0. 1. 50. 700. cm
BT
  /F0 36. Tf
  (Hello, World!) Tj
ET 

endstream 
endobj 
"""
    obj += """
5 0 obj 
<<
/Pages 1 0 R
/Type /Catalog
>>
endobj xref
"""
    xref = """
0 6
0000000000 65535 f 
0000000015 00000 n 
0000000074 00000 n 
0000000182 00000 n 
0000000281 00000 n 
0000000399 00000 n 
trailer
"""
    trailer = """
<<
/Root 5 0 R
/Size 6
>>
startxref
449 
"""
    end_Of_file = "%%EOF"
    new = header + obj + xref + trailer + end_Of_file
    print(new[452])
    print(new.find("xref"))
    write_pdf(new)
