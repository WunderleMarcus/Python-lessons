role = input("Rolle: ").lower()

if role == "admin":
    print("Alles erlaubt")
elif role == "user":
    print("Teilweise erlaubt") 
elif role == "gast":
    print("Nur Lesezugriff")
else:
    print("Unbekannte Rolle") 