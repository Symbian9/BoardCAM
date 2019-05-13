#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-11
# Desc:


filename = "line.pdf"


def gen_trailer():
    pass


def gen_xref():
    pass


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


def pack_obj(obj_no, data, is_nl):
    """
    对象号
    :param obj_no:
    :param data:
    :return:
    """
    if is_nl:
        content = "{} 0 obj\n<<\n{}\n>>\nendobj\n".format(obj_no, data)
    else:
        content = "{} 0 obj\n<<\n{}\n>>\nendobj".format(obj_no, data)
    return content


def cal_length(data):
    offset1 = data.find("stream\n")
    offset2 = data.find("\nendstream")
    offset = offset2 - offset1 - 7
    print(offset2 - offset1 - 7)
    return data.format(offset)


def cal_xref(objs):
    write_pdf(" xref\n")
    obj_no = len(objs)
    write_pdf("0 {}\n".format(obj_no + 1))
    write_pdf("0000000000 65535 f \n")
    for i in range(1, obj_no + 1):
        mark = "{} 0 obj".format(i)
        offset = find_offset(mark.encode())
        write_pdf("{} 00000 n \n".format(str(offset).zfill(10)))

    return ""


def cal_trailer(objs):
    offset = find_offset("xref".encode())
    write_pdf("trailer\n\n")
    write_pdf("""<<\n/Root {} 0 R\n/Size {}\n>>\nstartxref\n{}\n%%EOF\n""".format(len(objs), len(objs) + 1, offset))


class PDFObj:
    def __init__(self):
        pass


class Stream:
    def __init__(self):
        pass

    def pack(self):
        return ""

    def start(self):
        return "stream"

    def end(self):
        return "endstream"


class PDFDict:
    pass


def pack_obj_new(obj_info, dict_data):
    """

    :param obj_info:
    :param dict_data:
    :return:
    """
    content = "{}\n<<\n".format(obj_info)
    for key in dict_data.keys():
        value = dict_data.get(key)
        if type(value) == dict:
            content += "<<\n"
            for child_key in value.keys():
                print(child_key)
                child_value = value.get(child_key)
                content += "{} {}\n".format(child_key, child_value)

            content += ">>\n"
        else:
            content += "{} {}\n".format(key, value)

    content += ">>\nendobj\n"
    return content


if __name__ == "__main__":
    header = """%PDF-1.1\n%âãÏÓ\n"""
    write_pdf(header)

    objects = []
    obj1 = """/Kids [2 0 R]\n/Count 1\n/Type /Pages"""
    a = {"/Kids": "[2 0 R]", "/Count": 1, "/Type": "/Pages"}
    # write_pdf(pack_obj(1, obj1, True))
    write_pdf(pack_obj_new("1 0 obj", a))
    objects.append(obj1)

    obj2 = """/Rotate 0\n/Parent 1 0 R\n/Resources 3 0 R\n/MediaBox [0 0 792 612]\n/Contents [4 0 R]\n/Type /Page"""
    b = {"/Rotate": 0, "/Parent": "1 0 R", "/Resources": "3 0 R", "/MediaBox": "[0 0 792 612]", "/Contents": "[4 0 R]",
         "/Type": "/Page"}
    # write_pdf(pack_obj(2, obj2, True))
    write_pdf(pack_obj_new("2 0 obj", b))
    objects.append(obj2)

    obj3 = """/Font \n<<\n/F0 \n<<\n/BaseFont /Times-Italic\n/Subtype /Type1\n/Type /Font\n>>\n>>"""
    c = {"/Font": {"/F0": {"/Type": "/Font", "/BaseFont": "/Times-Italic", "/Subtype": "/Type1"}}}
    # write_pdf(pack_obj(3, obj3, True))
    write_pdf(pack_obj_new("3 0 obj", c))
    objects.append(obj3)

    # Length为stream 和endstream之间的长度
    stream = """/Length {}\n>>\nstream\n200 150 m 600 450 l S \n\nendstream """
    d = {"/Length": 23}
    stream = cal_length(stream)
    write_pdf(pack_obj_new("4 0 obj", d))
    # write_pdf(pack_obj(4, stream, True))
    objects.append(stream)

    obj5 = """/Pages 1 0 R\n/Type /Catalog"""
    e = {"/Pages": "1 0 R", "/Type": "/Catalog"}
    # write_pdf(pack_obj(5, obj5, False))
    write_pdf(pack_obj_new("5 0 obj", e))
    objects.append(obj5)

    cal_xref(objects)
    cal_trailer(objects)
