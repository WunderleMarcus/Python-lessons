# =========================================
# LÖSUNGEN: Python Datenstrukturen (kommentiert)
# =========================================


# ----------------------
# Aufgabe 1: Listen
# ----------------------

# Wir erstellen eine Liste (ordered, veränderbar)
fruits = ["Apfel", "Banane", "Kirsche"]

# Iteration über die Liste
# -> Jedes Element wird nacheinander der Variable 'fruit' zugewiesen
for fruit in fruits:
    print(fruit)

#   Stolpersteine:
# - Einrückung ist entscheidend! (Python nutzt Einrückung statt Klammern)
# - Variablenname frei wählbar, aber sinnvoll benennen (fruit statt x)


# ----------------------
# Aufgabe 2: List Comprehension
# ----------------------

numbers = [1, 2, 3, 4, 5]

# List Comprehension:
# Syntax: [Ausdruck for Element in Iterable]
# Hier: x**2 bedeutet "x zum Quadrat"
squared = [x**2 for x in numbers]

print(squared)

#   Stolpersteine:
# - Syntax wird oft verwechselt (Reihenfolge beachten!)
# - Vergleich mit klassischer Variante hilft beim Verständnis:
#   squared = []
#   for x in numbers:
#       squared.append(x**2)


# ----------------------
# Aufgabe 3: Verschachtelte Schleifen
# ----------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Erste Schleife: geht durch jede "Zeile"
for row in matrix:
    
    # Zweite Schleife: geht durch jedes Element in der Zeile
    for item in row:
        
        # end=" " verhindert Zeilenumbruch nach jedem print
        print(item, end=" ")
    
    # Nach jeder Zeile ein Zeilenumbruch
    print()

#   Stolpersteine:
# - Verständnis: äußere vs. innere Schleife
# - Ohne end=" " würde jede Zahl untereinander stehen
# - Einrückung ist hier besonders fehleranfällig


# ----------------------
# Aufgabe 4: Tuples
# ----------------------

coordinates = [(1, 2), (3, 4), (5, 6)]

# Tuple-Unpacking:
# (1,2) wird direkt in x und y zerlegt
for x, y in coordinates:
    print(f"x={x}, y={y}")

#   Stolpersteine:
# - Anzahl der Variablen muss zur Tuple-Größe passen!
#   (z.B. (1,2,3) -> Fehler bei x,y)
# - Tuples sind immutable (nicht veränderbar)


# ----------------------
# Aufgabe 5: Sets
# ----------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Schnittmenge: nur gemeinsame Elemente
print("Schnittmenge:", a & b)

# Vereinigung: alle Elemente ohne Duplikate
print("Vereinigung:", a | b)

#   Stolpersteine:
# - Sets sind ungeordnet → Ausgabe-Reihenfolge kann variieren!
# - Operatoren (&, |) oft unbekannt für Anfänger
# - Alternative Schreibweise:
#   a.intersection(b)
#   a.union(b)


# ----------------------
# Aufgabe 6: Dictionaries
# ----------------------

student = {"Name": "Anna", "Alter": 23, "Studiengang": "Informatik"}

# Iteration über Schlüssel
for key in student:
    print(key, student[key])  # Zugriff auf Wert über key

# Iteration über Schlüssel-Wert-Paare
for key, value in student.items():
    print(key, value)

#   Stolpersteine:
# - Unterschied zwischen key und value verstehen!
# - student[key] funktioniert nur, wenn key existiert
# - items() ist oft der bessere Weg


# ----------------------
# Aufgabe 7: Dictionary Comprehension
# ----------------------

scores = {"Math": 90, "Deutsch": 85, "Englisch": 95}

# Dictionary Comprehension:
# Syntax: {key: value for key, value in iterable if Bedingung}
high_scores = {k: v for k, v in scores.items() if v > 90}

print(high_scores)

#   Stolpersteine:
# - Reihenfolge der Elemente (key: value zuerst!)
# - Bedingung am Ende nicht vergessen
# - items() notwendig, um key UND value zu bekommen


# ----------------------
# Aufgabe 8: Kombinationsaufgabe
# ----------------------

# Liste von 1 bis 10
# range(1,11) → 11 wird NICHT eingeschlossen!
nums = list(range(1, 11))

# Quadrate
squares = [x**2 for x in nums]

# Tuple aus ersten drei Elementen
# nums[:3] erzeugt eine Liste → tuple() wandelt um
first_three = tuple(nums[:3])

# Sets: gerade und ungerade Zahlen
even = {x for x in nums if x % 2 == 0}  # durch 2 teilbar
odd = {x for x in nums if x % 2 != 0}   # Rest != 0

print(nums)
print(squares)
print(first_three)

# Schnittmenge (sollte leer sein!)
print("Schnittmenge:", even & odd)

# Vereinigung (alle Zahlen wieder enthalten)
print("Vereinigung:", even | odd)

#   Stolpersteine:
# - % Operator (Modulo) oft neu für Anfänger
# - Verständnis gerade/ungerade Zahlen
# - Leere Schnittmenge kann verwirren


# ----------------------
# Aufgabe 9: Buchstaben zählen
# ----------------------

word = "programming"
letter_count = {}

# Iteration über jeden Buchstaben im String
for letter in word:
    
    # get(letter, 0):
    # → gibt aktuellen Wert zurück oder 0, falls nicht vorhanden
    letter_count[letter] = letter_count.get(letter, 0) + 1

# Nur Buchstaben ausgeben, die mehrfach vorkommen
for letter, count in letter_count.items():
    if count > 1:
        print(letter)

#   Stolpersteine:
# - Ohne get() → KeyError möglich!
# - Strings sind iterierbar (wichtiges Konzept!)
# - Verständnis: Zählen mit Dictionaries


# ----------------------
# Bonus: Multiplikationstableau
# ----------------------

# Äußere Schleife = Zeilen
for i in range(1, 4):
    
    # Innere Schleife = Spalten
    for j in range(1, 4):
        
        # Multiplikation von i und j
        print(i * j, end=" ")
    
    # Neue Zeile nach jeder Reihe
    print()

#   Stolpersteine:
# - Verschachtelung verstehen
# - Reihenfolge der Schleifen
# - Einrückung ist kritisch!