# =========================================
# AUFGABEN: Python Datenstrukturen
# =========================================

# Ziel:
# Bearbeite die folgenden Aufgaben zu Listen, Tuples, Sets und Dictionaries.


# ----------------------
# Aufgabe 1: Listen
# ----------------------
# Erstelle eine Liste mit den Werten:
# ["Apfel", "Banane", "Kirsche"]
# Iteriere über die Liste und gib jedes Element aus.
"""
fruits = ["Apfel", "Banane", "Kirsche"]
for fruit in fruits:
    print(fruit)
"""
# ----------------------
# Aufgabe 2: List Comprehension
# ----------------------
# Gegeben:

"""
numbers = [1, 2, 3, 4, 5]

# Erstelle eine neue Liste mit den Quadraten der Zahlen. (Plus gerade Zahlen mit Modulo Operator {Rechnen mit und ohne Rest})
quadratzahl = [x**2 for x in numbers if x % 2 == 0]
print(quadratzahl)
"""
# ----------------------
# Aufgabe 3: Verschachtelte Schleifen
# ----------------------
# Gegeben:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Gib alle Elemente der Matrix in tabellarischer Form aus.


# ----------------------
# Aufgabe 4: Tuples
# ----------------------
# Gegeben:
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Iteriere über die Liste und gib die Werte im Format aus:
# x=1, y=2

"""
for x, y in coordinates:
    print(f"x={x}, y={y}")
"""    
    
    
# ----------------------
# Aufgabe 5: Sets
# ----------------------
# Gegeben:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Bestimme:
# - die Schnittmenge
# - die Vereinigung
"""
print("Schnittmenge:", a & b)

print("Vereinigung:", a | b)
"""
# ----------------------
# Aufgabe 6: Dictionaries
# ----------------------
# Gegeben:
"""
student = {"Name": "Anna", "Alter": 23, "Studiengang": "Informatik"}
for key in student:
    print(key, student[key])

# Gib alle Schlüssel und Werte aus.
# Nutze zusätzlich .items()
for key, value in student.items():
    print(key, value)
"""
# ----------------------
# Aufgabe 7: Dictionary Comprehension
# ----------------------
# Gegeben:
noten = {"Mathe": 90, "Deutsch": 85, "Englisch": 95}

# Erstelle ein neues Dictionary mit Werten > 90
gute_noten = {k: v for k, v in noten.items() if v >= 90}
print(gute_noten)





# ----------------------
# Aufgabe 8: Kombinationsaufgabe
# ----------------------
# 1. Liste von 1 bis 10 erstellen
# 2. Quadrate berechnen
# 3. Tuple aus ersten drei Zahlen
# 4. Sets für gerade und ungerade Zahlen
# 5. Schnittmenge & Vereinigung


# ----------------------
# Aufgabe 9: Buchstaben zählen
# ----------------------
word = "programming"

# Zähle die Häufigkeit jedes Buchstabens
# Gib nur Buchstaben aus, die mehr als einmal vorkommen


# ----------------------
# Bonus
# ----------------------
# Erstelle ein 3x3 Multiplikationstableau
