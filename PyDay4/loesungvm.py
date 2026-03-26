# Zähler für die eingegebenen Zahlen
anzahl = 0

while True:
    eingabe = input("Bitte eine Zahl eingeben (0 zum Beenden): ")
    
    # Prüfen, ob die Eingabe eine gültige Zahl ist
    if not eingabe.lstrip("-").isdigit():
        print("Ungültige Eingabe, bitte eine ganze Zahl eingeben.")
        continue  # Überspringt diese Schleifenrunde

    zahl = int(eingabe)
    
    # Prüfen, ob die Eingabe 0 ist, um das Programm zu beenden
    if zahl == 0:
        break

    # Zähler erhöhen
    anzahl += 1

    # Gerade oder ungerade prüfen
    if zahl % 2 == 0:
        print("Die Zahl ist gerade.")
    else:
        print("Die Zahl ist ungerade.")

    # Positiv oder negativ prüfen
    if zahl > 0:
        print("Die Zahl ist positiv.")
    elif zahl < 0:
        print("Die Zahl ist negativ.")

# Gesamte Anzahl ausgeben
print(f"Insgesamt wurden {anzahl} Zahlen eingegeben.")