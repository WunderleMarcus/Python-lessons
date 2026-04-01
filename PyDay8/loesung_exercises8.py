# ===============================
# LISTS
# ===============================
"""
# Leichte Aufgabe: jede Zahl verdoppeln
print("List easy:")
for num in numbers_list_easy:
    print(num * 2, end=" ")
print("\n")  # Zeilenumbruch

# Anspruchsvolle Aufgabe: gerade Zahlen quadrieren, ungerade entfernen
print("List hard:")
numbers_processed = []
for num in numbers_list_hard:
    if num % 2 == 0:  # nur gerade Zahlen
        numbers_processed.append(num ** 2)  # quadriere gerade Zahlen
print(numbers_processed)
print("\n")

# ===============================
# SETS
# ===============================

# Leichte Aufgabe: alle Elemente in Großbuchstaben
print("Set easy:")
for fruit in fruits_set_easy:
    print(fruit.upper())
print("\n")

# Anspruchsvolle Aufgabe: gerade Zahlen multiplizieren und neues Set bilden
print("Set hard:")
new_set = {num * 10 for num in numbers_set_hard if num % 2 == 0}
print(new_set)
print("\n")

# ===============================
# DICTIONARIES
# ===============================

# Leichte Aufgabe: Schlüssel und Werte ausgeben
print("Dict easy:")
for key, value in person_dict_easy.items():
    print(f"{key}: {value}")
print("\n")

# Anspruchsvolle Aufgabe: Studenten mit Note besser als 2.0
print("Dict hard:")
good_students = {}
for student, grade in grades_dict_hard.items():
    if grade < 2.0:
        good_students[student] = grade
count = len(good_students)
print(good_students)
print("Count =", count)
print("\n")

# ===============================
# TUPLES
# ===============================

# Leichte Aufgabe: Summe aller Werte
print("Tuple easy:")
total = sum(coordinates_tuple_easy)
print("Sum:", total)
print("\n")

# Anspruchsvolle Aufgabe: Namen extrahieren, Durchschnittsalter berechnen
print("Tuple hard:")
names = []
ages = []
for name, age in data_tuple_hard:
    names.append(name)
    ages.append(age)
average_age = sum(ages) / len(ages)
print("Names:", names)
print("Average age:", round(average_age, 2))

"""