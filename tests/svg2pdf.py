from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

drawing = svg2rlg("output1.svg")
renderPDF.drawToFile(drawing, "output1.pdf")
