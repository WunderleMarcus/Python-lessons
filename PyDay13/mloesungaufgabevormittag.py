# ============================================
# MUSTERLÖSUNG: Verwendung von super()
# ============================================

# Erklärung:
# Das Problem war, dass die Elternklasse (Benutzer)
# nicht initialisiert wurde.
#
# Dadurch wurde "self.name" nie gesetzt.
#
# Lösung:
# Mit super().__init__(...) wird der Konstruktor
# der Elternklasse korrekt aufgerufen.


class Benutzer:
    def __init__(self, name):
        print("Benutzer wird erstellt")
        self.name = name  # Attribut wird hier gesetzt

    def info(self):
        print(f"Name: {self.name}")


class Admin(Benutzer):
    def __init__(self, name, rechte):
        print("Admin wird erstellt")

        # ✅ WICHTIG:
        # Aufruf des Konstruktors der Elternklasse
        # Dadurch wird self.name korrekt gesetzt
        super().__init__(name)

        # Eigenes Attribut der Klasse Admin
        self.rechte = rechte

    def info(self):
        print("Admin-Info:")

        # ✅ Optional, aber sauber:
        # Nutzung der bestehenden Methode der Elternklasse
        super().info()

        # Zusätzliche Ausgabe der Admin-spezifischen Daten
        print(f"Rechte: {self.rechte}")


# Programmstart
a = Admin("Alice", "alle Rechte")
a.info()


# ============================================
# WICHTIGE ERKENNTNIS
# ============================================

# Ohne super():
# - Elternklasse wird NICHT ausgeführt
# - wichtige Attribute fehlen
# - Fehler entstehen

# Mit super():
# - Elternklasse wird korrekt eingebunden
# - bestehender Code wird wiederverwendet
# - Verhalten wird erweitert statt ersetzt