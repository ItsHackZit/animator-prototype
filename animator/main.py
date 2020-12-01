from imports import *

app = Interface(name='Test')
oval = Oval(Rect(100, 100, Point(100, 100)),
                 fill=Color(r=71, g=171, b=75), bd_stroke=3)
id = app.add_object(oval)
path = Path(Point(100, 100), dash=(5, 3), fill=Color(r=71, g=171, b=75), width=3)
path.line(Point(140, 110))
app.add_object(path)
animation = BasicAnimation('oval_anim_1', id, 'position')
animation.from_value = (100, 100)
animation.to_value = (150, 175)
app.run()
