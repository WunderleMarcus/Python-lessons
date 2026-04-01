# ===============================================
# Python Iteration & Methoden: Übersicht + Beispiele
# ===============================================
# Autor: Marcus Wunderle
# Beschreibung: Dieses Skript demonstriert alle wichtigen Methoden und Iterationsmöglichkeiten
# für Listen, Sets, Dictionaries und Tuples in Python, inklusive detaillierter Erklärungen
# und praxisnaher Anwendungsfälle.
# ===============================================

# ===============================
# LISTEN (List)
# ===============================
print("---- LISTEN ----")

# Beispiel-Liste
lst = [1, 2, 3, 4, 5]

# 1. append(): fügt ein Element am Ende der Liste hinzu
# Praxis: neue Kundenbestellung hinzufügen
lst.append(6)
print("Nach append(6):", lst)

# 2. extend(): fügt mehrere Elemente hinzu
# Praxis: neue Lieferungen aus API hinzufügen
lst.extend([7, 8])
print("Nach extend([7,8]):", lst)

# 3. insert(): fügt Element an bestimmter Position ein
# Praxis: Priorisierte Bestellung an 2. Position einfügen
lst.insert(1, 10)
print("Nach insert(1,10):", lst)

# 4. remove(): entfernt das erste Vorkommen eines Werts
# Praxis: fehlerhafte Bestellungen entfernen
lst.remove(2)
print("Nach remove(2):", lst)

# 5. pop(): entfernt Element am Index und gibt es zurück
# Praxis: letzte Bestellung bearbeiten
last_order = lst.pop()
print("Nach pop():", lst, "→ entfernte Bestellung:", last_order)

# 6. index(): findet Index eines Elements
# Praxis: Position einer Bestellung ermitteln
index_of_4 = lst.index(4)
print("Index von 4:", index_of_4)

# 7. count(): zählt, wie oft ein Element vorkommt
# Praxis: Häufigkeit bestimmter Produkte prüfen
count_3 = lst.count(3)
print("Anzahl der 3er:", count_3)

# 8. sort() & reverse()
# Praxis: Umsatzliste sortieren / Historische Daten umkehren
lst.sort()
print("Nach sort():", lst)
lst.reverse()
print("Nach reverse():", lst)

# 9. enumerate(): Iteration mit Index
print("Iteration mit enumerate():")
for i, val in enumerate(lst):
    print(f"Index {i} → Wert {val}")

# 10. List Comprehension: Transformation + Filter
# Praxis: Feature Engineering für ML
lst_transformed = [x*2 for x in lst if x%2==0]
print("List Comprehension (gerade*2):", lst_transformed)


# ===============================
# SETS
# ===============================
print("\n---- SETS ----")

s = {1, 2, 3}

# add(): Element hinzufügen → Eindeutige IDs sammeln
s.add(4)
print("Nach add(4):", s)

# update(): mehrere Elemente hinzufügen
s.update([5,6])
print("Nach update([5,6]):", s)

# remove(): Element entfernen (Fehler, falls nicht vorhanden)
s.remove(2)
print("Nach remove(2):", s)

# discard(): Element entfernen ohne Fehler
s.discard(10)
print("Nach discard(10) (kein Fehler):", s)

# pop(): zufälliges Element entfernen
removed = s.pop()
print("Nach pop():", s, "→ entfernte Element:", removed)

# union() / intersection() / difference()
s2 = {3,4,7}
print("Union:", s | s2)
print("Intersection:", s & s2)
print("Difference:", s - s2)

# Set Comprehension
set_transformed = {x*10 for x in s if x%2==0}
print("Set Comprehension (gerade*10):", set_transformed)


# ===============================
# DICTIONARIES
# ===============================
print("\n---- DICTIONARIES ----")

d = {"name":"Anna", "age":25, "city":"Berlin"}

# Zugriff: dict[key]
print("Name:", d["name"])

# get(): Zugriff mit Defaultwert
print("Alter:", d.get("age",0))
print("Land (nicht vorhanden):", d.get("country","DE"))

# keys(), values(), items()
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

# pop(): entfernt Schlüssel + Wert
age = d.pop("age")
print("Nach pop('age'):", d, "→ entfernte Wert:", age)

# update(): fügt Werte aus anderem dict hinzu
d.update({"city":"Munich","role":"Manager"})
print("Nach update():", d)

# Dict Comprehension: Filter + Transformation
grades = {"Anna":1.7,"Ben":2.3,"Clara":1.3}
top_students = {k:v for k,v in grades.items() if v<2.0}
print("Top Students (Note<2.0):", top_students)


# ===============================
# TUPLES
# ===============================
print("\n---- TUPLES ----")

t = (10,20,30)

# Indexing & Slicing
print("t[0]:", t[0])
print("t[1:3]:", t[1:3])

# len()
print("Länge des Tuples:", len(t))

# Iteration
print("Iteration über Tuple:")
for x in t:
    print(x)

# Tuple Comprehension via Generator + tuple()
t2 = tuple(x*2 for x in t)
print("Tuple Comprehension (x*2):", t2)


# ===============================
# Weitere Tools für Iteration
# ===============================
print("\n---- WEITERE ITERATIONSTOOLS ----")

names = ["Anna","Ben","Clara"]
ages = [25,30,22]

# zip(): parallele Iteration
print("zip():")
for n,a in zip(names, ages):
    print(f"{n} → {a}")

# reversed(): Rückwärtsiteration
print("reversed():")
for n in reversed([1,2,3]):
    print(n)

# sorted(): sortierte Iteration
print("sorted():")
for n in sorted({3,1,2}):
    print(n)

# itertools für komplexe Iterationen
import itertools
print("itertools.permutations([1,2,3],2):")
for p in itertools.permutations([1,2,3],2):
    print(p)