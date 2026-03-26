
# =========================
# Teil 1: Grundidee
# =========================

# Aufgabe 1.1
# Gib die Zahlen von 1 bis 5 mit einer while-Schleife aus



# Aufgabe 1.2
# Gib alle Zahlen aus der Liste aus (mit Index arbeiten)
zahlen = [3, 7, 2, 9]



# Aufgabe 1.3
# Berechne die Summe der Liste mit while
zahlen = [1, 2, 3, 4, 5]



# =========================
# Teil 2: Bedingungen steuern
# =========================

# Aufgabe 2.1
# Gib Zahlen von 0 bis 9 aus



# Aufgabe 2.2
# Gib nur gerade Zahlen bis 20 aus



# Aufgabe 2.3
# Zähle rückwärts von 10 bis 1



# =========================
# Teil 3: Benutzerinteraktion
# =========================

# Aufgabe 3.1
# Frage den Benutzer so lange nach einer Zahl,
# bis er die Zahl 0 eingibt



# Aufgabe 3.2
# Summiere alle eingegebenen Zahlen,
# bis 0 eingegeben wird



# Aufgabe 3.3
# Passwort-Abfrage (einfach)
# Der Benutzer muss "python" eingeben



# =========================
# Teil 4: break und continue
# =========================

# Aufgabe 4.1
# Beende die Schleife, wenn Zahl 5 erreicht wird



# Aufgabe 4.2
# Überspringe alle ungeraden Zahlen von 1 bis 10



# =========================
# Teil 5: Kombinierte Aufgaben
# =========================

# Aufgabe 5.1
# Rate-Spiel
# Eine feste Zahl (z.B. 7) soll erraten werden



# Aufgabe 5.2
# Fakultät berechnen (z.B. 5! = 120)



# Aufgabe 5.3
# Zähle Ziffern in einer Zahl
zahl = 12345



# Aufgabe 5.4
# Drehe eine Zahl um (123 -> 321)



# =========================
# BONUS
# =========================

# Aufgabe 6
# Endlosschleife mit Menü
# (1) Hallo ausgeben
# (2) Programm beenden



# ======================================================
# ================== MUSTERLÖSUNGEN =====================
# ======================================================

# Aufgabe 1.1
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Aufgabe 1.2
# i = 0
# while i < len(zahlen):
#     print(zahlen[i])
#     i += 1

# Aufgabe 1.3
# i = 0
# summe = 0
# while i < len(zahlen):
#     summe += zahlen[i]
#     i += 1
# print(summe)

# Aufgabe 2.1
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# Aufgabe 2.2
# i = 0
# while i <= 20:
#     print(i)
#     i += 2

# Aufgabe 2.3
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# Aufgabe 3.1
# zahl = int(input("Zahl eingeben (0 zum Beenden): "))
# while zahl != 0:
#     zahl = int(input("Zahl eingeben (0 zum Beenden): "))

# Aufgabe 3.2
# summe = 0
# zahl = int(input("Zahl eingeben (0 zum Beenden): "))
# while zahl != 0:
#     summe += zahl
#     zahl = int(input("Zahl eingeben (0 zum Beenden): "))
# print(summe)

# Aufgabe 3.3
# pw = ""
# while pw != "python":
#     pw = input("Passwort eingeben: ")
# print("Zugriff erlaubt")

# Aufgabe 4.1
# i = 1
# while True:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# Aufgabe 4.2
# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# Aufgabe 5.1
# ziel = 7
# tipp = -1
# while tipp != ziel:
#     tipp = int(input("Rate die Zahl: "))
# print("Richtig!")

# Aufgabe 5.2
# n = 5
# fak = 1
# while n > 0:
#     fak *= n
#     n -= 1
# print(fak)

# Aufgabe 5.3
# count = 0
# while zahl > 0:
#     zahl //= 10
#     count += 1
# print(count)

# Aufgabe 5.4
# result = 0
# while zahl > 0:
#     result = result * 10 + zahl % 10
#     zahl //= 10
# print(result)

# Aufgabe 6
#while True:
#     print("1: Hallo")
#     print("2: Beenden")
#     wahl = input("Auswahl: ")
#     if wahl == "1":
# print("Hallo!")
#     elif wahl == "2":
#         break
