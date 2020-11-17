from geometry import *
from core import *


class Timeline:
    __keyframes: [Keyframe] = []


class Keyframe:
    __animations: [Animation] = []


class Animation:
    def __init__(self, object_identifier: str):
        self.object_identifier = object_identifier
