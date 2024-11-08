import csv
from datetime import datetime 
class Proizvod:
    def __init__(self,naziv,cena,):
        self.naziv = naziv
        self.cena = cena

    def __str__(self):
        return(f"{self.naziv} \" [{self.cena}RSD]")
    
class Akcija(Proizvod):
    def __init__(self,naziv,cena,akcija):
        super().__init__(naziv,cena)
        self.akcija = cena * ((100 - akcija)/100)

    def __str__(self):
        return(f" {self.akcija} {self.naziv} [{self.cena}RSD]")
    
class Korpa:
    brojac_id = 0
    def __init__(self):
        self.korpa_id = Korpa.brojac_id
        Korpa.brojac_id += 1
        self.lista_proizvoda = []
        self.trenutna_cena = 0
    
    def DodajProzivod(self,naziv,cena):
        self.lista_proizvoda.append((naziv,cena))
        self.trenutna_cena += cena

    def IzbaciProzivod(self,naziv):
        for proizvod in self.lista_proizvoda:
            if proizvod[0] == naziv:
                self.lista_proizvoda.remove(proizvod)
                self.trenutna_cena -= proizvod[1]
                break
    def __str__(self):
        return (f"ID {self.id} [{self.ukupna_cena} RSD")
    
class Kasa:
    def __init__(self,naziv_prodavnice,lista_vaucera):
        self.naziv_prodavnice = naziv_prodavnice
        self.lista_vaucera = lista_vaucera
        self.izdati_racuni = []

    def NaplatiKorpu(self,korpa,vaucer = None):
        if vaucer:
            if vaucer not in self.lista_vaucera:
                print(f"Vaučer {vaucer} nije validan, koristi se osnovna naplata.")
                self.osnovna_naplata(korpa)
                return
            popust = 0.2
            ukupna_cena = korpa.trenutna_cena
            za_popust = sum(p.cena for p in korpa.proizvodi if not isinstance(p, Akcija))  # Samo proizvodi koji nisu na akciji

            umanjenje = za_popust * popust
            ukupna_cena -= umanjenje

            self.generisi_racun(korpa, ukupna_cena, umanjenje)
            self.vauceri.remove(vaucer)
        else:
            self.osnovna_naplata(korpa)

    def osnovna_naplata(self, korpa):
        self.generisi_racun(korpa, korpa.ukupna_cena)

    def generisi_racun(self, korpa, ukupna_cena, umanjenje=0):
        print(f"\nProdavnica: {self.naziv_prodavnice}")
        print(f"Datum i vreme: {datetime.now()}")
        for p in korpa.proizvodi:
            print(f"{p}")
        print("----------")
        if umanjenje:
            print(f"Umanjenje: {umanjenje} RSD")
        print(f"Ukupna cena: {ukupna_cena} RSD\n")
        self.izdati_racuni.append((korpa.id, ukupna_cena))  # Čuvanje računa u listi

    def __str__(self):
        return '\n'.join([f"Račun {racun[0]}: {racun[1]} RSD" for racun in self.izdati_racuni])

            