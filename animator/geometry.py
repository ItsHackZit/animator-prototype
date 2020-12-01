import tkinter as tk

from core import *


class GeometryObject:

    @staticmethod
    def assemble_args(args: dict) -> str:
        defaults = [str(i) for i in args.pop('args')]
        pairs = [f'{i}={j}' for i, j in args.items()]
        return ', '.join(defaults + pairs)

    def __init__(self, origin: Point, identifier=None, **flags):
        self.origin = origin
        self.identifier = identifier
        keys = {'fill': 'fill'}
        for key, value in flags.items():
            if key in keys.keys():
                setattr(self, keys[key], value)


class Path(GeometryObject):
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
    __points: [Point] = []
    endstyle = EndStyle.DEFAULT
    joinstyle = JoinStyle.ROUND

    def line(self, end: Point):
        self.__points.append(end)

    def args(self) -> str:
        paths = [j for i in [(i.x, i.y) for i in self.__points] for j in i]
        flags = self.__dict__.copy()
        flags['args'] = [self.origin.x, self.origin.y] + paths
        del flags['origin']
        return Shape.assemble_args(flags)

    def __init__(self, init_point: Point, identifier=None, **flags):
        super().__init__(init_point, identifier=identifier, **flags)
        keys = {'stroke': 'outline', 'end': 'endstyle', 'join': 'joinstyle',
                'dash': 'dash', 'dash_offset': 'dashoffset', 'width': 'width'}
        for key, value in flags.items():
            if key in keys.keys():
                if key == 'end':
                    setattr(self, keys[key], self.EndStyle(value))
                elif key == 'join':
                    setattr(self, keys[key], self.JoinStyle(value))
                else:
                    setattr(self, keys[key], value)


class Shape(GeometryObject):

    def __init__(self, origin: Point, identifier=None, **flags):
        super().__init__(origin, identifier=identifier, **flags)
        keys = {'bd_color': 'outline', 'bd_stroke': 'width'}
        for key, value in flags.items():
            if key in keys.keys():
                setattr(self, keys[key], value)


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

    def __init__(self, frame: Rect, identifier=None, **flags):
        super().__init__(frame.origin, identifier=identifier, **flags)
        self.frame = frame


class Arc(Rectangle):
    suffix = 'arc'

    def __init__(self, frame: Rect, start: int, angle: int, identifier=None, **flags):
        super().__init__(frame, identifier=identifier, **flags)
        keys = {'start': 'start', 'angle': 'extent', 'stroke': 'outline',
                'end': 'endstyle', 'join': 'joinstyle', 'dash': 'dash',
                'dash_offset': 'dashoffset', 'width': width}
        for key, value in flags.items():
            if key in keys.keys():
                if key == 'end':
                    setattr(self, keys[key], self.EndStyle(value))
                elif key == 'join':
                    setattr(self, keys[key], self.JoinStyle(value))
                else:
                    setattr(self, keys[key], value)


class Oval(Rectangle):
    suffix = 'oval'

    def __init__(self, frame: Rect, identifier=None, **flags):
        super().__init__(frame, identifier=identifier, **flags)
