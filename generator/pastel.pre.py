from ansi import ANSI, Effect, CantAdd

class C:
    def __init__(self, string: str = '') -> None:
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
    
    def __radd__(self, v) -> 'str | C': return self.__add__(v)
    