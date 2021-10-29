from random import randint, random
from dataclasses import dataclass

from sim.base import BaseSensor


@dataclass
class Sensor(BaseSensor):
    value: float = 0

    def __post_init__(self):
        super().__post_init__()
        self.readonly = True
        self.value = randint(0, 50)

    def update(self):
        sign = -1 if random() < 0.5 else 1
        self.value += sign * (2 + (self.value * 0.1)) * random()
        return self.value
