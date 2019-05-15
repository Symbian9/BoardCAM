#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019-05-10
# Desc: PDF


filename = "board_profile.pdf"


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
