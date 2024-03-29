# Fonction gérant les retours à l'écran du Problème 1
def affichage_nom_num():
    nom = "David Normandin"
    num = "#2295349"
    print("1. Voir le nom de l'étudiant")
    print("2. Voir le numéro de dossier de l'étudiant")
    sel = int(input("Choix: "))
    if sel == 1:
        print(nom)
    else:
        print(num)

# Fonction gérant les retours à l'écran du Problème 2
def puissance(base_entrante, exposant_entrant):
    if base_entrante < 0 or exposant_entrant < 0:
        print("Aucun chiffre ne doit être négatif")
    else: 
        print(base_entrante**exposant_entrant)

# Fonction gérant les retours à l'écran du Problème 3
def division_check():
    nombre = int(input("Entrez un nombre entier: "))
    if nombre % 2 == 0 and nombre % 3 == 0:
        print("Votre nombre est divisible par 2 et 3") 
    elif nombre % 2 == 0:
        print("Votre nombre est divisible par 2")
    elif nombre % 3 == 0:
        print("Votre nombre est divisible par 3")
    else:
        print("Votre nombre n'est pas divisible par 2 ou par 3")

# Fonction gérant les retours à l'écran du Problème 4
def cinquante_quand():
    fete = int(input("Entrez votre année de fête: "))
    if fete <= 1972:
        print(f"Vous avez eu 50 ans en {fete+50}")
    else: 
        print(f"Vous aurez 50 ans en {fete+50}")

# Fonction gérant le retour à l'écran du Problème 5
def operations(float1_entrant, float2_entrant, float3_entrant):
    print(f"{float1_entrant*float2_entrant/float3_entrant:.3f}")

# Fonction gérant le retour à l'écran du Problème 6
def phrase():
    plat = input("Entrez votre plat préféré: ")
    pays = input("Entrez votre pays préféré: ")
    futur = input("Entrez une année future: ")
    print(f"Vous aurez l'opportunité de manger de la/du {plat}, lorsque vous visiterez le/la/l' {pays} en {futur}")

def menu():
    exit = False
    while not exit:
        sel = -1
        while not 0 < sel <= 7:
            print("\nMenu de sélection du programme")
            print("1. Voir exécution du Problème 1")
            print("2. Voir exécution du Problème 2")
            print("3. Voir exécution du Problème 3")
            print("4. Voir exécution du Problème 4")
            print("5. Voir exécution du Problème 5")
            print("6. Voir exécution du Problème 6")
            print("7. Terminer programme")
            sel = int(input("Choix: "))
        if sel == 1:
            affichage_nom_num()
        elif sel == 2:
            base = int(input("Entrez le chiffre de la base: "))
            exp = int(input("Entrez le chiffre de l'exposant: "))
            puissance(base, exp)
        elif sel == 3:
            division_check()
        elif sel == 4:
            cinquante_quand()
        elif sel == 5:
            float1 = float(input("Entrez un chiffre décimal: "))
            float2 = float(input("Entrez un chiffre décimal: "))
            float3 = float(input("Entrez un chiffre décimal: "))
            operations(float1, float2, float3)
        elif sel == 6:
            phrase()
        else:
            exit = True


menu()



