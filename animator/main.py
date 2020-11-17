from imports import *

app = Interface(name='Test')
rectangle = Oval(Rect(100, 100, Point(100, 100)),
                 fill=Color(r=71, g=171, b=75), bd_stroke=3)
app.add_shape(rectangle)
path = Path(Point(100, 100), dash=(5, 3), fill=Color(r=71, g=171, b=75), width=3)
path.line(Point(140, 110))
app.add_shape(path)
app.run()
