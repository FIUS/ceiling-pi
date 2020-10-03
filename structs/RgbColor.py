from collections import namedtuple
from neopixel import Color
import colorsys

RGB = namedtuple("RGB", ["red", "green", "blue"])
HSV = namedtuple("RGB", ["hue", "saturation", "value"])


class RgbColor(RGB):
    """Named tuple for storing a rgb color with component values in range [0, 255]"""

    @staticmethod
    def from_color(color: Color):
        return RgbColor(RgbColor.clamp_byte(color.red), RgbColor.clamp_byte(color.green), RgbColor.clamp_byte(color.blue))

    @staticmethod
    def from_int(i: int):
        blue = i & 255
        green = (i >> 8) & 255
        red = (i >> 16) & 255
        return RgbColor(red, green, blue)

    @staticmethod
    def from_hsv(h, s, v):
        """h,s,v in range [0,1]"""
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return RgbColor(rgb[0]*255, rgb[1]*255, rgb[2]*255)

    @staticmethod
    def from_HsvColor(hsv: HSV):
        return RgbColor.from_hsv(hsv.hue, hsv.saturation, hsv.value)

    def __add__(self, other):
        """Add two RgbColors componentwise"""
        if isinstance(other, RgbColor):
            return RgbColor(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        """Subtract two RgbColors componentwise"""
        if isinstance(other, RgbColor):
            return RgbColor(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other):
        """Multiply two RgbColors componentwise or multiply each component of a RgbColor with a scalar"""
        if isinstance(other, RgbColor):
            return RgbColor(self.red * other.red, self.green * other.green, self.blue * other.blue)
        elif isinstance(other, int) or isinstance(other, float):
            return RgbColor(self.red * other, self.green * other, self.blue * other)

    def __truediv__(self, other):
        """Divide two RgbColors componentwise"""
        if isinstance(other, RgbColor):
            return RgbColor(self.red / other.red, self.green / other.green, self.blue / other.blue)

    @staticmethod
    def clamp_byte(val):
        return max(0, min(255, val))

    @staticmethod
    def lerp(start: RgbColor, target: RgbColor, t: float):
        """Linear interpolation between two RgbColors
        t in range [0, 1] is the transition coefficient """
        # This calculation is a bit unintuitive but guarantees return = target for t = 1. Floating point errors can occur in other implementations
        return (1 - t) * start + t * target

    @staticmethod
    def qerp(start: RgbColor, target: RgbColor, t: float):
        """Quadratic interpolation between two RgbColors
        t in range [0, 1] is the transition coefficient """
        return (1 - t**2) * start + t**2 * target


class HsvColor(HSV):
    """Named tuple for storing a hsv color with component values in range [0, 1]"""
    
    def __new__(cls, hue: float, saturation: float, value: float):
        h_clamped = max(0, min(1, hue))
        s_clamped = max(0, min(1, saturation))
        v_clamped = max(0, min(1, value))
        return super(HSV, cls).__new__(cls, [h_clamped, s_clamped, v_clamped])

    @staticmethod
    def from_rgb(r: int, g: int, b: int):
        hsv = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        return HsvColor(hsv[0], hsv[1], hsv[2])

    @staticmethod
    def from_RgbColor(rgb: RGB):
        return HsvColor.from_rgb(rgb.red, rgb.green, rgb.blue)

    def __add__(self, other):
        """Add two HsvColors componentwise"""
        if isinstance(other, HsvColor):
            return HsvColor(self.hue + other.hue, self.saturation + other.saturation, self.value + other.value)

    def __sub__(self, other):
        """Subtract two HsvColors componentwise"""
        if isinstance(other, HsvColor):
            return HsvColor(self.hue - other.hue, self.saturation - other.saturation, self.value - other.value)

    def __mul__(self, other):
        """Multiply two HsvColors componentwise or multiply each component of a RgbColor with a scalar"""
        if isinstance(other, HsvColor):
            return HsvColor(self.hue * other.hue, self.saturation * other.saturation, self.value * other.value)
        elif isinstance(other, int) or isinstance(other, float):
            return HsvColor(self.hue * other, self.saturation * other, self.value * other)

    def __truediv__(self, other):
        """Divide two HsvColors componentwise"""
        if isinstance(other, HsvColor):
            return HsvColor(self.hue / other.hue, self.saturation / other.saturation, self.value / other.value)

    @staticmethod
    def lerp(start: HsvColor, target: HsvColor, t: float):
        """Linear interpolation between two HsvColors
        t in range [0, 1] is the transition coefficient """
        # This calculation is a bit unintuitive but guarantees return = target for t = 1. Floating point errors can occur in other implementations
        return (1 - t) * start + t * target

    @staticmethod
    def qerp(start: HsvColor, target: HsvColor, t: float):
        """Quadratic interpolation between two HsvColors
        t in range [0, 1] is the transition coefficient """
        return (1 - t**2) * start + t**2 * target