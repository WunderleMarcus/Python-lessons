# 🔹 1. Liste von 1 bis 10 erstellen
# range(1, 11) erzeugt Zahlen von 1 bis 10 (11 ist exklusiv)
zahlen = list(range(1, 11))

# Ausgabe zur Kontrolle
print("1. Zahlenliste:", zahlen)


# 🔹 2. Liste mit Quadraten erstellen
# Wir gehen jede Zahl durch und berechnen das Quadrat
quadrate = []

for zahl in zahlen:
    quadrat = zahl ** 2   # Zahl hoch 2
    quadrate.append(quadrat)  # Ergebnis zur Liste hinzufügen

print("2. Quadrate:", quadrate)


# 🔹 3. Tuple aus den ersten drei Zahlen erstellen
# [:3] nimmt die ersten drei Elemente der Liste
erste_drei_tuple = tuple(zahlen[:3])

print("3. Tuple (erste drei Zahlen):", erste_drei_tuple)


# 🔹 4. Sets für gerade und ungerade Zahlen erstellen
gerade = set()
ungerade = set()

for zahl in zahlen:
    if zahl % 2 == 0:  # Wenn ohne Rest durch 2 teilbar → gerade
        gerade.add(zahl)
    else:              # Sonst ungerade
        ungerade.add(zahl)

print("4. Gerade Zahlen:", gerade)
print("4. Ungerade Zahlen:", ungerade)


# 🔹 5. Liste mit Zahlen, die durch 3 teilbar sind
# Wir prüfen jede Zahl mit Modulo 3
durch_drei = []

for zahl in zahlen:
    if zahl % 3 == 0:
        durch_drei.append(zahl)

print("5. Durch 3 teilbar:", durch_drei)


# 🔹 6. Dictionary: Zahl → "gerade"/"ungerade"
# Wir ordnen jeder Zahl eine Kategorie zu
kategorien = {}

for zahl in zahlen:
    if zahl % 2 == 0:
        kategorien[zahl] = "gerade"
    else:
        kategorien[zahl] = "ungerade"

print("6. Kategorien-Dictionary:", kategorien)


# 🔹 7. Schnittmenge und Vereinigung berechnen
# Schnittmenge = gemeinsame Elemente
schnittmenge = gerade.intersection(ungerade)

# Vereinigung = alle Elemente aus beiden Sets
vereinigung = gerade.union(ungerade)

print("7. Schnittmenge:", schnittmenge)
print("7. Vereinigung:", vereinigung)


# 🔹 Zusatz: Gesamtausgabe übersichtlich
print("\n--- Zusammenfassung ---")
print("Zahlen:", zahlen)
print("Quadrate:", quadrate)
print("Tuple:", erste_drei_tuple)
print("Gerade:", gerade)
print("Ungerade:", ungerade)
print("Durch 3 teilbar:", durch_drei)
print("Kategorien:", kategorien)
print("Schnittmenge:", schnittmenge)
print("Vereinigung:", vereinigung)

"""Das könnte ein Musterausgabe am Terminal sein, wenn man die
Ausgaben nacheinander ausführt. Es zeigt die Ergebnisse der 
einzelnen Schritte"""
"""
--- Zusammenfassung ---
Zahlen: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Quadrate: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Tuple: (1, 2, 3)
Gerade: {2, 4, 6, 8, 10}
Ungerade: {1, 3, 5, 7, 9}
Durch 3 teilbar: [3, 6, 9]
Kategorien: {1: 'ungerade', 2: 'gerade', 3: 'ungerade', 4: 'gerade', 5: 'ungerade', 6: 'gerade', 7: 'ungerade', 8: 'gerade', 9: 'ungerade', 10: 'gerade'}
Schnittmenge: set()
Vereinigung: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
"""