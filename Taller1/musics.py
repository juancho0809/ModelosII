from abc import ABC, abstractmethod
from instruments import Instrument

class Imusician(ABC):

    @abstractmethod
    def play(self):
        pass

class Musician(Imusician):
    def __init__(self,name: str, instrument: Instrument) -> None:

        self.name = name
        self.instrument = instrument

    def play(self):
        print(f"{self.name} playing the instrument ...")
        self.instrument.sound()
        