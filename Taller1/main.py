from band import Band
from musicians import Musician
from instruments import Violin, Guitar, Flute, Piano, Bass, Drums, Trumpet, Saxophone, Harmonica, Voice

if __name__ == '__main__':
    musicos = []
    musicos.append(Musician("Carlos"))
    musicos.append(Musician("Maria"))
    musicos.append(Musician("Luis"))
    musicos.append(Musician("Ana"))
    musicos.append(Musician("Pedro"))
    musicos.append(Musician("Sofia"))
    musicos.append(Musician("Javier"))
    musicos.append(Musician("Isabella"))
    musicos.append(Musician("Miguel"))
    musicos.append(Musician("Valeria"))

    instrumentos = []
    instrumentos.append(Violin())
    instrumentos.append(Guitar())
    instrumentos.append(Flute())
    instrumentos.append(Piano())
    instrumentos.append(Bass())
    instrumentos.append(Drums())
    instrumentos.append(Trumpet())
    instrumentos.append(Saxophone())
    instrumentos.append(Harmonica())
    instrumentos.append(Voice())



    banda = Band(musicos, instrumentos)
    banda.assignInstruments()
    banda.play(30)
