"""
Python Übungen: Kontrollstrukturen
Thema: Login-System, Bedingungen, Schleifen, Rollen

===============================
📘 AUSFÜHRLICHE AUFGABENSTELLUNG
===============================

Zeit: 45 Minuten
Ziel: Entwicklung eines einfachen Authentifizierungssystems

-------------------------------
Schritt 1: Login-System
-------------------------------
- Benutzername abfragen
- Passwort abfragen
- Verwende im Code gespeicherte Test-Credentials
- Bei korrekten Daten: Zugang gewähren
- Bei falschen Daten: Fehlermeldung ausgeben

-------------------------------
Schritt 2: Erweiterte Prüfung
-------------------------------
- Alter des Benutzers abfragen
- Nur Benutzer ab 18 Jahren dürfen zugreifen
- Wenn unter 18: Ausgabe "Zugriff verweigert - zu jung"

-------------------------------
Schritt 3: Rollenbasierter Zugriff
-------------------------------
- Rolle des Benutzers abfragen (admin, user, guest)
- Rechte:
    admin → Vollzugriff
    user  → Eingeschränkter Zugriff
    guest → Nur Lesezugriff

-------------------------------
Schritt 4: Dreimalige Eingabe
-------------------------------
- Maximal 3 Login-Versuche erlauben
- Nach 3 falschen Versuchen: "Account gesperrt"

-------------------------------
Bonus: match-Statement
-------------------------------
- Verwende match-case für die Rollenprüfung

===============================
📌 HINWEIS
===============================
Dieses Skript enthält:
- Aufgaben (als Kommentare)
- Musterlösungen direkt darunter

👉 Tipp:
Kommentiere alle anderen Übungen aus, wenn du nur eine testen willst.
"""

# =============================
# 🟢 Übung 1 – Einfach (Login)
# =============================
# Aufgabe:
# Benutzername = "user"
# Passwort = "pass"
# Prüfe Eingaben
# Ausgabe: Erfolg oder Fehler

print("\n--- Übung 1 ---")
correct_username = "user"
correct_password = "pass"

username = input("Benutzername: ")
password = input("Passwort: ")

if username == correct_username and password == correct_password:
    print("Erfolg")
else:
    print("Fehler")

# =============================
# 🟡 Übung 2 – Alter prüfen
# =============================
# Aufgabe:
# Alter abfragen
# <18 → Kein Zugang
# sonst → Willkommen

print("\n--- Übung 2 ---")
age = int(input("Alter: "))

if age < 18:
    print("Kein Zugang")
else:
    print("Willkommen")

# =============================
# 🟠 Übung 3 – Rollen (if/elif)
# =============================
# Aufgabe:
# admin → Alles erlaubt
# user → Teilweise Zugriff
# guest → Nur lesen

print("\n--- Übung 3 ---")
role = input("Rolle: ").lower()

if role == "admin":
    print("Alles erlaubt")
elif role == "user":
    print("Teilweise Zugriff")
elif role == "guest":
    print("Nur lesen")
else:
    print("Unbekannte Rolle")

# =============================
# 🔵 Übung 4 – Rollen (match)
# =============================

print("\n--- Übung 4 ---")
role = input("Rolle: ").lower()

match role:
    case "admin":
        print("Alles erlaubt")
    case "user":
        print("Teilweise Zugriff")
    case "guest":
        print("Nur lesen")
    case _:
        print("Unbekannte Rolle")

# =============================
# 🔴 Übung 5 – Login mit 3 Versuchen
# =============================

print("\n--- Übung 5 ---")
correct_username = "admin"
correct_password = "1234"

attempts = 0

while attempts < 3:
    username = input("Benutzername: ")
    password = input("Passwort: ")

    if username == correct_username and password == correct_password:
        print("Login erfolgreich")
        break
    else:
        attempts += 1
        print(f"Fehler! Versuch {attempts} von 3")

if attempts == 3:
    print("Account gesperrt")

# =============================
# 🟣 Übung 6 – Kombi-Aufgabe
# =============================

print("\n--- Übung 6 ---")
correct_username = "admin"
correct_password = "1234"

username = input("Benutzername: ")
password = input("Passwort: ")

if username == correct_username and password == correct_password:
    print("Login erfolgreich")

    age = int(input("Alter: "))

    if age < 18:
        print("Zugriff verweigert - zu jung")
    else:
        role = input("Rolle: ").lower()

        if role == "admin":
            print("Vollzugriff gewährt")
        else:
            print("Zugriff verweigert - kein Admin")
else:
    print("Login fehlgeschlagen")

# =============================
# ⚫ Bonus – Dictionary-System
# =============================

print("\n--- Bonus ---")
users = {
    "admin": {"password": "1234", "age": 25, "role": "admin"},
    "max": {"password": "abcd", "age": 16, "role": "user"}
}

username = input("Benutzername: ")
password = input("Passwort: ")

if username in users and users[username]["password"] == password:
    print("Login erfolgreich")

    age = users[username]["age"]

    if age < 18:
        print("Zugriff verweigert - zu jung")
    else:
        role = users[username]["role"]

        match role:
            case "admin":
                print("Vollzugriff")
            case "user":
                print("Eingeschränkter Zugriff")
            case "guest":
                print("Nur Lesen")
            case _:
                print("Unbekannte Rolle")
else:
    print("Login fehlgeschlagen")
