# Basisklasse Mitarbeiter
class Mitarbeiter:
    # Konstruktor der Klasse Mitarbeiter
    def __init__(self, name, gehalt):
        # Zuweisung der übergebenen Werte zu den Objektattributen
        self.name = name
        self.gehalt = gehalt

    # Methode vorstellen()
    def vorstellen(self):
        # Ausgabe eines einfachen Vorstellungstextes
        print("Hallo, ich bin ein Mitarbeiter")


# Kindklasse Entwickler, erbt von Mitarbeiter
class Entwickler(Mitarbeiter):
    # Konstruktor der Klasse Entwickler
    def __init__(self, name, gehalt, programmsprache):
        # WICHTIG: Kein super().__init__()
        # Stattdessen direkter Aufruf des Konstruktors der Basisklasse
        Mitarbeiter.__init__(self, name, gehalt)

        # Zusätzliches Attribut für Entwickler
        self.programmsprache = programmsprache

    # Überschreiben der Methode vorstellen()
    def vorstellen(self):
        # Erweiterte Ausgabe für Entwickler
        print(f"Hallo, ich bin ein Entwickler und programmiere in {self.programmsprache}")


# =========================
# Instanzen erstellen
# =========================

# Instanz der Klasse Mitarbeiter
mitarbeiter1 = Mitarbeiter("Max Mustermann", 3000)

# Instanz der Klasse Entwickler
entwickler1 = Entwickler("Anna Schmidt", 5000, "Python")


# =========================
# Methoden aufrufen
# =========================

# Vorstellung des Mitarbeiters
mitarbeiter1.vorstellen()

# Vorstellung des Entwicklers
entwickler1.vorstellen()


# =========================
# Attribute ausgeben
# =========================

print("\n--- Details ---")

# Zugriff auf Attribute des Mitarbeiters
print(f"Mitarbeiter: {mitarbeiter1.name}, Gehalt: {mitarbeiter1.gehalt}")

# Zugriff auf Attribute des Entwicklers
print(f"Entwickler: {entwickler1.name}, Gehalt: {entwickler1.gehalt}, Sprache: {entwickler1.programmsprache}")