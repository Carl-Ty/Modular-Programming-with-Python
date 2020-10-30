"""
Test Status
Generates:
> chart_bar.png with title, Y-axis, x-axis and bar chart at this point
> chart_line.png with title, Y-axis, x-axis and line chart at this point

Tests the continued functionality after moving current renderer files to the
renderers\png
Add renderers\pdf and renderers.py

Add rendering in PDF to the project complete

Had not checked out the branch till here
"""

import charter

chart = charter.new_chart()
charter.set_title(chart, "Wild Parrot Deaths per Year")
charter.set_x_axis(chart,
                   ["2009", "2010", "2011", "2012", "2013",
                    "2014", "2015"])
charter.set_y_axis(chart, minimum=0, maximum=700,
                   labels=[0, 100, 200, 300, 400, 500, 600, 700])
charter.set_series(chart, [250, 270, 510, 420, 680, 580, 450])
charter.set_series_type(chart, "bar")
charter.generate_chart(chart, "chart_bar.png")
charter.set_series_type(chart, "line")
charter.generate_chart(chart, "chart_line.png")

charter.set_series_type(chart, "bar")
charter.generate_chart(chart, "chart_bar.pdf")
charter.set_series_type(chart, "line")
charter.generate_chart(chart, "chart_line.pdf")