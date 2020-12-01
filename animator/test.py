from tkinter import *
import numpy as np
from time import sleep

from extras import *


class alien(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.circle1 = self.canvas.create_oval(20, 260, 120, 360, outline='white', fill='blue')
        self.canvas.pack()
        self.root.after(0, self.run_animation)
        self.root.mainloop()

    def run_animation(self):
        self.move(450, 380, 2, 120)

    @staticmethod
    def ease_inout_quad(current_time, start, change, duration):
        current_time /= duration / 2
        if current_time < 1:
            return change / 2 * current_time * current_time + start
        current_time -= 1
        return -change / 2 * (current_time * (current_time - 2) - 1) + start


    def move(self, new_x, new_y, duration, fps):
        total_frames = fps * duration
        interval = 1 / fps
        coords = self.canvas.coords(self.circle1)
        old_x, old_y = coords[0], coords[-1]
        x_frames = [alien.ease_inout_quad(i, old_x, new_x, total_frames) for i in range(total_frames + 1)]
        y_frames = [alien.ease_inout_quad(i, old_y, new_y, total_frames) for i in range(total_frames + 1)]
        del x_frames[0], y_frames[0]
        print(list(zip(x_frames, y_frames)))
        for x, y in list(zip(x_frames, y_frames)):
            c = self.canvas.coords(self.circle1)
            _x, _y = c[0], c[-1]
            sleep(interval)
            self.canvas.move(self.circle1, x - _x, y - _y)
            self.canvas.update()


alien()
