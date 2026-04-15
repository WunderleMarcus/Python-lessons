"""
OOP Übung: Einstieg in Klassen in Python
Thema: Auto

Ziel:
- Klassen definieren
- Objekte (Instanzen) erstellen
- Instanzattribute verwenden
- Attribute lesen und verändern
- Methoden definieren und nutzen (Bonus)
- Unterschied zwischen Instanz- und Klassenattributen verstehen (Bonus)
"""


# =========================
# AUFGABENSTELLUNG
# =========================

"""
1. Erstelle eine Klasse 'Auto'

Die Klasse soll folgende Instanzattribute besitzen:
- marke (z. B. BMW)
- farbe (z. B. schwarz)
- geschwindigkeit (Startwert: 0)

Verwende dazu die __init__-Methode.
"""


"""
2. Erstelle zwei Objekte:
- auto1: BMW, schwarz
- auto2: Audi, weiß
"""


"""
3. Lies die Attribute aus und gib sie aus:
- Marke
- Farbe
- Geschwindigkeit
"""


"""
4. Verändere Attribute direkt:
- Setze die Geschwindigkeit von auto1 auf 100
- Ändere die Farbe von auto2 auf "blau"

Gib danach die neuen Werte erneut aus.
"""


# =========================
# BONUS
# =========================

"""
Bonus 1: Methode beschleunigen
--------------------------------
Erweitere die Klasse um eine Methode:

def beschleunigen(self, wert):

Aufgabe:
- Erhöhe die Geschwindigkeit um 'wert'
- Teste die Methode mit beiden Autos
"""


"""
Bonus 2: Methode bremsen
--------------------------------
Erstelle eine Methode:

def bremsen(self, wert):

Aufgabe:
- Verringere die Geschwindigkeit um 'wert'
- Geschwindigkeit darf nicht unter 0 fallen
"""


"""
Bonus 3: Klassenattribut
--------------------------------
Füge ein Klassenattribut hinzu:

anzahl_autos = 0

Aufgabe:
- Erhöhe diesen Wert bei jeder neuen Instanz
- Gib die Gesamtanzahl der Autos aus
"""


"""
Bonus 4: Verständnisfragen
--------------------------------
1. Was passiert bei: auto1.farbe = "rot" ?
2. Was passiert bei: Auto.anzahl_autos = 10 ?
3. Warum ist geschwindigkeit ein Instanzattribut?
"""


# =========================
# HINWEIS
# =========================

"""
Du sollst hier noch KEINEN vollständigen Code schreiben,
sondern die Aufgaben Schritt für Schritt selbst lösen.
"""
