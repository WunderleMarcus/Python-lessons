# Basisklasse: Mitarbeiter
class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name  # Speichert den Namen des Mitarbeiters
        self.gehalt = gehalt  # Speichert das Gehalt des Mitarbeiters
    def vorstellen(self):
        # Standard-Vorstellung eines Mitarbeiters
        return f"Hallo, ich bin {self.name} und bin Mitarbeiter."


# Kindklasse: Entwickler erbt von Mitarbeiter
class Entwickler(Mitarbeiter):
    def __init__(self, name, gehalt, programmsprache):
        # ruft den Konstruktor der Elternklasse auf
        super().__init__(name, gehalt)
        self.programmsprache = programmsprache

    # Methode wird überschrieben (Method Overriding)
    def vorstellen(self):
        # spezifische Vorstellung für Entwickler
        return f"Hallo, ich bin {self.name}, habe ein Gehalt von {self.gehalt} und programmiere in {self.programmsprache}."


# --- Beispielhafte Nutzung ---

# Objekt der Basisklasse
mitarbeiter = Mitarbeiter("Anna", 3000)
print(mitarbeiter.vorstellen())
# Ausgabe: Hallo, ich bin Anna und bin Mitarbeiter.

# Objekt der Kindklasse
entwickler = Entwickler("Max", 5000, "Python")
print(entwickler.vorstellen())
# Ausgabe: Hallo, ich bin Max, habe ein Gehalt von 5000 und programmiere in Python