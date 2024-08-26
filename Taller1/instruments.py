from abc import ABC, abstractmethod 

class Instrument(ABC):

    @abstractmethod
    def test(self):
        pass

    @abstractmethod    
    def sound():
        pass
# The following classes are the concrete implementations of the abstract class Instrument
#1
class Guitar(Instrument):
    """
    This class represents a Guitar object.
    """

    def test(self):
        print("Testing Guitar...")

    def sound():
        print("**Guitar sound**")
#2
class Piano(Instrument):
    """
    This class represents a Piano object
    """

    def test(self):
        print("Testing Piano...")
    
    def sound():
        print("**Piano sound**")
#3
class Bass(Instrument):
    """
    This class represents a Bass object
    """

    def test(self):
        print("Testing Bass...")

    def sound():
        print("**Bass sound**")    
#4
class Drums(Instrument):
    """
    This class represents a Drums object
    """
    def test(self):
        print("Testing Drums...")
    
    def sound():
        print("**Drums sound**")
#5
class Violin(Instrument):
    """
    This class represents a Violin object
    """
    
    def test(self):
        print("Testing Violin...")

    def sound():
        print("**Violin sound**")
#6        
class Trumpet(Instrument):
    """
    This class represents a Trumpet object
    """
        
    def test(self):
        print("Testing Trumpet...")
    
    def sound():
        print("**Trumpet sound**")

#7
class Saxophone(Instrument):
    """
    This class represents a Saxophone object
    """

    def test(self):
        print("Testing Saxophone...")

    def sound():
        print("**Saxophone sound**")

#8
class Flute(Instrument):
    """
    This class represents a Flute object
    """
    
    def test(self):
        print("Testing Flute...")

    def sound():
        print("**Flute sound**")

#9
class Harmonica(Instrument):
    """
    This class represents a Harmonica object
    """
    
    def test(self):
        print("Testing Harmonica...")

    def sound():
        print("**Harmonica sound**")

#10
class Voice(Instrument):
    """
    This class represents a Voice object
    """
    
    def test(self):
        print("Do Re Mi Fa Sol La Si...")

    def sound():
        print("**Singig**")