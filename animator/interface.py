import tkinter as tk
from time import sleep

from core import *
from objects import *
from geometry import *


class Window:

    __objects = {}

    def add_object(self, object: GeometryObject):
        name = f'create_{object.suffix}({object.args()})'
        identifier = object.identifier
        scope = {'canvas': self.canvas, 'identifier': identifier}
        exec(f'''object_id = canvas.{name}
if identifier is not None:
    canvas.itemconfig(object_id, tags=identifier)
''', scope)
        object_id = scope['object_id'] if identifier is None else identifier
        self.__objects[object_id] = object
        return object_id

    def remove_shape(self, identifier):
        self.canvas.delete(identifier)
        del self.__objects[identifier]

    def run_animation(self, timeline: Timeline, fps: int = 24):
        total_frames = fps * timeline.total_duration()
        interval = 1 / fps
        for block, animations in timeline.animations():
            sleep(block.delay)

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

    def add_object(self, object: GeometryObject):
        return self.__main_window.add_object(object)

    def configure_canvas(self, **flags):
        pass

    def __init__(self, main=Window(), name='Automator'):
        self.__main_window = main
