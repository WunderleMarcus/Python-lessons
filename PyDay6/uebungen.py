# exercises.py
# Python Übungen: List, Tuple, Set, Dict

# Aufgabe 1: List
# Erstelle eine Liste mit 5 Lieblingsfilmen
"""
films = ["Matrix", "Inception", "Interstellar", "Avatar", "Titanic"]
# Zugriff über Index (0 = erstes Element)

print("erstes Element:", films[0])

# Element hinzufügen
films.append("Gladiator")

#Element aus der Liste ändern (Index 2 = drittes Element der Liste)
films[2] = "Der Herr der Ringe"

print("Liste nach Änderungen:", films)

# Aufgabe 2: Tuple
# Speichere Koordinaten und gib sie aus

coordinates = (48.1, 11.6)

# Zugriff über den Indexwert
print("Breitengrad.", coordinates[0])
print("Längengrad.", coordinates[1])

# Tuple-Unpacking über Variablenzuweisung
x, y = coordinates
print("Unpacked:", x, y)


# Aufgabe 3: Set
# Erstelle ein Set mit Duplikaten

zahlen_set = {1, 2, 2, 3, 4, 4, 5}
print("Set mit/ohne Duplikaten:", zahlen_set)

#Ausageb: Set ohne Duplikate: {1, 2, 3, 4, 5}

zahlen_set.add(6)
print("Set nach Hinzufügen von der Zahl 6:", zahlen_set)

# Membership-Test: Ist die Zahl 8 im Set enthalten?
print("Ist die Zahl 8 im Set enthalten?", 8 in zahlen_set)

# Aufgabe 4: Dictionary
# Erstelle ein Dictionary mit Personendaten

person = {
    "name": "Max",
    "alter": 25,
    "stadt": "Zwickau"
}
# Zugriff über den (Key-Wert/ Schlüssel)
print("Name:", person["name"])

#Wert verändern innerhalb des Dicts - Alter auf 26 ändern
person["alter"] = 26
print("Alter", person["alter"])

#Neues Feld im Dict einfügen
person["job"] = "Entwickler"

print("Person:", person)


for key in person.keys():
    print(key)

print("Max" in person)

"""
# Aufgabe 5: List + Schleife
# Summe berechnen

"""
zahlen = [1, 2, 3, 4, 5]
summe = 0
for zahl in zahlen:
    print("Zahl:", zahl)
    summe += zahl   
    
    print("Summe bis jetzt:", summe)
"""
"""
# Aufgabe 6: Set vs List
zahlen = [1, 2, 2, 3, 4, 4, 5]

#Schritt 1: in Set umwandeln (Duplikate weg)
unique = set(zahlen)
# Schritt 2: umwandeln des Sets zurück in eine Liste
unique_list = list(unique)

print("Ohne Duplikate als Liste", unique_list)
"""


# Aufgabe 7: Dictionary + Schleife
"""
noten = {
    "Mathe": 2,
    "Deutsch": 3,
    "Informatik": 1
}

summe = 0

#Iteration über die Key-Values
for fach, note in noten.items():
    print(F"{fach}: {note}")
    summe += note
    
# Durschnschnitt berechnen (2+3+1 / Anzahl der Noten "3")
durchschnitt = summe / len(noten) 
print("Durchschnittsnote aus allen Fächern:", durchschnitt)
"""
# Aufgabe 8: Mini-Kontaktliste


# Aufgabe 9: Set-Logik
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
# Schnittmenge aus 2 Sets berechnen
print ("Schnittmenge:", a & b)  
 
# Vereinigung aus 2 Sets berechnen
print("Vereinigung:", a | b)

# Differenz aus 2 Sets berechnen (Elemente in a, die nicht in b sind)
print("Differenz:", a - b)

# Aufgabe 10: Alles kombiniert
