from dataclasses import dataclass
from tweening import Tweener


# Event classes

@dataclass
class MovementStart:
    scene: object
    colors: dict

@dataclass
class MovementDone:
    scene: object

@dataclass
class TweeningDone:
    tweener: Tweener

@dataclass
class DamageDealt:
    target: str
    dmg: int

@dataclass
class MonsterDeath:
    monster: object
