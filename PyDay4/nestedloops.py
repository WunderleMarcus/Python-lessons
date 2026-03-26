# ============================================
# NESTED LOOPS (Verschachtelte Schleifen)
# ============================================

# Grundidee:
# Eine Schleife läuft innerhalb einer anderen Schleife

# --------------------------------------------
# Einfaches Beispiel
# --------------------------------------------

for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

# Erklärung:
# Für jeden Wert von i wird die innere Schleife komplett durchlaufen


# --------------------------------------------
# Praxisbeispiel: Online-Shop
# --------------------------------------------

produkte = ["T-Shirt", "Hoodie", "Sneaker"]
farben = ["Rot", "Blau"]

for produkt in produkte:
    for farbe in farben:
        print(produkt, "-", farbe)

# Erklärung:
# Jedes Produkt wird mit jeder Farbe kombiniert


# --------------------------------------------
# Praxisbeispiel: 2D-Daten (Matrix)
# --------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for zeile in matrix:
    for wert in zeile:
        print("Wert:", wert)

# Erklärung:
# Wir gehen jede Zeile durch und dann jedes Element in der Zeile


# --------------------------------------------
# Kombinationen erzeugen
# --------------------------------------------

for a in [1, 2]:
    for b in [3, 4]:
        print("Paar:", a, b)

# Erklärung:
# Alle möglichen Kombinationen werden erzeugt


# --------------------------------------------
# Achtung: Laufzeit
# --------------------------------------------

# Zwei Schleifen bedeuten:
# Anzahl Durchläufe = n * m
# Kann bei großen Datenmengen langsam werden!


# ============================================
# Kombination: List Comprehension + Nested Loop
# ============================================

pairs = [(i, j) for i in range(3) for j in range(2)]

print("Paare:", pairs)

# Erklärung:
# Kurzform einer verschachtelten Schleife
# Reihenfolge entspricht normalen nested loops


# ============================================
# MERKSÄTZE
# ============================================

# List Comprehension:
# → Schnell Listen erzeugen

# Nested Loops:
# → Kombinationen und Strukturen durchlaufen