from typing import List
import random
from instruments import Instrument
from musicians import Musician
import time

class Band():
    def __init__(self, musicians: List[Musician], instruments: List[Instrument]) -> None:
        self.musicians = musicians
        self.instruments = instruments

    def assignInstruments(self):
        randNumber = random.randint(1,10)
        counter = 0
        for musician in self.musicians:
            counter += 1
            if counter > randNumber:
                break
            randInstrument = random.randint(-1, len(self.instruments) -1)
            musician.instrument = self.instruments[randInstrument]

    def play(self, tiempo: int):

        for musician in self.musicians:
            if musician.instrument:
                musician.instrument.test()
        print("-----------------------------------")
        print("La banda se presentará en 5 segundos...")
        time.sleep(5)
        inicio = time.time()
        
        while time.time() - inicio < tiempo:
            for musician in self.musicians:
                if musician.instrument:
                    musician.play()
            print("-----------------------------------")
            time.sleep(5)