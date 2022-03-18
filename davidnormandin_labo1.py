#Problème 1:
#Écrire un programme affichant un menu offrant les options suivantes à l'utilisateur:
#1. Afficher le nom
#2. Afficher le numéro d'étudiant
#Votre programme doit soit afficher votre propre nom à l'écran si l'utilisateur choisi l'option 1, si l'option 2 est choisie vous devez 
#afficher votre numéro d'étudiant, sinon vous devez indiquer à l'utilisateur que son choix n'est pas valide.

#Problème 2:
#Créer un programme contenant une fonction prenant 2 nombres entiers (une base et un exposant). Vérifier que la base et l'exposant ne soient 
#pas négatifs et retourner le résultat de la puissance.

#Problème 3:
#Créer un programme demandant à un utilisateur d'entrer un nombre entier et afficher à la console si ce nombre est divisible par 2 ou 3.

#Problème 4:
#Créer une fonction demandant à l'utilisateur d'entrer son année de fête et afficher à l'écran en quel année l'utilisateur a eu 50 ans ou aura 
#50 ans.

#Problème 5:
#Créer une fonction prenant 3 floats, effectuant la multiplication des deux premiers et divisant le résultat par le troisième. Imprimer le 
#résultat de sorte qu'il n'y ait seulement 3 chiffres après la virgule.

#Problème 6:
#Créer un programme demandant à l'utilisateur d'entrer son plat préféré, son pays préféré et une année future et affichez la phrase suivante : 
#Vous aurez l'opportunité de manger «le plat préféré, lorsque vous visiterai «le pays préféré» en «l'année future».


def appels_fonctions():
    return 

def affichage_nom_num():
    nom = "David Normandin"
    num = "#2295349"
    user_input = int(input("Choissisez une des 2 options suivantes: \n"
                            "1. Afficher le nom de l'étudiant \n"
                            "2. Afficher le  numéro d'étudiant \n"))
    if user_input == 1:
        print(nom)
    elif user_input == 2:
        print(num)
    else:
        print("Votre choix n'est pas valide")
    return

def puissance(base_entrante, exposant_entrant):
    if base_entrante < 0 or exposant_entrant < 0:
        print("Aucun chiffre ne doit être négatif")
    else: 
        print(base_entrante**exposant_entrant)
    return 

def division_check():
    nombre = int(input("Entrez un nombre entier"))
    if nombre % 2 == 0 and nombre % 3 == 0:
        print("Votre nombre est divisible par 2 et 3") 
    elif nombre % 2 == 0:
        print("Votre nombre est divisible par 2")
    elif nombre % 3 == 0:
        print("Votre nombre est divisible par 3")
    else:
        print("Votre nombre n'est pas divisible par 2 ou par 3")
    return 

def cinquante_quand():
    fete = int(input("Entrez votre année de fête"))
    if fete <= 1972:
        print(f"Vous avez eu 50 ans en {fete+50}")
    else: 
        print(f"Vous aurez 50 ans en {fete+50}")
    return 

def operations(float1_entrant, float2_entrant, float3_entrant):
    return print(f"{float1_entrant*float2_entrant/float3_entrant:.3f}")

def phrase():
    plat = input("Entrez votre plat préféré")
    pays = input("Entrez votre pays préféré")
    futur = input("Entrez une année future")
    return print(f"Vous aurez l'opportunité de manger de la/du {plat}, lorsque vous visiterez le/la/l' {pays} en {futur}")


appels_fonctions()



