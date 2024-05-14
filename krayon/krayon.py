"""
This file is only used in generating the krayon.py file.
It is not meant to be run.
"""

from .ansi import ANSI, Effect, CantAdd # type: ignore

class C:
    def __init__(self, string: 'str | C' = '') -> None:
        if isinstance(string, C):
            string = string.string
        self.string: str = string
        self.length = len(string)
        self.effects: list[int] = []
    
    def __str__(self) -> str:
        self.string = self.string.replace(
            ANSI.make(Effect.RESET), 
            ANSI.make(Effect.RESET) + ANSI.make(*self.effects)
        )

        return ANSI.make(*self.effects) + self.string + ANSI.make(Effect.RESET)
    
    def __add__(self, v) -> 'str | C':
        if isinstance(v, str):
            return str(self) + v
        elif isinstance(v, C):
            newC = C(self.string + v.string)
            newC.effects = self.effects + v.effects
            return newC
        else:
            raise CantAdd(type(v))
    
    def __radd__(self, v) -> 'str | C':
        if isinstance(v, str):
            return v + str(self)
        elif isinstance(v, C):
            newC = C(v.string + self.string)
            newC.effects = v.effects + self.effects
            return newC
        else:
            raise CantAdd(type(v))
        
    def raw(self) -> str:
        """Return the string with ANSI code escaped. Useful for debugging colouring issues"""
        return str(self).replace("\033", "\\033")
    
    def add_ansi(self, ansi_code: int) -> 'C':
        self.effects.append(ansi_code)
        return self

    @property
    def reset(self) -> 'C':
        self.effects.append(Effect.RESET)
        return self
    @property
    def bold(self) -> 'C':
        self.effects.append(Effect.BOLD)
        return self
    @property
    def faint(self) -> 'C':
        self.effects.append(Effect.FAINT)
        return self
    @property
    def italic(self) -> 'C':
        self.effects.append(Effect.ITALIC)
        return self
    @property
    def underline(self) -> 'C':
        self.effects.append(Effect.UNDERLINE)
        return self
    @property
    def slow_blink(self) -> 'C':
        self.effects.append(Effect.SLOW_BLINK)
        return self
    @property
    def rapid_blink(self) -> 'C':
        self.effects.append(Effect.RAPID_BLINK)
        return self
    @property
    def reverse_video(self) -> 'C':
        self.effects.append(Effect.REVERSE_VIDEO)
        return self
    @property
    def conceal(self) -> 'C':
        self.effects.append(Effect.CONCEAL)
        return self
    @property
    def crossed_out(self) -> 'C':
        self.effects.append(Effect.CROSSED_OUT)
        return self
    @property
    def primary_font(self) -> 'C':
        self.effects.append(Effect.PRIMARY_FONT)
        return self
    @property
    def fraktur(self) -> 'C':
        self.effects.append(Effect.FRAKTUR)
        return self
    @property
    def doubly_underlined(self) -> 'C':
        self.effects.append(Effect.DOUBLY_UNDERLINED)
        return self
    @property
    def normal_intensity(self) -> 'C':
        self.effects.append(Effect.NORMAL_INTENSITY)
        return self
    @property
    def neither_italic_nor_blackletter(self) -> 'C':
        self.effects.append(Effect.NEITHER_ITALIC_NOR_BLACKLETTER)
        return self
    @property
    def not_underlined(self) -> 'C':
        self.effects.append(Effect.NOT_UNDERLINED)
        return self
    @property
    def not_blinking(self) -> 'C':
        self.effects.append(Effect.NOT_BLINKING)
        return self
    @property
    def proportional_spacing(self) -> 'C':
        self.effects.append(Effect.PROPORTIONAL_SPACING)
        return self
    @property
    def not_reversed(self) -> 'C':
        self.effects.append(Effect.NOT_REVERSED)
        return self
    @property
    def reveal(self) -> 'C':
        self.effects.append(Effect.REVEAL)
        return self
    @property
    def not_crossed_out(self) -> 'C':
        self.effects.append(Effect.NOT_CROSSED_OUT)
        return self
    @property
    def black(self) -> 'C':
        self.effects.append(Effect.BLACK)
        return self
    @property
    def red(self) -> 'C':
        self.effects.append(Effect.RED)
        return self
    @property
    def green(self) -> 'C':
        self.effects.append(Effect.GREEN)
        return self
    @property
    def yellow(self) -> 'C':
        self.effects.append(Effect.YELLOW)
        return self
    @property
    def blue(self) -> 'C':
        self.effects.append(Effect.BLUE)
        return self
    @property
    def magenta(self) -> 'C':
        self.effects.append(Effect.MAGENTA)
        return self
    @property
    def cyan(self) -> 'C':
        self.effects.append(Effect.CYAN)
        return self
    @property
    def white(self) -> 'C':
        self.effects.append(Effect.WHITE)
        return self
    @property
    def default_color(self) -> 'C':
        self.effects.append(Effect.DEFAULT_COLOR)
        return self
    @property
    def default_colour(self) -> 'C':
        self.effects.append(Effect.DEFAULT_COLOUR)
        return self
    @property
    def bg_black(self) -> 'C':
        self.effects.append(Effect.BG_BLACK)
        return self
    @property
    def bg_red(self) -> 'C':
        self.effects.append(Effect.BG_RED)
        return self
    @property
    def bg_green(self) -> 'C':
        self.effects.append(Effect.BG_GREEN)
        return self
    @property
    def bg_yellow(self) -> 'C':
        self.effects.append(Effect.BG_YELLOW)
        return self
    @property
    def bg_blue(self) -> 'C':
        self.effects.append(Effect.BG_BLUE)
        return self
    @property
    def bg_magenta(self) -> 'C':
        self.effects.append(Effect.BG_MAGENTA)
        return self
    @property
    def bg_cyan(self) -> 'C':
        self.effects.append(Effect.BG_CYAN)
        return self
    @property
    def bg_white(self) -> 'C':
        self.effects.append(Effect.BG_WHITE)
        return self
    @property
    def default_bg_color(self) -> 'C':
        self.effects.append(Effect.DEFAULT_BG_COLOR)
        return self
    @property
    def default_bg_colour(self) -> 'C':
        self.effects.append(Effect.DEFAULT_BG_COLOUR)
        return self
    @property
    def disable_proportional_spacing(self) -> 'C':
        self.effects.append(Effect.DISABLE_PROPORTIONAL_SPACING)
        return self
    @property
    def framed(self) -> 'C':
        self.effects.append(Effect.FRAMED)
        return self
    @property
    def encircled(self) -> 'C':
        self.effects.append(Effect.ENCIRCLED)
        return self
    @property
    def overlined(self) -> 'C':
        self.effects.append(Effect.OVERLINED)
        return self
    @property
    def neither_framed_nor_encircled(self) -> 'C':
        self.effects.append(Effect.NEITHER_FRAMED_NOR_ENCIRCLED)
        return self
    @property
    def not_overlined(self) -> 'C':
        self.effects.append(Effect.NOT_OVERLINED)
        return self
    @property
    def default_underline_color(self) -> 'C':
        self.effects.append(Effect.DEFAULT_UNDERLINE_COLOR)
        return self
    @property
    def default_underline_colour(self) -> 'C':
        self.effects.append(Effect.DEFAULT_UNDERLINE_COLOUR)
        return self
    @property
    def ideogram_underline_right(self) -> 'C':
        self.effects.append(Effect.IDEOGRAM_UNDERLINE_RIGHT)
        return self
    @property
    def ideogram_double_underline_right(self) -> 'C':
        self.effects.append(Effect.IDEOGRAM_DOUBLE_UNDERLINE_RIGHT)
        return self
    @property
    def ideogram_overline_left(self) -> 'C':
        self.effects.append(Effect.IDEOGRAM_OVERLINE_LEFT)
        return self
    @property
    def ideogram_double_overline_left(self) -> 'C':
        self.effects.append(Effect.IDEOGRAM_DOUBLE_OVERLINE_LEFT)
        return self
    @property
    def ideogram_stress_marking(self) -> 'C':
        self.effects.append(Effect.IDEOGRAM_STRESS_MARKING)
        return self
    @property
    def no_ideogram_attributes(self) -> 'C':
        self.effects.append(Effect.NO_IDEOGRAM_ATTRIBUTES)
        return self
    @property
    def superscript(self) -> 'C':
        self.effects.append(Effect.SUPERSCRIPT)
        return self
    @property
    def subscript(self) -> 'C':
        self.effects.append(Effect.SUBSCRIPT)
        return self
    @property
    def neither_superscript_nor_subscript(self) -> 'C':
        self.effects.append(Effect.NEITHER_SUPERSCRIPT_NOR_SUBSCRIPT)
        return self
    @property
    def bright_black(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BLACK)
        return self
    @property
    def bright_red(self) -> 'C':
        self.effects.append(Effect.BRIGHT_RED)
        return self
    @property
    def bright_green(self) -> 'C':
        self.effects.append(Effect.BRIGHT_GREEN)
        return self
    @property
    def bright_yellow(self) -> 'C':
        self.effects.append(Effect.BRIGHT_YELLOW)
        return self
    @property
    def bright_blue(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BLUE)
        return self
    @property
    def bright_magenta(self) -> 'C':
        self.effects.append(Effect.BRIGHT_MAGENTA)
        return self
    @property
    def bright_cyan(self) -> 'C':
        self.effects.append(Effect.BRIGHT_CYAN)
        return self
    @property
    def bright_white(self) -> 'C':
        self.effects.append(Effect.BRIGHT_WHITE)
        return self
    @property
    def bright_bg_black(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_BLACK)
        return self
    @property
    def bright_bg_red(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_RED)
        return self
    @property
    def bright_bg_green(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_GREEN)
        return self
    @property
    def bright_bg_yellow(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_YELLOW)
        return self
    @property
    def bright_bg_blue(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_BLUE)
        return self
    @property
    def bright_bg_magenta(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_MAGENTA)
        return self
    @property
    def bright_bg_cyan(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_CYAN)
        return self
    @property
    def bright_bg_white(self) -> 'C':
        self.effects.append(Effect.BRIGHT_BG_WHITE)
        return self
