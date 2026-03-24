#Praktisches Recap von heute: Datentypen, Umwandeln von Datentypen, 
# Rechnen mit Datentypen, Zugriff auf Elemente

# Aufgabe 1 Datentypen erkennen mit type()
"""
a = 10
b = 4.14
c = "Hallo Teilnehmer"
d = True
e = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

"""


"""

# Aufgabe 2 Datentypen umwandeln

x = "25"    # in einen Integer umwandeln
y = 4.8     # in einen Integer umwandeln
z = 10      # in einen String umwandeln

print(type(x))
print(type(y))
print(type(z))

x = int(x)
y = int(y)
z = str(z)

print(type(x))
print(type(y))
print(type(z))


"""

"""

a = 5
b = "10"


# Aufgabe 3 Rechnen mit Datentypen: 
     # Was passiert hier?

    # Lösung:
print(a + int(b))  
print(str(a) + b) 




"""





"""

#Aufgabe 4 Zugriff auf Elemente

text = "Python"
liste = ["P", "y", "t", "h", "o", "n"]

# Aufgabe:
# Greife auf das 3. Element zu und gib es aus

print(text[2])
print(liste[2])

"""

#Kombinierte Strings und Listen Aufgabe:

# Aufgabe:
# Eingabe von Name und Alter
# Ausgabe: "Hallo Max, in 5 Jahren bist du 30 Jahre alt."

name = input("Name: ")
alter = int(input("alter: "))

print(f"Hallo {name}, in 5 Jahren bist du {alter + 5} Jahre alt.")