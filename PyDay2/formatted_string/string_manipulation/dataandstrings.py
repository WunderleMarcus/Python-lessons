"""
===========================================
ÜBUNGEN: DATENTYPEN & F-STRINGS (OHNE LÖSUNGEN)
===========================================

👉 Ziel:
Diese Übungen helfen dir, ein solides Verständnis für:
- grundlegende Datentypen in Python
- Typumwandlungen
- f-Strings und Formatierung

👉 Vorgehen:
1. Lies die Aufgabenbeschreibung genau
2. Schreibe deinen Code unter die Aufgabe
3. Teste dein Ergebnis mit print()
4. Vergleiche später mit einer Lösung

Tipp: Arbeite Schritt für Schritt – nicht alles auf einmal lösen!
"""

# =========================
# TEIL 1: DATENTYPEN
# =========================

print("\n--- Übung 1: Datentyp erkennen ---")

"""
AUFGABE:
Gegeben sind verschiedene Variablen mit unterschiedlichen Werten.

Deine Aufgabe:
- Finde heraus, welchen Datentyp jede Variable hat
- Nutze dafür die Funktion type()

Erwartung:
Du sollst verstehen, wie Python verschiedene Arten von Daten speichert
(z. B. Zahlen, Texte, Wahrheitswerte, Listen)
"""

a = 10
b = 3.14
c = "Hallo"
d = True
e = [1, 2, 3]

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 2: Typen umwandeln ---")

"""
AUFGABE:
Du hast Variablen mit "falschen" Datentypen für bestimmte Operationen.

Deine Aufgabe:
- Wandle die Variablen in passende Datentypen um

Konkret:
- x soll ein Integer werden
- y soll ein Integer werden (achte auf Nachkommastellen!)
- z soll ein String werden

Zusatz:
Überlege, warum Typumwandlung in Python wichtig ist.
"""

x = "25"
y = 4.8
z = 10

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 3: Rechnen mit Datentypen ---")

"""
AUFGABE:
Du sollst zwei verschiedene Arten von Operationen durchführen.

Gegeben:
- eine Zahl (int)
- ein String, der wie eine Zahl aussieht

Deine Aufgaben:
1. Addiere beide Werte mathematisch
2. Verbinde beide Werte als Text (String)

Ziel:
Verstehen, wann Python rechnet und wann es Texte zusammenfügt.
"""

a = 5
b = "10"

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 4: Listen vs Strings ---")

"""
AUFGABE:
Hier siehst du zwei verschiedene Datentypen:
- einen String
- eine Liste

Deine Aufgaben:
1. Greife jeweils auf das 3. Element zu (Index beachten!)
2. Gib das Element aus

Zusatz:
Überlege:
- Was ist der strukturelle Unterschied zwischen String und Liste?
"""

text = "Python"
liste = ["P", "y", "t", "h", "o", "n"]

# 👉 Schreibe hier deinen Code:



# =========================
# TEIL 2: F-STRINGS
# =========================

print("\n--- Übung 5: Erste f-Strings ---")

"""
AUFGABE:
Du sollst eine formatierte Ausgabe erzeugen.

Gegeben:
- Name
- Alter

Ziel:
Erstelle folgenden Satz mit einem f-String:

"Hallo Anna, du bist 25 Jahre alt."

Wichtig:
- Verwende die f-String-Syntax: f"...{variable}..."
"""

name = "Anna"
alter = 25

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 6: Rechnen im f-String ---")

"""
AUFGABE:
Du sollst eine Berechnung direkt im f-String durchführen.

Gegeben:
- zwei Zahlen

Ziel:
Gib folgenden Satz aus:

"Die Summe von 5 und 3 ist 8."

Wichtig:
- Die Rechnung soll direkt im f-String passieren (nicht vorher speichern)
"""

a = 5
b = 3

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 7: Formatierung von Zahlen ---")

"""
AUFGABE:
Du arbeitest mit einer Zahl mit vielen Nachkommastellen.

Ziel:
- Runde die Zahl auf 2 Nachkommastellen
- Gib sie formatiert aus

Erwartete Ausgabe:
Pi gerundet: 3.14

Tipp:
Nutze Formatierung innerhalb von f-Strings
"""

pi = 3.1415926535

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 8: Textausrichtung ---")

"""
AUFGABE:
Du sollst Text in einer bestimmten Breite formatieren.

Gegeben:
- ein Name

Deine Aufgaben:
1. Gib den Namen rechtsbündig mit Breite 10 aus
2. Optional:
   - linksbündig
   - zentriert

Ziel:
Verstehen, wie Text formatiert und ausgerichtet wird
(z. B. für Tabellen)
"""

name = "Max"

# 👉 Schreibe hier deinen Code:



# =========================
# TEIL 3: KOMBINATION
# =========================

print("\n--- Übung 9: Benutzerprofil ---")

"""
AUFGABE:
Du sollst mehrere Variablen in einer strukturierten Ausgabe darstellen.

Gegeben:
- Name
- Alter
- Größe

Ziel:
Erstelle eine saubere, mehrzeilige Ausgabe wie:

Name: Lisa
Alter: 30 Jahre
Größe: 1.7 m

Zusatz:
- Runde die Größe sinnvoll
"""

name = "Lisa"
alter = 30
groesse = 1.68

# 👉 Schreibe hier deinen Code:



print("\n--- Übung 10: Mini-Projekt ---")

"""
AUFGABE:
Erstelle ein kleines interaktives Programm.

Deine Aufgaben:
1. Frage den Benutzer nach seinem Namen (input)
2. Frage nach seinem Alter
3. Berechne das Alter in 5 Jahren
4. Gib eine personalisierte Nachricht aus

Ziel:
"Hallo Max, in 5 Jahren bist du 30 Jahre alt."

Wichtig:
- input() liefert Strings → ggf. umwandeln!
- Nutze f-Strings
"""

# 👉 Schreibe hier deinen Code:



# =========================
# CHALLENGE
# =========================

print("\n--- Übung 11: Formatierte Tabelle ---")

"""
AUFGABE:
Du sollst eine einfache Tabelle erstellen.

Gegeben:
- Name
- Punktezahl (mit Nachkommastellen)

Ziel:
Erzeuge eine Ausgabe wie:

Name       | Punkte
-------------------
Tom        | 87.46

Anforderungen:
- Spalten sauber ausrichten
- Zahl auf 2 Nachkommastellen runden
- Trennlinie erzeugen

Hinweis:
Diese Aufgabe kombiniert alles:
- Datentypen
- Formatierung
- f-Strings
"""

name = "Tom"
punkte = 87.456

# 👉 Schreibe hier deinen Code:



print("\n--- ENDE DER ÜBUNGEN ---")