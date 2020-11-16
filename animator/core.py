class Point:
    def __str__(self):
        return f'Point: ({self.x}, {self.y})'

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Rect:
    def __str__(self):
        return f'Frame: {self.width}x{self.height} at ({self.origin.x}, {self.origin.y})'

    def __init__(self, width: int, height: int, origin: Point):
        self.origin = origin
        self.width = width
        self.height = height


class Color:

    def __str__(self):
        hex_digits = ('{:02X}' * 3).format(self.r, self.g, self.b)
        return f'\'#{hex_digits.lower()}\''

    def __init__(self, **kwargs):
        rgb_scale, cmyk_scale = range(0, 256), range(0, 101)
        try:
            r, g, b = kwargs['r'], kwargs['g'], kwargs['b']
            assert r in rgb_scale and g in rgb_scale and b in rgb_scale
        except KeyError:
            try:
                c, m, y, k = kwargs['c'], kwargs['m'], kwargs['y'], kwargs['k']
                assert c in cmyk_scale and m in cmyk_scale and y in cmyk_scale and k in cmyk_scale
            except KeyError:
                raise Exception('Color: Invalid arguments.')
            except AssertionError:
                raise Exception('Color: Invalid scale.')
            else:
                rgb_scale, cmyk_scale = 255, 100
                r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
                g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
                b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
                self.r, self.g, self.b = r, g, b
        except AssertionError:
            raise Exception('Color: Invalid scale.')
        else:
            self.r, self.g, self.b = r, g, b
