# solutions_detailed.py
# Ausführliche Lösungen + Erklärungen: List, Tuple, Set, Dict

# -------------------------------
# Aufgabe 1: List
# -------------------------------
# Eine Liste ist:
# - geordnet (Reihenfolge bleibt erhalten)
# - veränderbar (mutable)
# - erlaubt Duplikate

films = ["Matrix", "Inception", "Interstellar", "Avatar", "Titanic"]

# Zugriff über Index (0 = erstes Element)
print("Erstes Element:", films[0])

# Element hinzufügen
films.append("Gladiator")

# Element ändern (Index 2 = drittes Element)
films[2] = "Der Pate"

print("Liste nach Änderungen:", films)


# -------------------------------
# Aufgabe 2: Tuple
# -------------------------------
# Ein Tuple ist:
# - geordnet
# - NICHT veränderbar (immutable)
# - schneller als Listen (kleiner Vorteil)
# - ideal für feste Daten (z.B. Koordinaten)

coordinates = (48.1, 11.6)

# Zugriff
print("Breitengrad:", coordinates[0])
print("Längengrad:", coordinates[1])

# Tuple-Unpacking
x, y = coordinates
print("Unpacked:", x, y)


# -------------------------------
# Aufgabe 3: Set
# -------------------------------
# Ein Set ist:
# - ungeordnet
# - enthält KEINE Duplikate
# - sehr schnell bei "ist enthalten?"-Prüfungen

numbers = {1, 2, 2, 3, 4, 4}

# Duplikate werden automatisch entfernt
print("Set ohne Duplikate:", numbers)

# Element hinzufügen
numbers.add(5)

# Membership-Test
print("Ist 3 enthalten?", 3 in numbers)


# -------------------------------
# Aufgabe 4: Dictionary
# -------------------------------
# Ein Dictionary ist:
# - Schlüssel-Wert-Struktur (key-value)
# - geordnet (seit Python 3.7)
# - Schlüssel müssen eindeutig sein

person = {
    "name": "Max",
    "alter": 25,
    "stadt": "München"
}

# Zugriff über Schlüssel
print("Name:", person["name"])

# Wert ändern
person["alter"] = 26

# Neues Feld hinzufügen
person["job"] = "Entwickler"

print("Person:", person)


# -------------------------------
# Aufgabe 5: List + Schleife
# -------------------------------
# Kombination aus Liste + Schleife

zahlen = [1, 2, 3, 4, 5]

summe = 0
for zahl in zahlen:
    print("Zahl:", zahl)
    summe += zahl

print("Summe:", summe)

# Alternativ (Pythonic Way)
print("Summe mit sum():", sum(zahlen))


# -------------------------------
# Aufgabe 6: Set vs List
# -------------------------------
# Ziel: Duplikate entfernen

zahlen = [1, 2, 2, 3, 4, 4, 5]

# Schritt 1: in Set umwandeln (Duplikate weg)
unique = set(zahlen)

# Schritt 2: zurück in Liste
unique_list = list(unique)

print("Ohne Duplikate:", unique_list)


# -------------------------------
# Aufgabe 7: Dictionary + Schleife
# -------------------------------

noten = {
    "Mathe": 2,
    "Deutsch": 3,
    "Informatik": 1
}

summe = 0

# Iteration über key-value
for fach, note in noten.items():
    print(f"{fach}: {note}")
    summe += note

# Durchschnitt berechnen
durchschnitt = summe / len(noten)
print("Durchschnitt:", durchschnitt)


# -------------------------------
# Aufgabe 8: Mini-Kontaktliste
# -------------------------------
# Verschachteltes Dictionary

kontakte = {
    "Max": {"alter": 25, "stadt": "München"},
    "Anna": {"alter": 30, "stadt": "Berlin"}
}

# Alle Namen
print("Namen:")
for name in kontakte:
    print(name)

# Alle Städte
print("Städte:")
for info in kontakte.values():
    print(info["stadt"])

# Neue Person hinzufügen
kontakte["Tom"] = {"alter": 22, "stadt": "Hamburg"}

print("Kontakte:", kontakte)


# -------------------------------
# Aufgabe 9: Set-Operationen
# -------------------------------
# Typische Mengenoperationen

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Schnittmenge (gemeinsam):", a & b)
print("Vereinigung (alle):", a | b)
print("Differenz (nur in a):", a - b)


# -------------------------------
# Aufgabe 10: Alles kombiniert
# -------------------------------
# Kombination aller Datentypen

personen = {
    "Max": {
        "alter": 25,
        "hobbys": ["Sport", "Gaming"],   # List
        "location": (48.1, 11.6)         # Tuple
    }
}

print("Personenstruktur:", personen)


# -------------------------------
# BONUS: Funktion
# -------------------------------
# Funktionen kapseln Logik

def add_person(db, name, alter, stadt):
    db[name] = {
        "alter": alter,
        "stadt": stadt
    }

kontakte = {}
add_person(kontakte, "Max", 25, "München")
add_person(kontakte, "Anna", 30, "Berlin")

print("Kontakte (Funktion):", kontakte)
