# ============================================
# AUFGABE: Warum funktioniert dieser Code nicht?
# ============================================

# 1. Führe den Code aus
# 2. Analysiere die Fehlermeldung
# 3. Finde heraus, warum der Fehler entsteht
# 4. Behebe das Problem so, dass die Ausgabe korrekt ist
#
# Ziel-Ausgabe:
#
# Admin wird erstellt
# Benutzer wird erstellt
# Admin-Info:
# Name: Alice
# Rechte: alle Rechte
#
# Hinweis:
# - Die Klasse "Benutzer" funktioniert korrekt
# - Das Problem liegt in der Klasse "Admin"


class Benutzer:
    def __init__(self, name):
        print("Benutzer wird erstellt")
        self.name = name

    def info(self):
        print(f"Name: {self.name}")


class Admin(Benutzer):
    def __init__(self, name, rechte):
        print("Admin wird erstellt")
        self.rechte = rechte

    def info(self):
        print("Admin-Info:")
        print(f"Rechte: {self.rechte}")
        print(f"Name: {self.name}")  # <- Hier tritt der Fehler auf


# Programmstart
a = Admin("Alice", "alle Rechte")
a.info()