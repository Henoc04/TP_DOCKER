try:
    # Demander à l'utilisateur d'entrer le premier nombre
    nombre1 = float(input("Entrez le premier nombre : "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")
    exit(1)

try:
    # Demander à l'utilisateur d'entrer le deuxième nombre
    nombre2 = float(input("Entrez le deuxième nombre : "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")
    exit(1)

# Additionner les deux nombres
somme = nombre1 + nombre2

# Afficher le résultat
print(f"La somme de {nombre1} et {nombre2} est : {somme}")
