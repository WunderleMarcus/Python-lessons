"""
===============================
ÜBUNGEN: DATENTYPEN & F-STRINGS
===============================

👉 Anleitung:
1. Lies die Aufgabe
2. Kommentiere die Lösung ggf. aus
3. Versuche es selbst
4. Vergleiche mit der Lösung

"""

# =========================
# TEIL 1: DATENTYPEN
# =========================

print("\n--- Übung 1: Datentyp erkennen ---")

a = 10
b = 3.14
c = "Hallo"
d = True
e = [1, 2, 3]

# Aufgabe:
# Bestimme die Datentypen mit type()

# Lösung:
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool
print(type(e))  # list


print("\n--- Übung 2: Typen umwandeln ---")

x = "25"
y = 4.8
z = 10

# Aufgabe:
# x → int
# y → int
# z → str

# Lösung:
x = int(x)
y = int(y)
z = str(z)

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Bonus:
# int("abc")  # → Fehler (ValueError)


print("\n--- Übung 3: Rechnen mit Typen ---")

a = 5
b = "10"

# Aufgabe: Was passiert hier?

# Lösung:
print(a + int(b))   # 15
print(str(a) + b)   # "510"


print("\n--- Übung 4: Listen vs Strings ---")

text = "Python"
liste = ["P", "y", "t", "h", "o", "n"]

# Aufgabe:
# Greife auf das 3. Element zu

# Lösung:
print(text[2])   # t
print(liste[2])  # t


# =========================
# TEIL 2: F-STRINGS
# =========================

print("\n--- Übung 5: Erste f-Strings ---")

name = "Anna"
alter = 25

# Aufgabe:
# "Hallo Anna, du bist 25 Jahre alt."

# Lösung:
print(f"Hallo {name}, du bist {alter} Jahre alt.")


print("\n--- Übung 6: Rechnen im f-String ---")

a = 5
b = 3

# Aufgabe:
# "Die Summe von 5 und 3 ist 8."

# Lösung:
print(f"Die Summe von {a} und {b} ist {a + b}.")


print("\n--- Übung 7: Formatierung ---")

pi = 3.1415926535

# Aufgabe:
# Ausgabe: 3.14

# Lösung:
print(f"Pi gerundet: {pi:.2f}")


print("\n--- Übung 8: Alignment ---")

name = "Max"

# Aufgabe:
# rechtsbündig, Breite 10

# Lösung:
print(f"{name:>10}")
print(f"{name:<10}")
print(f"{name:^10}")


# =========================
# TEIL 3: KOMBINATION
# =========================

print("\n--- Übung 9: Benutzerprofil ---")

name = "Lisa"
alter = 30
groesse = 1.68

# Aufgabe:
# Formatierte Ausgabe erstellen

# Lösung:
print(f"Name: {name}")
print(f"Alter: {alter} Jahre")
print(f"Größe: {groesse:.1f} m")


print("\n--- Übung 10: Mini-Projekt ---")

# Aufgabe:
# Eingabe von Name und Alter
# Ausgabe: "Hallo Max, in 5 Jahren bist du 30 Jahre alt."

# Lösung:
name = input("Name: ")
alter = int(input("Alter: "))

print(f"Hallo {name}, in 5 Jahren bist du {alter + 5} Jahre alt.")


# =========================
# CHALLENGE
# =========================

print("\n--- Übung 11: Tabelle ---")

name = "Tom"
punkte = 87.456

# Aufgabe:
# Tabelle formatieren

# Lösung:
print(f"{'Name':<10} | {'Punkte'}")
print("-" * 20)
print(f"{name:<10} | {punkte:.2f}")


print("\n--- ENDE ---")