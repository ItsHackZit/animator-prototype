from tkinter import *
import numpy as np
from time import sleep

from extras import *


class alien(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.circle1 = self.canvas.create_oval(20, 260, 120, 360, outline='white', fill='blue')
        self.canvas.pack()
        self.root.after(0, self.run_animation)
        self.root.mainloop()

    def run_animation(self):
        self.move(50, 240, 2, 120)

    def move(self, new_x, new_y, duration, fps):
        total_frames = fps * duration
        interval = 1 / fps
        coords = self.canvas.coords(self.circle1)
        old_x, old_y = coords[0], coords[-1]
        x_frames = np.linspace(old_x, new_x, total_frames)
        y_frames = np.linspace(old_y, new_y, total_frames)
        for x, y in list(zip(x_frames, y_frames)):
            c = self.canvas.coords(self.circle1)
            _x, _y = c[0], c[-1]
            sleep(interval)
            self.canvas.move(self.circle1, x - _x, y - _y)
            self.canvas.update()


alien()
