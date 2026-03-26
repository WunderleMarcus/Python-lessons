while True:
    eingabe = input("\nDeine Zahl: ").strip()

    try:
        zahl = int(eingabe)  # Versuch, die Eingabe in eine Zahl umzuwandeln
    except ValueError:
        print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")
        continue

    if zahl == 0:
        print("Programm wird beendet.")
        break
    else:
        print(f"Du hast die Zahl {zahl} eingegeben.")