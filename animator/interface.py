import tkinter as tk

from core import *
from objects import *
from geometry import *


class Window:

    __objects = {}

    def add_shape(self, shape, identifier=None):
        name = f'create_{shape.suffix}({shape.args()})'
        scope = {'canvas': self.canvas, 'identifier': identifier}
        exec(f'''object_id = canvas.{name}
if identifier is not None:
    canvas.itemconfig(object_id, tags=identifier)
''', scope)
        object_id = scope['object_id'] if identifier is None else identifier
        self.__objects[object_id] = shape

    def remove_shape(self, identifier):
        self.canvas.delete(identifier)
        del self.__objects[identifier]

    def run_animation(self, timeline: Timeline):
        pass

    def __init__(self, frame: Rect = Rect(500, 300, Point(300, 300)),
                 title='Window'):
        super().__init__()
        tk_object = tk.Tk()
        tk_object.title(title)
        geometry = f'{frame.width}x{frame.height}+{frame.origin.x}+{frame.origin.y}'
        tk_object.geometry(geometry)
        tk_object.resizable(False, False)
        self.__tk_object = tk_object
        self.canvas = tk.Canvas(self.__tk_object, bd=0, width=frame.width, height=frame.height, )
        self.canvas.pack()

    def show(self):
        self.__tk_object.mainloop()

    def dismiss(self):
        self.__tk_object.destroy()


class Interface:

    def run(self):
        self.__main_window.show()

    def add_shape(self, shape: Shape):
        self.__main_window.add_shape(shape)

    def configure_canvas(self, **flags):
        pass

    def __init__(self, main=Window(), name='Automator'):
        self.__main_window = main
