from .ansi import ANSI, Effect, CantAdd

class C:
    def __init__(self, string: 'str | C' = '') -> None:
        if isinstance(string, C):
            string = string.string
        self.string = string
        self.length = len(string)
        self.effects: list[int] = []
    
    def __str__(self) -> str:
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