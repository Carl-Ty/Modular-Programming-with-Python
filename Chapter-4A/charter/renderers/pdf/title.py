"""
The way we calculate the width and the height of the text is different. For the
width, we call the canvas's stringWidth() function, while for the height, we
multiply the font size of the text by 1.2. By default, ReportLab leaves a gap
of 20% of the font size between lines of text, so multiplying the font size
by 1.2 is an accurate way of calculating the height of a line of text.

The units used to calculate the position of elements on the page are different.
ReportLab measures all positions and sizes using points rather than pixels.
A point is roughly 1/72nd of an inch. Fortunately, one point is fairly close to
the size of a pixel on a typical computer screen; this allows us to ignore the
different measurement systems and have the PDF output still look good.

PDF files use a different coordinate system to PNG files. In a PNG-format file,
the top of the image has a y value of zero, while for PDF files y=0 is at
the bottom of the image. This means that all our positions on the page have to
be calculated relative to the bottom of the page, rather than the top of the
image as was done with the PNG renderers.

The colors are specified using RGB color values, where each component of the
color is given as a number between zero and one. For example, a color value of
(0.25,0.25,0.625) is equivalent to the hex color code #4040a0.
"""
from ...constants import *


def draw(chart, canvas):
    text_width = canvas.stringWidth(chart['title'],
                                    "Helvetica", 24)
    text_height = 24 * 1.2

    left = CHART_WIDTH / 2 - text_width / 2
    bottom = CHART_HEIGHT - TITLE_HEIGHT / 2 + text_height / 2

    canvas.setFont("Helvetica", 24)
    canvas.setFillColorRGB(0.25, 0.25, 0.625)
    canvas.drawString(left, bottom, chart['title'])
