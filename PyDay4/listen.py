"""
fruechte = ["Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere"]
for frucht in fruechte:
    print(frucht)
    """
    
#for i in range(1, 11, 2):
#    print(i)


#namen = ["Alice", "Bob", "Charlie", "David", "Eve"]
#for index, name in enumerate(namen):
#     print(index, "\t", name)
"""    
    
for i in range(10):
    if i == 2:
        continue
    print(i) 
"""
zahlen = [1, 3, 5, 7, 9]
for zahl in zahlen:
    if zahl == 2:
        break
else:  
    print("Zahl nicht gefunden")