from typing import List
import random
from instruments import Instrument
from musicians import Musician
import time

class Band():
    """
    Create the Band with the lists musicians and instruments
    """
    def __init__(self, musicians: List[Musician], instruments: List[Instrument]) -> None:
        self.musicians = musicians
        self.instruments = instruments

    def assignInstruments(self):
        """
        Assign each instrument for each musician
        """
        randNumber = random.randint(1,10) # Random size 1-10 for sublist


        randomMusicians = random.sample(self.musicians , randNumber) # Random sublist of musicians
        for musician in randomMusicians:
            randInstrument = random.randint(0, len(self.instruments) -1)

            musician.instrument = self.instruments[randInstrument]

    def play(self, tiempo: int):
        """
        Start to play the band during x time
        """

        for musician in self.musicians:
            if musician.instrument: # Take only the musicians who have instrument
                musician.instrument.test()
        print("-----------------------------------")
        print("La banda se presentará en 5 segundos...")
        time.sleep(5)
        start = time.time()
        
        while time.time() - start < tiempo:
            for musician in self.musicians:
                if musician.instrument:
                    musician.play()
            print("-----------------------------------")
            time.sleep(5)