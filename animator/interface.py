import tkinter as tk

from core import *
from geometry import *


class Window:

    __objects = {}

    def add_shape(self, shape):
        name = f'create_{shape.suffix}({shape.args()})'
        scope = {'canvas': self.canvas}
        exec(f'object_id = canvas.{name}', scope)
        self.__objects[scope['object_id']] = shape

    def get_shape(self, id):
        return self.__objects[id]

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

    def __del__(self):
        self.__main_window.dismiss()
