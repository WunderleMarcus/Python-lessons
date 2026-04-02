# ===============================
# Python Übungsprogramm: Funktionen
# ===============================

# -------------------------------
# Übung 1: Deine erste Funktion
# -------------------------------

def guten_morgen():
    """Gibt eine Morgenbegrüßung aus."""
    print("Guten Morgen!")
    print("Ich wünsche dir einen schönen Tag!")

def guten_abend():
    """Gibt eine Abendbegrüßung aus."""
    print("Guten Abend!")
    print("Ich hoffe, du hattest einen guten Tag!")

# Aufruf der Begrüßungen
print("=== Übung 1: Begrüßungen ===")
guten_morgen()
guten_abend()


# -------------------------------
# Übung 2: Funktionen mit Parametern
# -------------------------------

def stelle_vor(name, alter):
    """Stellt eine Person mit Name und Alter vor."""
    print(f"Ich bin {name} und ich bin {alter} Jahre alt.")

def rechne(zahl1, zahl2):
    """Berechnet Summe, Differenz und Produkt von zwei Zahlen."""
    return {
        "summe": zahl1 + zahl2,
        "differenz": zahl1 - zahl2,
        "produkt": zahl1 * zahl2
    }

print("\n=== Übung 2: Parameter ===")
stelle_vor("Anna", 25)
stelle_vor("Ben", 30)

ergebnis = rechne(10, 5)
print(f"10 + 5 = {ergebnis['summe']}")
print(f"10 - 5 = {ergebnis['differenz']}")
print(f"10 * 5 = {ergebnis['produkt']}")


# -------------------------------
# Übung 3: Funktionen mit Return
# -------------------------------

def quadrat(zahl):
    """Gibt das Quadrat einer Zahl zurück."""
    return zahl * zahl

def verdopple(zahl):
    """Gibt das Doppelte einer Zahl zurück."""
    return zahl * 2

def berechne_preis(netto, steuersatz):
    """Berechnet Bruttopreis inkl. Steuer, gerundet auf 2 Dezimalstellen."""
    brutto = netto * (1 + steuersatz)
    return round(brutto, 2)

def teile_mit_rest(dividend, divisor):
    """Gibt das Ergebnis und den Rest einer Division zurück."""
    return dividend // divisor, dividend % divisor

print("\n=== Übung 3: Return-Werte ===")
x = 7
print(f"{x}² = {quadrat(x)}")
print(f"{x} verdoppelt = {verdopple(x)}")

netto = 100
steuer = 0.19
print(f"Bruttopreis von {netto} € bei {steuer*100}% Steuer: {berechne_preis(netto, steuer)} €")

quotient, rest = teile_mit_rest(17, 5)
print(f"17 geteilt durch 5 = {quotient} Rest {rest}")


# -------------------------------
# Übung 4: Parameter-Varianten
# -------------------------------

def erstelle_profil(name, alter, stadt, beruf):
    """Erstellt ein Benutzerprofil aus allen Parametern."""
    profil = f"""
--- BENUTZERPROFIL ---
Name:   {name}
Alter:  {alter}
Stadt:  {stadt}
Beruf:  {beruf}
----------------------
"""
    print(profil)

def berechne_rabatt(preis, rabatt=10):
    """Berechnet den neuen Preis nach Rabatt."""
    neuer_preis = preis * (1 - rabatt/100)
    return round(neuer_preis, 2)

def erstelle_nachricht(text, absender="System", wichtig=False):
    """Erstellt eine formatierte Nachricht, optional wichtig."""
    if wichtig:
        return f"!!! WICHTIG !!! [{absender}]: {text}"
    return f"[{absender}]: {text}"

print("\n=== Übung 4: Parameter-Varianten ===")
erstelle_profil("Anna Müller", 28, "Berlin", "Entwicklerin")
erstelle_profil(beruf="Designer", name="Ben Schmidt", stadt="Hamburg", alter=32)

preis = 99.99
print(f"Preis mit Standard-Rabatt: {berechne_rabatt(preis)} €")
print(f"Preis mit 20% Rabatt: {berechne_rabatt(preis, 20)} €")

print(erstelle_nachricht("Server läuft normal"))
print(erstelle_nachricht("Backup abgeschlossen", absender="Backup-Service"))
print(erstelle_nachricht("Wartung in 10 Minuten!", absender="Admin", wichtig=True))


# -------------------------------
# Übung 5: Scope verstehen
# -------------------------------

kontostand = 1000  # Globale Variable

def zeige_kontostand():
    """Gibt den aktuellen Kontostand aus."""
    print(f"Aktueller Kontostand: {kontostand} €")

def pruefe_betrag(betrag):
    """Prüft, ob ein Betrag verfügbar ist."""
    if betrag <= kontostand:
        return "Betrag verfügbar"
    else:
        return "Nicht genug Guthaben"

def simuliere_abzug(betrag):
    """Simuliert Abzug lokal, ohne den globalen Kontostand zu ändern."""
    neuer_kontostand = kontostand - betrag
    print(f"Wenn wir {betrag} € abziehen würden, wäre der Kontostand: {neuer_kontostand} €")

print("\n=== Übung 5: Scope ===")
zeige_kontostand()
print(pruefe_betrag(300))
print(pruefe_betrag(1500))
simuliere_abzug(300)
zeige_kontostand()


# -------------------------------
# Übung 6: Text-Verarbeitung (Fortgeschritten)
# -------------------------------

def bereite_text_vor(text):
    """Entfernt Leerzeichen und formatiert jeden Wortanfang groß."""
    return text.strip().title()

def ersetze_zeichen(text, alt, neu):
    """Ersetzt Teile eines Strings."""
    return text.replace(alt, neu)

def teile_text(text, trenner=" "):
    """Teilt einen Text in eine Liste auf Basis eines Trenners."""
    return text.split(trenner)

print("\n=== Übung 6: Text-Verarbeitung ===")
text = "  python ist toll  "
text_vorbereitet = bereite_text_vor(text)
print(f"Vorbereitet: '{text_vorbereitet}'")

text_ersetzt = ersetze_zeichen(text_vorbereitet, "Python", "Java")
print(f"Ersetzt: '{text_ersetzt}'")

teile = teile_text(text_vorbereitet)
print(f"Geteilt: {teile}")