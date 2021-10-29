from dataclasses import dataclass

from sim.base import BaseSensor


@dataclass
class ToggleSensor(BaseSensor):

    value: bool = False

    def toggle(self):
        self.value = not self.value

    def update(self):
        "nothing to do"
        pass
