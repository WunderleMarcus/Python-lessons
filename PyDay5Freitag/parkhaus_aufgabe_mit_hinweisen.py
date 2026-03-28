# ============================================================
# PRAXISAUFGABE: SMARTES PARKHAUS-SYSTEM
# ============================================================
#
# Ziel:
# Entwickle Schritt für Schritt ein Parkhaus-System in Python.
#
# Du sollst dabei folgende Konzepte anwenden:
# - if / elif / else
# - Vergleichs- und logische Operatoren
# - while- und for-Schleifen
# - Kontrollstrukturen
#
# ------------------------------------------------------------
# PFLICHTTEIL
# ------------------------------------------------------------
#
# Aufgabe:
# Schreibe ein Programm, das entscheidet, ob ein Auto einfahren darf.
#
# Gegeben:
# - Maximale Kapazität: 50 Autos
# - Eingabe: aktuelle Anzahl Autos im Parkhaus
# - Eingabe: Fahrzeugtyp ("Elektro", "SUV", "Normal")
#
# Regeln:
# - Elektroautos dürfen IMMER einfahren
# - SUVs nur, wenn weniger als 40 Autos im Parkhaus sind
# - Normale Autos nur, wenn das Parkhaus nicht voll ist
#
# Ausgabe:
# - "Einfahrt erlaubt" oder passende Ablehnung
#
# Denkanstoß-Code:
max_kapazitaet = 50

aktuelle_autos = int(input("Autos im Parkhaus: "))
fahrzeug = input("Fahrzeugtyp: ").lower()

if fahrzeug == "elektro":
    print("...")
elif fahrzeug == "suv":
    if aktuelle_autos < ...:
        print("...")
    else:
        print("...")
else:
    if aktuelle_autos < ...:
        print("...")
    else:
        print("...")


# ------------------------------------------------------------
# WEITERFÜHRENDER TEIL
# ------------------------------------------------------------
#
# Aufgabe:
# Erweitere dein Programm:
#
# - Verwende eine while-Schleife
# - Fahrzeuge werden wiederholt eingegeben
# - Eingabe "stop" beendet das Programm
#
# Zähle:
# - wie viele Autos eingefahren sind
# - wie viele abgewiesen wurden
#
# Zusatz:
# - Gib am Ende eine Statistik mit einer for-Schleife aus
#
# Denkanstoß-Code:
rein = 0
abgewiesen = 0

while True:
    eingabe = input("Fahrzeug (oder stop): ")

    if eingabe == "stop":
        break

    # Hier Logik aus Pflichtteil wiederverwenden!
    if ...:
        rein += 1
    else:
        abgewiesen += 1

print("Rein:", rein)
print("Abgewiesen:", abgewiesen)

# Beispiel-Statistik:
stunden = [3, 5, 2]

for i in range(len(stunden)):
    print("Stunde", i+1, ":", stunden[i])


# ------------------------------------------------------------
# BONUSTEIL
# ------------------------------------------------------------
#
# Aufgabe:
# Berechne Parkgebühren abhängig von der Parkdauer.
#
# Regeln:
# - 0–2 Stunden → 2€ pro Stunde
# - 3–5 Stunden → 1.5€ pro Stunde
# - >5 Stunden → Pauschal 10€
#
# Anforderungen:
# - Eingabe der Stunden
# - Berechnung mit if/elif/else
# - Mehrere Berechnungen mit Schleife
#
# Denkanstoß-Code:
stunden = float(input("Parkdauer: "))

if stunden <= 2:
    preis = ...
elif stunden <= 5:
    preis = ...
else:
    preis = ...

print("Preis:", preis)

while True:
    eingabe = input("Stunden (oder stop): ")

    if eingabe == "stop":
        break

    stunden = float(eingabe)
    # Hier Preis berechnen


# ------------------------------------------------------------
# CHALLENGE
# ------------------------------------------------------------
#
# Aufgabe:
# Entwickle ein vollständiges Parkhaus-System mit Menü:
#
# Menü:
# 1 = Einfahrt
# 2 = Ausfahrt
# 3 = Status anzeigen
# 0 = Beenden
#
# Anforderungen:
# - Parkplätze als Liste speichern
# - Freie Plätze automatisch vergeben
# - Plätze wieder freigeben
#
# Extra:
# - Fehlerhafte Eingaben abfangen
# - Optional: Zufällige Autos simulieren
#
# Denkanstoß-Code:
parkplaetze = [None] * 10

# Freien Platz finden
for i in range(len(parkplaetze)):
    if parkplaetze[i] is None:
        parkplaetze[i] = "Auto"
        print("Platz:", i)
        break

# Menü
while True:
    print("1=Einfahrt, 2=Ausfahrt, 3=Status, 0=Ende")
    wahl = input("-> ")

    if wahl == "1":
        pass
    elif wahl == "2":
        pass
    elif wahl == "3":
        pass
    elif wahl == "0":
        break

# ============================================================
# Viel Erfolg! 🚀
# ============================================================

# Hallo zusammen,

# hier noch eine kurze Erklärung zum bereitgestellten Code und wie er im Kontext eurer Abgabe zu verstehen ist:

# Der Code ist bewusst in mehrere Funktionen aufgeteilt, die jeweils einer Teilaufgabe entsprechen:

# pflichtteil() → bildet die grundlegende Logik der Einfahrtskontrolle ab
# weiterfuehrend() → erweitert das Ganze um Schleifen, Zählung und eine einfache Auswertung
# bonus() + berechne_preis() → zeigt eine mögliche Zusatzfunktion (z. B. Preisberechnung)
# challenge() → stellt ein vereinfachtes Gesamtsystem mit Parkplätzen dar


# Wichtig für eure Abgabe:
# Orientiert euch an genau dieser Struktur.

# Das bedeutet:

# Jede Teilaufgabe sollte in einer eigenen Datei umgesetzt werden

# Die Funktionen im Beispiel zeigen euch, welche Logik jeweils erwartet wird


# Für den Challenge-Teil gilt:

# Hier könnt ihr die einzelnen Aspekte in einem Gesamtsystem zusammenführen
# Die Einfahrtslogik sollte enthalten sein
# Erweiterungen (wie z. B. Preisberechnung) sind optional


# Der Code dient also nicht nur als Lösung, sondern auch als Leitfaden für Aufbau und Struktur eurer Abgabe.

# Wenn etwas unklar ist, meldet euch jederzeit!
