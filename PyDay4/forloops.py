
# =========================
# Teil 1: Grundidee
# =========================

# Aufgabe 1.1
# Gib die Zahlen von 1 bis 5 aus


# Aufgabe 1.2
# Gegeben ist die Liste. Gib jede Zahl einzeln aus
zahlen = [3, 7, 2, 9]


# Aufgabe 1.3
# Berechne die Summe aller Zahlen in der Liste
zahlen = [1, 2, 3, 4, 5]


# =========================
# Teil 2: range()
# =========================

# Aufgabe 2.1
# Gib alle Zahlen von 0 bis 9 aus



# Aufgabe 2.2
# Gib alle Zahlen von 5 bis 10 aus



# Aufgabe 2.3
# Gib alle geraden Zahlen zwischen 0 und 20 aus



# Aufgabe 2.4
# Gib die Zahlen von 10 bis 1 rückwärts aus



# =========================
# Teil 3: enumerate()
# =========================

# Aufgabe 3.1
# Gib Namen mit ihrem Index aus
namen = ["Anna", "Ben", "Clara"]



# Aufgabe 3.2
# Gib die Namen nummeriert aus (beginnend bei 1)



# Aufgabe 3.3
# Finde die Position von "Python"
sprachen = ["Java", "C++", "Python", "Go"]



# =========================
# Teil 4: Strings
# =========================

# Aufgabe 4.1
# Gib jeden Buchstaben aus
text = "Hallo"



# Aufgabe 4.2
# Zähle die Vokale
text = "Programmieren macht Spaß"



# Aufgabe 4.3
# Gib nur Großbuchstaben aus
text = "PyThOn Is FuN"



# =========================
# Teil 5: Kombiniert
# =========================

# Aufgabe 5.1
# Zähle die Wörter im Satz
satz = "Python ist eine tolle Programmiersprache"



# Aufgabe 5.2
# Gib den String rückwärts aus (ohne [::-1])
text = "Python"



# Aufgabe 5.3
# Zähle die Häufigkeit der Buchstaben
text = "banana"



# Aufgabe 5.4
# Passwort-Checker
# Bedingungen:
# - mindestens 8 Zeichen
# - enthält mindestens eine Zahl
passwort = "Test1234"



# =========================
# BONUS
# =========================

# Aufgabe 6: FizzBuzz
# Zahlen von 1 bis 30



# ======================================================
# ================== MUSTERLÖSUNGEN =====================
# ======================================================

# Aufgabe 1.1
#for i in range(1, 6):
#    print(i)

# Aufgabe 1.2
#for zahl in zahlen:
#    print(zahl)

# Aufgabe 1.3
#summe = 0 
#for zahl in zahlen:
#    summe += zahl
#   print(summe)

# Aufgabe 2.1
#for i in range(10):
#    print(i)

# Aufgabe 2.2
#for i in range(5, 11):
#   print(i)

# Aufgabe 2.3
# for i in range(0, 21, 2):
#     print(i)

# Aufgabe 2.4
# for i in range(10, 0, -1):
#     print(i)

# Aufgabe 3.1
# for index, name in enumerate(namen):
#     print(index, name)

# Aufgabe 3.2
# for index, name in enumerate(namen, start=1):
#     print(f"{index}. {name}")

# Aufgabe 3.3
# for index, sprache in enumerate(sprachen):
#     if sprache == "Python":
#         print(index)

# Aufgabe 4.1
# for buchstabe in text:
#     print(buchstabe)

# Aufgabe 4.2
# vokale = "aeiouAEIOU"
# count = 0
# for buchstabe in text:
#     if buchstabe in vokale:
#         count += 1
# print(count)

# Aufgabe 4.3
# for buchstabe in text:
#     if buchstabe.isupper():
#         print(buchstabe)

# Aufgabe 5.1
# count = 0
# for wort in satz.split():
#     count += 1
# print(count)

# Aufgabe 5.2
# for i in range(len(text) - 1, -1, -1):
#     print(text[i])

# Aufgabe 5.3
# haeufigkeit = {}
# for buchstabe in text:
#     if buchstabe in haeufigkeit:
#         haeufigkeit[buchstabe] += 1
#     else:
#         haeufigkeit[buchstabe] = 1
# for k, v in haeufigkeit.items():
#     print(f"{k}: {v}")

# Aufgabe 5.4
# hat_zahl = False
# for zeichen in passwort:
#     if zeichen.isdigit():
#         hat_zahl = True
#
# if len(passwort) >= 8 and hat_zahl:
#     print("Gültiges Passwort")
# else:
#     print("Ungültiges Passwort")

# Aufgabe 6
# for i in range(1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
