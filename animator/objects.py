import math

from core import *
from geometry import *


class Animation:
    property = None
    duration = 0.0
    timing_funtion = None
    calculation_mode = None

    class Functions:
        @staticmethod
        def linear_n(current, start, end, duration):
            return end * current / duration + start

        @staticmethod
        def sine_easein(current, start, end, duration):
            return -end * math.cos(current / duration * (math.pi / 2)) + end + start

        @staticmethod
        def sine_easeout(current, start, end, duration):
            return end * math.sin(current / duration * (math.pi / 2)) + start

        @staticmethod
        def sine_easeinout(current, start, end, duration):
            return -end / 2 * (math.cos(math.pi * current / duration) - 1) + start

        @staticmethod
        def quad_easein(current, start, end, duration):
            current /= duration
            return end * current ** 2 + start

        @staticmethod
        def quad_easeout(current, start, end, duration):
            current /= duration
            return -end * current * (current - 2) + start

        @staticmethod
        def quad_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return end / 2 * current ** 2 + start
            current -= 1
            return -end / 2 * (current * (current - 2) - 1) + start

        @staticmethod
        def cubic_easein(current, start, end, duration):
            current /= duration
            return end * current ** 3 + start

        @staticmethod
        def cubic_easeout(current, start, end, duration):
            current /= duration
            current -= 1
            return end * (current ** 3 + 1) + start

        @staticmethod
        def cubic_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return end / 2 * current ** 3 + start
            current -= 2
            return end / 2 * (current ** 3 + 2) + start

        @staticmethod
        def quart_easein(current, start, end, duration):
            current /= duration
            return end * current ** 4 + start

        @staticmethod
        def quart_easeout(current, start, end, duration):
            current /= duration
            current -= 1
            return -end * (current ** 4 - 1) + start

        @staticmethod
        def quart_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return end / 2 * current ** 4 + start
            current -= 2
            return -end / 2 * (current ** 4 - 2) + start

        @staticmethod
        def quint_easein(current, start, end, duration):
            current /= duration
            return end * current ** 5 + start

        @staticmethod
        def quint_easeout(current, start, end, duration):
            current /= duration
            current -= 1
            return end * (current ** 5 + 1) + start

        @staticmethod
        def quint_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return end / 2 * t ** 5 + start
            current -= 2
            return end / 2 * (current ** 5 + 2) + start

        @staticmethod
        def expo_easein(current, start, end, duration):
            return end * 2 ** (10 * (current / duration - 1)) + start

        @staticmethod
        def expo_easeout(current, start, end, duration):
            return end * (-(2 ** (-10 * current / duration)) + 1) + start

        @staticmethod
        def expo_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return end / 2 * 2 ** (10 * (current - 1)) + start
            current -= 1
            return end / 2 * (-(2 ** (-10 * current)) + 2) + start

        @staticmethod
        def circ_easein(current, start, end, duration):
            current /= duration
            return -end * (math.sqrt(1 - current ** 2) - 1) + start

        @staticmethod
        def circ_easeout(current, start, end, duration):
            current /= duration
            current -= 1
            return end * math.sqrt(1 - current ** 2) + start

        @staticmethod
        def circ_easeinout(current, start, end, duration):
            current /= duration / 2
            if current < 1:
                return -end / 2 * (math.sqrt(1 - current ** 2) - 1) + start
            current -= 2
            return end / 2 * (math.sqrt(1 - current ** 2) + 1) + start

    class Property:
        position = 'position'
        frame = 'frame'
        fill = 'fill'
        opacity = 'opacity'
        stroke = 'stroke'
        dash = 'dash'
        bd_stroke = 'bd_stroke'

        def __init__(self, name: str):
            id = name.lower()
            if id == 'position':
                self = self.position
            elif id == 'frame':
                self = self.frame
            elif id == 'fill':
                self = self.fill
            elif id == 'opacity':
                self = self.opacity
            elif id == 'stroke':
                self = self.stroke
            elif id == 'dash':
                self = self.dash
            elif id == 'bd_stroke':
                self = self.bd_stroke

    class TimingFunction:
        LINEAR = 'linear'
        QUAD = 'quad'
        CUBIC = 'cubic'
        QUART = 'quart'
        QUINT = 'quint'
        EXPO = 'expo'
        SINE = 'sine'
        CIRC = 'circ'

        def __init__(self, name: str):
            id = name.lower()
            if id == 'linear':
                self = self.LINEAR
            elif id == 'quad':
                self = self.QUAD
            elif id == 'cubic':
                self = self.CUBIC
            elif id == 'quart':
                self = self.QUART
            elif id == 'quint':
                self = self.QUINT
            elif id == 'expo':
                self = self.EXPO
            elif id == 'sine':
                self = self.SINE
            elif id == 'circ':
                self = self.CIRC
            else:
                raise Exception(f'Invalid timing function \'{name}\'.')

    class CalculationMode:
        NONE = 'n'
        EASE_IN = 'easein'
        EASE_OUT = 'easeout'
        EASE_INOUT = 'easeinout'
        # BOUNCE = 'bounce'
        # ELASTIC = 'elastic'

        def __init__(self, name: str):
            id = name.lower()
            if id == 'none':
                self = self.NONE
            elif id == 'easein':
                self = self.EASE_IN
            elif id == 'easeout':
                self = self.EASE_OUT
            elif id == 'easeinout':
                self = self.EASE_INOUT
            # elif id == 'bounce':
            #     self = self.BOUNCE
            # elif id == 'elastic':
            #     self = self.ELASTIC
            else:
                raise Exception(f'Invalid timing function \'{name}\'.')

    def __init__(self, identifier: str, object_identifier: str, property: str):
        self.identifier = identifier
        self.object_identifier = object_identifier
        self.property = self.Property(property)


class BasicAnimation(Animation):

    from_value = None
    to_value = None

    def keyframes(self, fps: int = 24):
        total_frames = fps * self.duration
        name = f'{self.timing_funtion}_{self.calculation_mode}'
        timing_funtion = getattr(self, name)
        if self.property == self.Property.position:
            if isinstance(self.from_value, tuple) and len(self.from_value) == 2:
                old, new = self.from_value, self.to_value
                frame_range = range(total_frames + 1)
                x_frames = [timing_funtion(i, old[0], new[0], total_frames) for i in frame_range]
                y_frames = [timing_funtion(i, old[1], new[1], total_frames) for i in frame_range]
                return list(zip(x_frames, y_frames))
            else:
                raise Exception('Argument(s) does not match property.')

    def __init__(self, identifier: str, object_identifier: str, property: str):
        super().__init__(identifier, object_identifier, property)


class KeyframeAnimation(Animation):

    values = []
    key_times: [float] = []

    def __init__(self, identifier: str, object_identifier: str, property: str):
        super().__init__(identifier, object_identifier, property)


class TransitionAnimation(Animation):
    pass


class Keyframe:
    __animations: [Animation] = []

    def __init__(self, time: float, value):
        self.time = time
        self.value = value


class HybridKeyframe(Keyframe):
    __keyframes: [Keyframe] = []


class Block:
    enabled = True

    class BuildOrder:
        SYNC = 'sync'
        AFTER = 'after'

        def __init__(self, name: str):
            id = name.lower()
            if id == 'sync':
                self = self.SYNC
            elif id == 'after':
                self = self.AFTER
            else:
                raise Exception(f'Invalid build order \'{name}\'.')

    def __init__(self, name: str, build_order: str, delay: float = 0.0):
        self.name = name
        self.build_order = self.BuildOrder(build_order)
        self.delay = delay


class Timeline:
    __blocks = {}

    def animations(self):
        return self.__blocks.items()

    def total_duration(self) -> float:
        durations, prev_duration = 0.0, 0.0
        for block, animations in self.__blocks.items():
            if block.build_order == Block.BuildOrder.AFTER:
                duration = block.delay
                for anim in animations:
                    duration += anim.duration
                prev_duration = duration
            elif block.build_order == Block.BuildOrder.SYNC:
                duration = 0.0
                for anim in animations:
                    duration += anim.duration
                delta = duration + block.delay - prev_duration
                prev_duration = delta if delta >= 0 else 0
            else:
                raise Exception('An error has occured.')
            durations += prev_duration
        return durations

    def add_block(self, name: str, build_order: str, delay: float = 0.0,
                  *animation):
        block = Block(name, build_order, delay=delay)
        if all([isinstance(a, Animation) for a in animation]):
            self.__blocks[block] = animation
        else:
            raise Exception(f'Invalid arguemnts(s) - Erroneous object type(s).')

    def remove_block(self, block_name: str):
        for block, animations in self.__blocks.items():
            if block.name == block_name:
                del self.__blocks[block]

    def disable_block(self, block_name: str):
        for block, animations in self.__blocks.items():
            if block.name == block_name:
                block.enabled = False

    def update_build_order(self, block_name: str, build_order: str):
        for block, animations in self.__blocks.items():
            if block.name == block_name:
                block.build_order = Block.BuildOrder(build_order)
