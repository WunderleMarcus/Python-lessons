"""
=========================================================
INTERAKTIVE PYTHON CHALLENGE – CLOUD-25-11 (PYTHON DAY 9)
=========================================================

WICHTIG FÜR TEILNEHMER:

Lies jede Aufgabe genau!
Achte auf die geforderte SYNTAX
Gib NUR das ein, was verlangt ist

Beispiel:
Wenn gefragt wird:
"Nur der Ausdruck hinter return"
→ NICHT: return a + b
→ SONDERN: a + b
"""

score = 0


def check(user, expected):
    return str(user).strip().lower() == str(expected).strip().lower()


def pause():
    input("\nENTER drücken...")


# =========================================
# LEVEL 1 – GRUNDLAGEN
# =========================================

def level_1():
    global score
    print("\n=== LEVEL 1: FUNKTIONS-GRUNDLAGEN ===")

    print("""
AUFGABE 1:
Gegeben ist folgende Funktion:

def hallo():
    print("Hallo")

FRAGE:
Wie rufst du diese Funktion korrekt auf?

ERWARTETE EINGABE:
Nur der Funktionsaufruf, z.B.:
hallo.....[]
""")

    if check(input("> "), "hallo()"):
        print("✅ korrekt")
        score += 1
    else:
        print("❌ Falsch → hallo()")

    print("""
AUFGABE 2:
Eine Funktion enthält KEIN return.

FRAGE:
Welchen Wert gibt Python automatisch zurück?

ERWARTETE EINGABE in "Anfühtungszeichen innerhalb der Klammer:

""")

    if check(input("> "), "none"):
        print("✅ korrekt")
        score += 1

    print("""
AUFGABE 3:
Muss jede Funktion einen return haben?

ERWARTETE EINGABE:
ja oder nein
""")

    if check(input("> "), "nein"):
        print("✅ korrekt")
        score += 1

    print("""
AUFGABE 4:
Muss eine Funktion im Code VOR dem Aufruf definiert sein?

ERWARTETE EINGABE:
ja oder nein
""")

    if check(input("> "), "ja"):
        print("✅ korrekt")
        score += 1


# =========================================
# LEVEL 2 – RECHNEN
# =========================================

def level_2():
    global score
    print("\n=== LEVEL 2: RECHNEN MIT PARAMETERN ===")

    print("""
AUFGABE:
Du simulierst eine Funktion:

def rechne(a, b):

Berechne folgende Werte:

1. Summe → a + b
2. Produkt → a * b
3. Differenz → a - b
4. Durchschnitt → (a + b) / 2

 WICHTIG:
- Gib NUR das Ergebnis ein (Zahl)
- KEIN Python-Code!
""")

    a = int(input("Zahl a: "))
    b = int(input("Zahl b: "))

    if check(input("Summe:\n> "), a + b):
        score += 1
        print("✅")

    if check(input("Produkt:\n> "), a * b):
        score += 1
        print("✅")

    if check(input("Differenz:\n> "), a - b):
        score += 1
        print("✅")

    if check(input("Durchschnitt:\n> "), (a + b) / 2):
        score += 1
        print("✅")


# =========================================
# LEVEL 3 – SCOPE
# =========================================

def level_3():
    global score
    print("\n=== LEVEL 3: SCOPE ===")

    print("""
AUFGABE:
Beantworte die Fragen zu Variablen.

 Antworte IMMER mit:
ja oder nein / lokal oder global
""")

    if check(input("Können Funktionen globale Variablen LESEN?\n> "), "ja"):
        score += 1
        print("✅")

    if check(input("Können lokale Variablen globale automatisch ändern?\n> "), "nein"):
        score += 1
        print("✅")

    if check(input("Variablen innerhalb einer Funktion heißen?\n> "), "lokal"):
        score += 1
        print("✅")

    if check(input("Variablen außerhalb heißen?\n> "), "global"):
        score += 1
        print("✅")


# =========================================
# LEVEL 4 – STRINGS
# =========================================

def level_4():
    global score
    print("\n=== LEVEL 4: STRING-METHODEN ===")

    print("""
AUFGABE:
Du bekommst einen Text.

Führe folgende Operationen aus:

1. Entferne Leerzeichen → .strip()
2. Zähle Wörter → .split()
3. Alles groß → .upper()
4. Ersetze a → X

WICHTIG:
- Gib IMMER das RESULTAT ein
- NICHT den Code!
""")

    text = input("Text:\n> ")
    clean = text.strip()

    if check(input("1. Ohne Leerzeichen:\n> "), clean):
        score += 1
        print("✅")

    if check(input("2. Wortanzahl:\n> "), len(clean.split())):
        score += 1
        print("✅")

    if check(input("3. Großbuchstaben:\n> "), clean.upper()):
        score += 1
        print("✅")

    if check(input("4. a → X:\n> "), clean.replace("a", "X")):
        score += 1
        print("✅")


# =========================================
# LEVEL 5 – CODE CHALLENGE
# =========================================

def level_5():
    global score
    print("\n=== LEVEL 5: RETURN-SYNTAX ===")

    print("""
AUFGABE:
Du schreibst Funktionen.

WICHTIG:
Gib NUR den Ausdruck NACH return ein!

❌ Falsch: return a + b
✅ Richtig: a + b
""")

    print("\n1. addiere(a,b)")
    if eval(input("> "), {}, {"a": 3, "b": 5}) == 8:
        score += 1
        print("✅")

    print("\n2. multipliziere(a,b)")
    if eval(input("> "), {}, {"a": 3, "b": 5}) == 15:
        score += 1
        print("✅")

    print("\n3. subtrahiere(a,b)")
    if eval(input("> "), {}, {"a": 5, "b": 3}) == 2:
        score += 1
        print("✅")

    print("""
4. verdopple(x)

Erwartet:
x _ _
""")
    if eval(input("> "), {}, {"x": 4}) == 8:
        score += 1
        print("✅")


# =========================================
# LEVEL 6 – ADVANCED
# =========================================

def level_6():
    global score
    print("\n=== LEVEL 6: ADVANCED RETURN ===")

    print("""
AUFGABE:
Schreibe komplexere Ausdrücke.

Wieder gilt:
NUR der Ausdruck hinter return!
""")

    print("\n1. Quadrat → x2")
    if eval(input("> "), {}, {"x": 4}) == 16:
        score += 1
        print("✅")

    print("\n2. Hälfte → x / 2")
    if eval(input("> "), {}, {"x": 10}) == 5:
        score += 1
        print("✅")

    print("""
3. Preis mit 19% Steuer

Erwartet:
netto * 1.19
""")
    if round(eval(input("> "), {}, {"netto": 100}), 2) == 119:
        score += 1
        print("✅")

    print("""
4. Rest (Modulo)

Erwartet:
a _ _
""")
    if eval(input("> "), {}, {"a": 17, "b": 5}) == 2:
        score += 1
        print("✅")


# =========================================
# MENÜ
# =========================================

def menu():
    while True:
        print("\n====== MENÜ ======")
        print("1 Grundlagen")
        print("2 Rechnen")
        print("3 Scope")
        print("4 Strings")
        print("5 Code")
        print("6 Advanced")
        print("0 Ende")

        choice = input("> ")

        if choice == "1":
            level_1()
        elif choice == "2":
            level_2()
        elif choice == "3":
            level_3()
        elif choice == "4":
            level_4()
        elif choice == "5":
            level_5()
        elif choice == "6":
            level_6()
        elif choice == "0":
            break

        pause()


print("Python Challenge Cloud-25-11")
menu()

print("\nPunkte:", score)