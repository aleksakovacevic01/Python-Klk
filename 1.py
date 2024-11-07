import csv
import random

class Avion:
    serijski_broj_counter = 20241001 

    def __init__(self, tezina):
        self.serijski_broj = Avion.serijski_broj_counter
        Avion.serijski_broj_counter += 1
        self.tezina = tezina

    def __str__(self):
        return f"{self.vrsta}{self.serijski_broj}[{self.tezina} kg]"

class PutnickiAvion(Avion):
    def __init__(self, tezina, kapacitet=100):
        super().__init__(tezina)
        self.vrsta = "P"
        self.kapacitet = kapacitet
        self.broj_putnika = random.randint(0, kapacitet)
        self.tezina_putnika = 80
        self.tezina_prtljaga = 30

    def ukupna_tezina(self):
        ukupna_tezina_putnika = self.broj_putnika * (self.tezina_putnika + self.tezina_prtljaga)
        return self.tezina + ukupna_tezina_putnika

class TeretniAvion(Avion):
    def __init__(self, tezina, kapacitet, procenat_popunjenosti=None):
        super().__init__(tezina)
        self.vrsta = "T"
        self.kapacitet = kapacitet
        self.procenat_popunjenosti = procenat_popunjenosti or random.randint(10, 90)

    def ukupna_tezina(self):
        return self.tezina + (self.kapacitet * (self.procenat_popunjenosti / 100))


class Aerodrom:
    def __init__(self, naziv, broj_mesta, max_tezina, aerodromska_taxa):
        self.naziv = naziv
        self.mesta = [None] * broj_mesta
        self.max_tezina = max_tezina
        self.aerodromska_taxa = aerodromska_taxa
        self.prihod = 0

    def sleti(self, avion, mesto):
        if mesto < 0 or mesto >= len(self.mesta):
            return "Neuspešno: Neispravan broj mesta."
        if self.mesta[mesto] is not None:
            return "Neuspešno: Mesto je već zauzeto."
        if avion.ukupna_tezina() > self.max_tezina:
            return "Neuspešno: Avion prelazi maksimalnu dozvoljenu težinu."
        self.mesta[mesto] = avion
        naplacena_taksa = avion.ukupna_tezina() * self.aerodromska_taxa
        self.prihod += naplacena_taksa
        return f"Uspešno sletanje. Naplaćena taksa: {naplacena_taksa:.2f} evra."

    def poleti(self, mesto):
        if mesto < 0 or mesto >= len(self.mesta) or self.mesta[mesto] is None:
            return "Neuspešno: Mesto je prazno ili neispravno."
        self.mesta[mesto] = None
        return "Avion je uspešno poleteo."

    def trenutni_prihod(self):
        return self.prihod

    def __str__(self):
        opis_mesta = []
        for mesto in self.mesta:
            if mesto is None:
                opis_mesta.append("<<prazno>>")
            else:
                opis_mesta.append(str(mesto))
        return "\n".join(opis_mesta)

def ucitaj_avione(putanja):
    avioni = []
    with open(putanja, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tip = row['Tip']
            tezina = int(row['Tezina'])
            kapacitet = int(row['Kapacitet'])
            if tip == 'putnicki':
                avioni.append(PutnickiAvion(tezina, kapacitet))
            elif tip == 'teretni':
                avioni.append(TeretniAvion(tezina, kapacitet))
    return avioni


def main():
    aerodrom1 = Aerodrom("Nikola Tesla", 10, 25000, 1)
    aerodrom2 = Aerodrom("Konstantin Veliki", 6, 10000, 0.7)


    avioni = ucitaj_avione('Avioni.csv')


    for i in range(7):
        mesto = random.randint(0, 9)
        if i < len(avioni):
            print(aerodrom1.sleti(avioni[i], mesto))

    for i in range(4):
        mesto = random.randint(0, 5)
        if i < len(avioni):
            print(aerodrom2.sleti(avioni[i], mesto))


    print(aerodrom1.poleti(0))
    print(aerodrom2.poleti(0))


    print("\nAerodrom Nikola Tesla:")
    print(f"Trenutni prihod: {aerodrom1.trenutni_prihod():.2f} evra")
    print(aerodrom1)

    print("\nAerodrom Konstantin Veliki:")
    print(f"Trenutni prihod: {aerodrom2.trenutni_prihod():.2f} evra")
    print(aerodrom2)


if __name__ == "__main__":
    main()

        