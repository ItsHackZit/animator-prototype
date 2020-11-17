import tkinter as tk

from core import *
import escape


class Path:
    class EndStyle:
        ROUND = tk.ROUND
        PROMINENT = tk.PROJECTING
        DEFAULT = tk.BUTT

        def __init__(self, name: str):
            if name == 'ROUND':
                self = self.ROUND
            elif name == 'PROMINENT':
                self = self.PROMINENT
            elif name == 'DEFAULT':
                self = self.DEFAULT
            else:
                raise Exception(f'Invalid style name \'{name}\'.')

    class JoinStyle:
        ROUND = tk.ROUND
        BEVEL = tk.BEVEL
        MITER = tk.MITER

        def __init__(self, name: str):
            if name == 'ROUND':
                self = self.ROUND
            elif name == 'BEVEL':
                self = self.BEVEL
            elif name == 'MITER':
                self = self.MITER
            else:
                raise Exception(f'Invalid style name \'{name}\'.')

    suffix = 'line'
    points: [Point] = []
    endstyle = EndStyle.DEFAULT
    joinstyle = JoinStyle.ROUND

    def line(self, end: Point):
        self.points.append(end)

    def args(self) -> str:
        paths = [j for i in [(i.x, i.y) for i in self.points] for j in i]
        flags = self.__dict__.copy()
        flags['args'] = [self.origin.x, self.origin.y] + paths
        del flags['origin']
        return Shape.assemble_args(flags)

    @escape
    def __init__(self, init_point: Point, **flags):
        self.origin = init_point
        self.fill = flags['fill']
        self.stroke = flags['stroke']
        self.endstyle = self.EndStyle(flags['end'])
        self.joinstyle = self.JoinStyle(flags['join'])
        self.dash = flags['dash']
        self.dashoffset = flags['dash_offset']
        self.width = flags['width']


class Shape:

    @staticmethod
    def assemble_args(args: dict) -> str:
        defaults = [str(i) for i in args.pop('args')]
        pairs = [f'{i}={j}' for i, j in args.items()]
        return ', '.join(defaults + pairs)

    @escape
    def __init__(self, origin: Point, **flags):
        self.origin = origin
        self.fill = flags['fill']
        self.outline = flags['bd_color']
        self.width = flags['bd_stroke']


class Rectangle(Shape):
    suffix = 'rectangle'

    def args(self) -> str:
        flags = self.__dict__.copy()
        x0, y0 = self.origin.x, self.origin.y
        x1 = x0 + self.frame.width + 1
        y1 = y0 + self.frame.height + 1
        flags['args'] = [x0, y0, x1, y1]
        del flags['origin'], flags['frame']
        return Shape.assemble_args(flags)

    def __init__(self, frame: Rect, **flags):
        super().__init__(frame.origin, **flags)
        self.frame = frame


class Oval(Rectangle):
    suffix = 'oval'

    def __init__(self, frame: Rect, **flags):
        super().__init__(frame, **flags)
