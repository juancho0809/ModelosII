from abc import ABC, abstractmethod
from instruments import Instrument

class MusicianBase(ABC):

    @abstractmethod
    def play(self):
        pass

class Musician(MusicianBase):
    def __init__(self,name: str) -> None:

        self.name = name
        self.instrument = None

    def play(self):
        print(f"{self.name} playing the instrument ...")
        self.instrument.sound()
        