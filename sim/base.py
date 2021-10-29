from abc import ABC, abstractmethod
from dataclasses import dataclass
from faker import Faker

Faker.seed(0)


@dataclass
class BaseSensor(ABC):
    id: str
    description: str
    readonly: bool = False
    lat: str = ""
    lng: str = ""
    place: str = ""
    state_code: str = ""

    def __post_init__(self):
        fake = Faker()
        geo = fake.location_on_land()
        self.lat = geo[0]
        self.lng = geo[1]
        self.place = geo[2]
        self.state_code = geo[3]

    @abstractmethod
    def update(self):
        pass