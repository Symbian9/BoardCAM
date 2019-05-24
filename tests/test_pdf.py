#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@boardcam.org>
# Date: 2019-05-07
# Desc: 


import io

from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white


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
    p._filename = "demo.pdf"
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
    canvas.setLineWidth(4)
    canvas.setPageCompression(0)
    canvas._filename = "demo.pdf"
    if debug:
        canvas.scale(2.8, 2.8)  # make it big
        canvas.setLineWidth(1)  # small lines
    # canvas.setDash(10, 3)
    # canvas.setStrokeAlpha(0.3)
    # canvas.setLineWidth(0.5)

    # 虚线辅助线
    canvas.line(0, 150 * mm, 1520 * mm, 150 * mm)
    # canvas.line(180 * mm, 0 * mm, 180 * mm, 300 * mm)
    # canvas.line(760 * mm, 0 * mm, 760 * mm, 300 * mm)
    # canvas.line(1340 * mm, 0 * mm, 1340 * mm, 300 * mm)
    #
    # path = canvas.beginPath()
    # path.moveTo(0 * mm, 150 * mm)
    # path.lineTo(180*mm, 300 * mm)
    # path.lineTo(760 * mm, 290 * mm)
    # path.lineTo(1340 * mm, 300 * mm)
    # path.lineTo(1520 * mm, 150 * mm)
    # path.lineTo(1340 * mm, 0 * mm)
    # path.lineTo(760 * mm, 10 * mm)
    # path.lineTo(180 * mm, 0 * mm)
    # path.close()
    #
    # canvas.setDash()
    # canvas.setStrokeAlpha(1)
    # canvas.setLineWidth(1)
    # canvas.drawPath(path, stroke=1, fill=0)

    canvas.showPage()
    canvas.save()


if __name__ == "__main__":
    # some_view()
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    canvas = canvas.Canvas(buffer, pagesize=(1520 * mm, 300 * mm))
    penciltip(canvas, debug=0)
