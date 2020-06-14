from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import *

import pars_work

URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
data = pars_work.get_data(URL)

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]
d = Drawing(400, 200)

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)), list(zip(times, high)), list(zip(times, low))]

lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

d.add(lp)
d.add(String(250, 150, 'Sunspots', fillColor=colors.red))

renderPDF.drawToFile(d, 'report1.pdf', 'Sunspots')
