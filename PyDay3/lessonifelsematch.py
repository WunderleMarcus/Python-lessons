"""
Python Zusatzübungen – Vertiefung (mit direkten Erklärungen & steigender Schwierigkeit)

Ziel:
- Jede Aufgabe erklärt sofort, WAS passiert und WARUM
- Schwierigkeit steigt Schritt für Schritt

Tipp:
👉 Lies erst die Erklärung, dann versuche den Code zu verstehen
👉 Danach selbst nachprogrammieren
"""

# =============================
# 🟢 LEVEL 1 – Grundlagen (if)
# =============================
print("\n--- LEVEL 1 ---")

# Erklärung:
# input() liest eine Eingabe als Text
# == vergleicht zwei Werte

name = input("Name: ")

if name == "admin":
    print("Willkommen Admin")
else:
    print("Unbekannter Benutzer")


# =============================
# 🟡 LEVEL 2 – Zahlen & Bedingungen
# =============================
print("\n--- LEVEL 2 ---")

# Erklärung:
# int() wandelt Text in Zahl um
# Vergleich mit < (kleiner als)

age = int(input("Alter: "))

if age < 18:
    print("Kein Zugang")
else:
    print("Zugang erlaubt")


# =============================
# 🟠 LEVEL 3 – Mehrere Bedingungen (elif)
# =============================
print("\n--- LEVEL 3 ---")

# Erklärung:
# elif = weitere Bedingung prüfen
# Reihenfolge ist wichtig!

age = int(input("Alter: "))

if age < 13:
    print("Kind")
elif age < 18:
    print("Jugendlich")
else:
    print("Erwachsen")


# =============================
# 🔵 LEVEL 4 – Strings bearbeiten
# =============================
print("\n--- LEVEL 4 ---")

# Erklärung:
# .lower() macht alles klein → vermeidet Fehler bei Eingaben

username = input("Benutzername: ").lower()

if username == "admin":
    print("Admin erkannt")
else:
    print("Normaler Benutzer")


# =============================
# 🔴 LEVEL 5 – while-Schleife
# =============================
print("\n--- LEVEL 5 ---")

# Erklärung:
# while läuft solange Bedingung True ist
# counter zählt Versuche

counter = 0

while counter < 3:
    print("Versuch", counter + 1)
    counter += 1

print("Fertig")


# =============================
# 🟣 LEVEL 6 – Login mit Versuchen
# =============================
print("\n--- LEVEL 6 ---")

# Erklärung:
# Kombination aus if + while

correct_password = "1234"
attempts = 0

while attempts < 3:
    password = input("Passwort: ")

    if password == correct_password:
        print("Erfolg")
        break  # beendet die Schleife sofort
    else:
        print("Falsch")
        attempts += 1

if attempts == 3:
    print("Gesperrt")


# =============================
# ⚫ LEVEL 7 – Dictionary (echte Struktur)
# =============================
print("\n--- LEVEL 7 ---")

# Erklärung:
# Dictionary speichert Daten wie eine kleine Datenbank

users = {
    "admin": {"password": "1234", "role": "admin"},
    "max": {"password": "abcd", "role": "user"}
}

username = input("Benutzername: ")
password = input("Passwort: ")

if username in users:
    if users[username]["password"] == password:
        print("Login erfolgreich")
    else:
        print("Falsches Passwort")
else:
    print("User existiert nicht")


# =============================
# 🚀 LEVEL 8 – Rollen mit match
# =============================
print("\n--- LEVEL 8 ---")

# Erklärung:
# match ersetzt viele if-Abfragen → sauberer Code

role = input("Rolle: ").lower()

match role:
    case "admin":
        print("Vollzugriff")
    case "user":
        print("Eingeschränkt")
    case "guest":
        print("Nur Lesen")
    case _:
        print("Unbekannt")


# =============================
# 🧠 LEVEL 9 – Mini-System (alles kombiniert)
# =============================
print("\n--- LEVEL 9 ---")

# Erklärung:
# Jetzt kommt alles zusammen:
# Login + Schleife + Dictionary + Rolle

users = {
    "admin": {"password": "1234", "role": "admin"},
    "max": {"password": "abcd", "role": "user"}
}

attempts = 0

while attempts < 3:
    username = input("Benutzername: ")
    password = input("Passwort: ")

    if username in users and users[username]["password"] == password:
        print("Login erfolgreich")

        role = users[username]["role"]

        match role:
            case "admin":
                print("Adminbereich")
            case "user":
                print("Userbereich")
            case _:
                print("Kein Zugriff")

        break
    else:
        print("Fehler")
        attempts += 1

if attempts == 3:
    print("Account gesperrt")
