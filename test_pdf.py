#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 


import io

from reportlab.lib.colors import tan, black
from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

def mm_to_dpi(mm):
    """
    毫米转换成dpi
    :param mm:
    :return:
    """
    cm = mm * 0.1
    inch = cm / 2.54  # 1in = 2.54cm
    dpi = 72 * inch
    return dpi


def some_view():
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=(1520 * mm, 300 * mm))
    # 不压缩
    p.setPageCompression(0)
    p._filename = "test.pdf"
    # p.setAuthor("ZhengXiang")
    p.bezier(0 * mm, 200 * mm, 50 * mm, 190 * mm, 10 * mm, 250 * mm, 180 * mm, 300 * mm)
    p.circle(100 * mm, 100 * mm, 18 * mm)
    p.circle(100 * mm, 100 * mm, 10 * mm)
    p.circle(100 * mm, 100 * mm, 0.5 * mm)
    p.line(0 * mm, 200 * mm, 1520 * mm, 200 * mm)
    p.beginPath()

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawString(100, 100, "Hello world.")
    # p.linkURL()

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.


def penciltip(canvas, debug=1):
    u = inch / 10.0
    canvas.setLineWidth(4)
    canvas.setPageCompression(0)
    canvas._filename = "test.pdf"
    if debug:
        canvas.scale(2.8, 2.8)  # make it big
        canvas.setLineWidth(1)  # small lines
    canvas.setStrokeColor(black)
    canvas.setFillColor(tan)
    p = canvas.beginPath()
    p.moveTo(10 * u, 0)
    p.lineTo(0, 5 * u)
    p.lineTo(10 * u, 10 * u)
    p.curveTo(11.5 * u, 10 * u, 11.5 * u, 7.5 * u, 10 * u, 7.5 * u)
    p.curveTo(12 * u, 7.5 * u, 11 * u, 2.5 * u, 9.7 * u, 2.5 * u)
    p.curveTo(10.5 * u, 2.5 * u, 11 * u, 0, 10 * u, 0)
    canvas.drawPath(p, stroke=1, fill=1)
    canvas.setFillColor(black)
    p = canvas.beginPath()
    # p.moveTo(0, 5 * u)

    canvas.showPage()
    canvas.save()


if __name__ == "__main__":
    # some_view()
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    canvas = canvas.Canvas(buffer, pagesize=(1520 * mm, 300 * mm))
    penciltip(canvas, debug=0)
