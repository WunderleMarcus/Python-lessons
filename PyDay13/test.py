class Tier:
    def __init__(self, name):
        print("Tier.__init__ wird ausgeführt")
        self.name = name

    def vorstellen(self):
        print(f"Ich bin ein Tier und heiße {self.name}")


# OHNE super()
class HundOhneSuper(Tier):
    def __init__(self, name, rasse):
        print("HundOhneSuper.__init__ wird ausgeführt")
        self.rasse = rasse

    def vorstellen(self):
        print("Ich bin ein Hund")
        print(f"Rasse: {self.rasse}")
        # versucht auf self.name zuzugreifen → Problem!
        try:
            print(f"Name: {self.name}")
        except AttributeError:
            print("FEHLER: name wurde nicht gesetzt!")


# MIT super()
class HundMitSuper(Tier):
    def __init__(self, name, rasse):
        print("HundMitSuper.__init__ wird ausgeführt")
        super().__init__(name)  # ruft Eltern-Konstruktor auf
        self.rasse = rasse

    def vorstellen(self):
        print("Ich bin ein Hund")
        super().vorstellen()  # ruft Methode der Elternklasse
        print(f"Rasse: {self.rasse}")


print("=== OHNE super() ===")
hund1 = HundOhneSuper("Bello", "Labrador")
hund1.vorstellen()

print("\n=== MIT super() ===")
hund2 = HundMitSuper("Max", "Beagle")
hund2.vorstellen()


class Fahrzeug: 
  def __init__(self, anzahlTueren):
    self.anzahlTueren = anzahlTueren
 
  def fahren(self):
    return f"Das Fahrzeug fährt"
      
class LKW(Fahrzeug):
  def __init__(self, anzahlTueren, hatAnhaenger):
    super.__init__(anzahlTueren)
    self.hatAnhaenger = hatAnhaenger 
    
  def lkwFahren(self):
    print("Hallo")
    print(super().fahren())  
    print("Ich bin ein LKW")   
      
lastwagen = LKW()
lastwagen.lkwFahren() 