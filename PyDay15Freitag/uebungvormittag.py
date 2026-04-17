class Buch:
    titel = ""
    ausgeliehen = False

    def ausleihen(self):
        if self.ausgeliehen == False:
            self.ausgeliehen = True
            print(self.titel + " wurde ausgeliehen")
        else:
            print(self.titel + " ist schon ausgeliehen")


class Bibliothek:
    def __init__(self):
        self.buecher = []
    

    def buch_hinzufuegen(self, buch):
        self.buecher.append(buch)

    def zeige_buecher(self):
        for buch in self.buecher:
            print(buch.titel)


# Nutzung
buch1 = Buch()
buch1.titel = "Python Basics"

buch2 = Buch()
buch2.titel = "OOP verstehen"

buch3 = Buch()
buch3.titel = "Fehler finden"

bib = Bibliothek()
bib2 = Bibliothek()

bib.buch_hinzufuegen(buch1)
bib.buch_hinzufuegen(buch2)
bib2.buch_hinzufuegen(buch3)

bib.zeige_buecher()
bib2.zeige_buecher()

buch1.ausleihen()
buch1.ausleihen()