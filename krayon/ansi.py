from typing import Any


class BaseKrayonException(Exception):
    message = ''
    def __init__(self, msg: str | Any = '') -> None:
        super().__init__(f'{self.message} {msg}')

class InvalidANSICode(BaseKrayonException):
    message = 'ANSI Code should be between 0 and 107. Code given:'

class CantAdd(BaseKrayonException):
    message = 'Only str and C can be added with C. Not'

class ANSI:
    pre = "\033["
    post = "m"
    
    @classmethod
    def make(cls, *effects: int):
        effects_ = []
        for effect in effects:
            if 0 <= effect <= 107:
                effects_.append(str(effect))
            else:
                raise InvalidANSICode(effect)
        return f"{cls.pre}{';'.join(effects_)}{cls.post}"


class Effect:
    RESET = 0
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4
    SLOW_BLINK = 5
    RAPID_BLINK = 6
    REVERSE_VIDEO = 7
    CONCEAL = 8
    CROSSED_OUT = 9
    PRIMARY_FONT = 10
    # ALTERNATIVE_FONT_1 = 11
    # ALTERNATIVE_FONT_2 = 12
    # ALTERNATIVE_FONT_3 = 13
    # ALTERNATIVE_FONT_4 = 14
    # ALTERNATIVE_FONT_5 = 15
    # ALTERNATIVE_FONT_6 = 16
    # ALTERNATIVE_FONT_7 = 17
    # ALTERNATIVE_FONT_8 = 18
    # ALTERNATIVE_FONT_9 = 19
    FRAKTUR = 20
    DOUBLY_UNDERLINED = 21
    NORMAL_INTENSITY = 22
    NEITHER_ITALIC_NOR_BLACKLETTER = 23
    NOT_UNDERLINED = 24
    NOT_BLINKING = 25
    PROPORTIONAL_SPACING = 26
    NOT_REVERSED = 27
    REVEAL = 28
    NOT_CROSSED_OUT = 29
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    # SET_COLOR = 38
    DEFAULT_COLOR = 39
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_WHITE = 47
    # SET_BG_COLOR = 48
    DEFAULT_BG_COLOR = 49
    DISABLE_PROPORTIONAL_SPACING = 50
    FRAMED = 51
    ENCIRCLED = 52
    OVERLINED = 53
    NEITHER_FRAMED_NOR_ENCIRCLED = 54
    NOT_OVERLINED = 55
    # SET_UNDERLINE_COLOR = 58
    DEFAULT_UNDERLINE_COLOR = 59
    IDEOGRAM_UNDERLINE_RIGHT = 60
    IDEOGRAM_DOUBLE_UNDERLINE_RIGHT = 61
    IDEOGRAM_OVERLINE_LEFT = 62
    IDEOGRAM_DOUBLE_OVERLINE_LEFT = 63
    IDEOGRAM_STRESS_MARKING = 64
    NO_IDEOGRAM_ATTRIBUTES = 65
    SUPERSCRIPT = 73
    SUBSCRIPT = 74
    NEITHER_SUPERSCRIPT_NOR_SUBSCRIPT = 75
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97
    BRIGHT_BG_BLACK = 100
    BRIGHT_BG_RED = 101
    BRIGHT_BG_GREEN = 102
    BRIGHT_BG_YELLOW = 103
    BRIGHT_BG_BLUE = 104
    BRIGHT_BG_MAGENTA = 105
    BRIGHT_BG_CYAN = 106
    BRIGHT_BG_WHITE = 107