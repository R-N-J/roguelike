from enum import auto, Enum


class RenderOrder(Enum):
    CORPSE = auto()     # lowest
    ITEM = auto()
    ACTOR = auto()      # highest
