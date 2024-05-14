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
        return str(self).replace("\033", "\\033")