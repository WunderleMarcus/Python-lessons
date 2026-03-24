# Persönlicher Budget-Rechner
# Musterlösung mit ausführlichen Erklärungen

# -----------------------------
# Schritt 1: Begrüßung & Personalisierung
# -----------------------------
# input() liest Eingaben vom Benutzer (immer als String!)
name = input("Wie heißt du? ")
monat = input("Für welchen Monat möchtest du dein Budget planen? ")

# f-Strings erlauben einfache und lesbare String-Formatierung
print(f"\nHallo {name}! Willkommen zu deinem Budget-Rechner für den Monat {monat}.\n")

# -----------------------------
# Schritt 2: Einnahmen erfassen
# -----------------------------
# float() wandelt String-Eingaben in Fließkommazahlen um
gehalt = float(input("Monatliches Gehalt (€): "))
zusatz = float(input("Zusatzeinkommen (€): "))

# Berechnung der Gesamteinnahmen
gesamt_einnahmen = gehalt + zusatz
print(f"\nDeine Gesamteinnahmen betragen: {gesamt_einnahmen:.2f} €\n")

# -----------------------------
# Schritt 3: Ausgaben erfassen
# -----------------------------
miete = float(input("Miete (€): "))
lebensmittel = float(input("Lebensmittel (€): "))
transport = float(input("Transport (€): "))
freizeit = float(input("Freizeit (€): "))

# Berechnung der Gesamtausgaben
gesamt_ausgaben = miete + lebensmittel + transport + freizeit

# -----------------------------
# Schritt 4: Bilanz berechnen
# -----------------------------
# Differenz zwischen Einnahmen und Ausgaben
bilanz = gesamt_einnahmen - gesamt_ausgaben

# Sparquote in Prozent (nur sinnvoll, wenn Einnahmen > 0)
if gesamt_einnahmen > 0:
    sparquote = (bilanz / gesamt_einnahmen) * 100
else:
    sparquote = 0

# Bewertung der finanziellen Situation
if bilanz > 0:
    bewertung = "Du sparst Geld – sehr gut!"
elif bilanz == 0:
    bewertung = "Du gibst genau so viel aus wie du einnimmst."
else:
    bewertung = "Achtung: Du gibst mehr aus als du einnimmst!"

# -----------------------------
# Schritt 5: Schöne Ausgabe
# -----------------------------
print("\n" + "="*40)
print(f"Budgetübersicht für {name} ({monat})")
print("="*40)

print("\nEinnahmen:")
print(f"  Gehalt:           {gehalt:.2f} €")
print(f"  Zusatzeinkommen: {zusatz:.2f} €")
print(f"  -> Gesamt:       {gesamt_einnahmen:.2f} €")

print("\nAusgaben:")
print(f"  Miete:           {miete:.2f} €")
print(f"  Lebensmittel:    {lebensmittel:.2f} €")
print(f"  Transport:       {transport:.2f} €")
print(f"  Freizeit:        {freizeit:.2f} €")
print(f"  -> Gesamt:       {gesamt_ausgaben:.2f} €")

print("\nBilanz:")
print(f"  Ergebnis:        {bilanz:.2f} €")
print(f"  Sparquote:       {sparquote:.2f} %")

print("\nBewertung:")
print(f"  {bewertung}")

print("="*40)

# Ende des Programms

