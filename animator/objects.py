from core import *
from geometry import *


class Animation:
    duration = 0.0
    timing_funtion = None


class TweeningAnimation(Animation):

    def __init__(self, object_identifier: str):
        super().__init__()
        self.object_identifier = object_identifier


class KeyframeAnimation(Animation):

    values = []
    key_times: [float] = []

    def __init__(self, object_identifier: str):
        super().__init__()
        self.object_identifier = object_identifier


class TransitionAnimation(Animation):
    pass


class AnimationGroup:
    animations: [Animation] = []


class HybridKeyframe:
    pass


class Keyframe:
    __animations: [Animation] = []


class Timeline:
    __keyframes: [Keyframe] = []
