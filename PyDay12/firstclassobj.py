class Auto:
    def __init__(self, marke, farbe):
        # __init__ ist der Konstruktor der Klasse
        # Er wird automatisch aufgerufen, wenn ein neues Objekt erstellt wird

        # Instanzattribut:
        # self.marke gehört nur zu diesem einen Auto-Objekt
        # speichert die Marke (z. B. BMW oder Audi)
        self.marke = marke

        # Instanzattribut:
        # speichert die Farbe dieses konkreten Autos
        self.farbe = farbe

        # Instanzattribut:
        # jedes Auto startet mit Geschwindigkeit 0
        # dieser Wert ist individuell pro Objekt
        self.geschwindigkeit = 0


# =========================
# OBJEKTERZEUGUNG
# =========================

# Hier wird ein neues Auto-Objekt erstellt
# Der Konstruktor __init__ wird automatisch ausgeführt:
# marke = "BMW", farbe = "schwarz"
auto1 = Auto("BMW", "schwarz")

# Zweites Auto-Objekt wird erstellt
# marke = "Audi", farbe = "weiß"
auto2 = Auto("Audi", "weiß")


# =========================
# ATTRIBUTE AUSLESEN
# =========================

# Zugriff auf Instanzattribute von auto1
# Hier werden die gespeicherten Werte des Objekts ausgegeben
print(auto1.marke, auto1.farbe, auto1.geschwindigkeit)

# Zugriff auf Instanzattribute von auto2
print(auto2.marke, auto2.farbe, auto2.geschwindigkeit)


# =========================
# ATTRIBUTE VERÄNDERN
# =========================

# Direkte Veränderung eines Instanzattributs:
# nur dieses eine Objekt (auto1) wird verändert
auto1.geschwindigkeit = 100

# Änderung der Farbe nur für auto2
# andere Autos bleiben davon unberührt
auto2.farbe = "blau"


# =========================
# NEUE AUSGABE NACH ÄNDERUNG
# =========================

# Ausgabe zeigt den neuen Zustand von auto1
# marke bleibt gleich, farbe bleibt gleich, nur Geschwindigkeit hat sich geändert
print(auto1.marke, auto1.farbe, auto1.geschwindigkeit)

# Ausgabe zeigt den neuen Zustand von auto2
# nur die Farbe wurde verändert
print(auto2.marke, auto2.farbe, auto2.geschwindigkeit)