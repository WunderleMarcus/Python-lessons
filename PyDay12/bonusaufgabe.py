class Auto:
    # Klassenattribut:
    # Wird von allen Instanzen gemeinsam genutzt
    # Hier zählt es, wie viele Autos insgesamt erstellt wurden
    anzahl_autos = 0

    def __init__(self, marke, farbe):
        # Instanzattribute:
        # Diese gehören nur zu genau diesem Objekt (Auto)
        self.marke = marke  # speichert die Marke des Autos (z. B. BMW)
        self.farbe = farbe  # speichert die Farbe des Autos (z. B. schwarz)

        # Startwert für jedes Auto individuell
        # Jedes neue Auto beginnt mit Geschwindigkeit 0
        self.geschwindigkeit = 0

        # Erhöht das Klassenattribut bei jeder neuen Instanz
        # Bedeutet: jedes Mal wenn ein Auto erstellt wird, zählt der Zähler hoch
        Auto.anzahl_autos += 1

    def beschleunigen(self, wert):
        # Methode verändert den Zustand des Objekts
        # "wert" ist der Betrag, um den die Geschwindigkeit erhöht wird
        self.geschwindigkeit += wert

        # Erklärung:
        # self.geschwindigkeit ist ein Instanzattribut
        # Jede Änderung betrifft nur dieses eine Auto

    def bremsen(self, wert):
        # Methode reduziert die Geschwindigkeit
        self.geschwindigkeit -= wert

        # Schutzlogik:
        # Geschwindigkeit darf nicht negativ werden
        if self.geschwindigkeit < 0:
            self.geschwindigkeit = 0


# =========================
# OBJEKTERZEUGUNG
# =========================

# Hier wird ein Objekt der Klasse Auto erstellt
# __init__ wird automatisch aufgerufen
auto1 = Auto("BMW", "schwarz")

# Zweites Objekt wird erstellt
auto2 = Auto("Audi", "weiß")

# =========================
# METHODENAUFRUFE
# =========================

# Auto 1 wird beschleunigt um 40 km/h
auto1.beschleunigen(40)

# Auto 2 wird beschleunigt um 60 km/h
auto2.beschleunigen(60)

# Auto 1 wird um 15 km/h gebremst
auto1.bremsen(15)

# Auto 2 wird stark gebremst (80 km/h)
auto2.bremsen(80)

# =========================
# AUSGABEN DER ZUSTÄNDE
# =========================

# Ausgabe der Grunddaten von Auto 1
print("Auto 1:", auto1.marke, auto1.farbe)

# Ausgabe der aktuellen Geschwindigkeit von Auto 1
# Diese wurde durch Methoden verändert
print("Geschwindigkeit Auto 1:", auto1.geschwindigkeit)

# Ausgabe der Grunddaten von Auto 2
print("Auto 2:", auto2.marke, auto2.farbe)

# Ausgabe der aktuellen Geschwindigkeit von Auto 2
print("Geschwindigkeit Auto 2:", auto2.geschwindigkeit)

# Ausgabe des Klassenattributs
# Zeigt, wie viele Autos insgesamt erstellt wurden
print("Anzahl Autos:", Auto.anzahl_autos)

# =========================
# ZUSÄTZLICHER TEST
# =========================

print("\nTest:")

# Auto 1 wird erneut beschleunigt
# Zeigt, dass Methoden mehrfach aufgerufen werden können
auto1.beschleunigen(20)

# Ausgabe der neuen Geschwindigkeit von Auto 1
print("Neue Geschwindigkeit Auto 1:", auto1.geschwindigkeit)

# Auto 2 wird erneut gebremst
auto2.bremsen(30)

# Ausgabe der neuen Geschwindigkeit von Auto 2
print("Neue Geschwindigkeit Auto 2:", auto2.geschwindigkeit)