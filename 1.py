import pandas as pd
import random

class Fudbaler:
    def __init__(self, ime, pozicija, broj_utakmica):
        self.ime = ime
        self.pozicija = pozicija
        self.broj_utakmica = broj_utakmica

    def __str__(self):
        return(f"{self.ime} \" {self.pozicija} \" [{self.broj_utakmica}]")
    
    def add_game_number(self):
        self.broj_utakmica=+1

class Golman(Fudbaler):
    def __init__(self,ime,broj_utakmica):
        super().__init__(ime,"golman", broj_utakmica)
        self.broj_primljnih_golova = 0

    def dodaj_broj_primljenih_golova(self, broj_golova):
        self.broj_primljnih_golova += broj_golova


    def __str__(self):
        return(f"{self.ime} \"{self.pozicija} \"[{self.broj_utakmica}] [{self.broj_primljnih_golova}]")
    
class Igrac(Fudbaler):
    def __init__(self,ime,pozicija,broj_utakmica):
        if pozicija.lower() == "golman":
            raise ValueError("Igrac ne moze biti na poziciji 'golman'")
        super().__init__(ime,pozicija,broj_utakmica)
        self.broj_postignutih_golova = 0

    def dodaj_broj_postignutih_golova(self, broj_golova):
        self.broj_postignutih_golova+= broj_golova

    def __str__(self):
        return(f"{self.ime} \" {self.pozicija} \" [{self.broj_utakmica}] [{self.broj_postignutih_golova}] ")

class Reprezentacija:
    def __init__(self,naziv,golman,igraci):

        self.naziv = naziv
        self.golman = golman
        self.igraci = igraci
        self.broj_poena = 0
        self.broj_utakmica = 0

    def dodaj_broj_poena(self, broj_poena):
        self.broj_poena += broj_poena

    def dodaj_broj_utakmica(self, broj_utakmica):
        self.broj_utakmica +=broj_utakmica

    def daj_golmana(self):
        return random.choices(self.golman)[0]
    
    def daj_igrace(self):
        return random.sample(self.igraci, 10)
    
    def __str__(self):
        return(f"TIM {self.naziv} [{self.broj_poena}]")
    
    def prikazi_tim(self):
        for golman in self.golman:
            print(golman)
        for igrac in self.igraci:
            print(igrac)


def ucitaj_fudbalere_iz_csv(datoteka):
    reprezentacija_klase = []
    
    df = pd.read_csv(datoteka)
    reprezentacije = set(df['Reprezentacija'])

    for rep in reprezentacije:
        golmani_klase = []
        igraci_klase = []
        
        reprezentacija = df.loc[df['Reprezentacija'] == rep]
        golmani = reprezentacija.loc[reprezentacija['Pozicija'] == 'GK']
        igraci = reprezentacija.loc[reprezentacija['Pozicija'] !='GK']


        for index, row in golmani.iterrows():
            instanca_golman = Golman(ime=row['Ime'], broj_utakmica= row['BrojUtakmica'])
            golmani_klase.append(instanca_golman)

        for index, row in igraci.iterrows():
            instanca_igrac = Igrac(ime=row['Ime'], broj_utakmica= row['BrojUtakmica'], pozicija=row['Pozicija'])
            igraci_klase.append(instanca_igrac)

        reprezentacija_instanca = Reprezentacija(naziv=rep, golman=golmani_klase, igraci=igraci_klase)
        reprezentacija_klase.append(reprezentacija_instanca)
        print(reprezentacija_klase)

    return reprezentacija_klase


class Prvenstvo:
    def __init__(self,naziv):
        self.naziv = naziv
        self.reprezentacije = ucitaj_fudbalere_iz_csv('Fudbaleri.csv')

    def print_svega(self):
        
        for rep in self.reprezentacije:
            rep.prikazi_tim()



    def odigraj_utakmicu(self, reprezentacija1, reprezentacija2):
        golovi1 = random.randint(0,5)
        golovi2 = random.randint(0,5)
        strelci1 = random.choices(reprezentacija1.daj_igrace(), k = golovi1)
        strelci2 = random.choices(reprezentacija2.daj_igrace(), k = golovi2)

        print(f"{reprezentacija1.naziv} vs {reprezentacija2.naziv}")
        print(f"Rezultat: {golovi1} : {golovi2}")

        print("Postignuti golovi: ")
        for igrac in strelci1:
            igrac.dodaj_broj_postignutih_golova(1)
            print(f"{igrac.ime} je postigao gol za {reprezentacija1.naziv}")

        for igrac in strelci2:
            igrac.dodaj_broj_postignutih_golova(1)
            print(f"{igrac.ime} je postigao gol za {reprezentacija2.naziv}")

        reprezentacija1.broj_utakmica += 1
        reprezentacija2.broj_utakmica += 1 
        golman1 = reprezentacija1.daj_golmana()
        golman2 = reprezentacija2.daj_golmana()
        golman1.dodaj_broj_primljenih_golova(golovi2) 
        golman2.dodaj_broj_primljenih_golova(golovi1)

        if golovi1 > golovi2:
            reprezentacija1.broj_poena += 3
        elif golovi1 < golovi2:
            reprezentacija2.broj_poena += 3
        else:
            reprezentacija1.broj_poena += 1
            reprezentacija2.broj_poena += 1
    def odigraj_takmicenje(self):
        for i in range(len(self.reprezentacije)):
            for j in range(i + 1,len(self.reprezentacije)):
                self.odigraj_utakmicu(self.reprezentacije[i], self.reprezentacije[j])
    def prikazi_reprezentacije(self):
        for reprezentacija in self.reprezentacije:
            print(reprezentacija)


def main():
    prvenstvo = Prvenstvo("Svetsko prvenstvo")
    prvenstvo.odigraj_takmicenje()
    

if __name__ == "__main__":
    main()

