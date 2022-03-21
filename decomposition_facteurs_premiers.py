def liste_facteurs(entier):
    facteurs = []
    diviseur = 2
    variable = entier
    while diviseur <= variable and diviseur <= (entier // 2) :
        while variable % diviseur == 0 :
            facteurs.append(diviseur)
            variable = variable // diviseur
        diviseur += 1
    if facteurs == [] :
        facteurs = [entier]
    return facteurs

def occurrence_liste(liste):
    liste1 = list(liste)
    from collections import Counter
    return Counter(liste1)

def decomposition(entier):
    occurrence_facteur = occurrence_liste(liste_facteurs(entier))
    decomposition = ""
    for facteur in occurrence_facteur :
        if occurrence_facteur[facteur] == 1 :
            produit = str(facteur)
        else :
            produit = str(facteur) + "^" + str(occurrence_facteur[facteur])
        if decomposition == "" :
            decomposition = produit
        else :
            decomposition = decomposition + " x " + produit
    decomposition = str(entier) + " = " + decomposition
    return decomposition

if __name__=="__main__" :
    entier = int(input("Entier a decomposer : "))
    print(decomposition(entier))
