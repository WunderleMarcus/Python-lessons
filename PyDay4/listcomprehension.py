
# --------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------

# Grundidee:
# List Comprehension ist eine kurze Schreibweise,
# um Listen basierend auf einer Schleife zu erzeugen.

# Allgemeiner Aufbau:
# [ausdruck for element in sequenz]

# --------------------------------------------
# Einfaches Beispiel
# --------------------------------------------

# Wir berechnen Quadratzahlen von 0 bis 4
quadrate = [x**2 for x in range(5)]

print("Quadrate:", quadrate)

# Erklärung:
# x läuft durch range(5) → 0,1,2,3,4
# x**2 berechnet das Quadrat
# Ergebnisse werden direkt in die Liste geschrieben


# --------------------------------------------
# Vergleich mit normaler Schleife
# --------------------------------------------

quadrate_alt = []
for x in range(5):
    quadrate_alt.append(x**2)

print("Quadrate (klassisch):", quadrate_alt)

# Nachteil:
# - mehr Code
# - weniger kompakt


# --------------------------------------------
# List Comprehension mit Bedingung (Filter)
# --------------------------------------------

# Nur gerade Zahlen
gerade = [x for x in range(10) if x % 2 == 0]

print("Gerade Zahlen:", gerade)

# Erklärung:
# Nur Werte werden übernommen, wenn die Bedingung True ist


# --------------------------------------------
# Praxisbeispiel: Daten umformen
# --------------------------------------------

# Benutzernamen in Kleinbuchstaben umwandeln
usernames = ["Max", "ANNA", "john"]

lower_usernames = [name.lower() for name in usernames]

print("Usernames klein:", lower_usernames)


# --------------------------------------------
# Hinweis
# --------------------------------------------

# List Comprehension ist praktisch,
# aber bei sehr komplexen Ausdrücken wird der Code schwer lesbar!

