import pandas as pd
import os


mots = pd.read_csv('./liste_de_mots.csv')
df_frequences_lettres = pd.read_csv('./frequences_lettres.csv')
mots = mots.dropna(subset=['MotsSA'])


def filtered_words(str_match: str)->list:
    return mots[mots['MotsSA'].str.match(f'^{str_match}$')]


def supprimer_mots_testes(liste_de_choix: list, mots_testes: list)->list:
    indices_a_supprimer = []

    for index, row in liste_de_choix.iterrows():
        mot = row['MotsSA']
        if mot in mots_testes:
            indices_a_supprimer.append(index)

    return indices_a_supprimer


def supprimer_mots_liste_bleue(liste_de_choix: list, l_bleues: list)->list:
    indices_a_supprimer = []

    for index, row in liste_de_choix.iterrows():
        mot = row['MotsSA']
        for lettre in l_bleues:
            if lettre in mot:
                indices_a_supprimer.append(index)

    return indices_a_supprimer


def supprimer_mots_liste_jaune(liste_de_choix: list, l_jaunes: list)->list:
    indices_a_supprimer = []

    for index, row in liste_de_choix.iterrows():
        mot = row['MotsSA']
        for pos, lettre in enumerate(mot):
            if lettre in l_jaunes[pos]:
                indices_a_supprimer.append(index)

    return indices_a_supprimer




#INIT
l_rouges = {}
l_jaunes = {}
l_bleues = []
os.system('clear')
lettres = input('début du jeu : ')
lettres = lettres.lower()
for index, lettre in enumerate(lettres):
    l_rouges[index] = lettre
    l_jaunes[index] = ''
nb_lettres = len(lettres)
mots_testes = []


#JEU
while True:
    os.system('clear')

    print('--------------------')
    str_match = "".join(l_rouges.values())
    print(str_match.upper())
    print('--------------------')
    print()

    liste_de_choix = filtered_words(str_match)
    liste_de_choix = liste_de_choix.drop(supprimer_mots_testes(liste_de_choix, mots_testes))
    liste_de_choix = liste_de_choix.drop(supprimer_mots_liste_bleue(liste_de_choix, l_bleues))
    liste_de_choix = liste_de_choix.drop(supprimer_mots_liste_jaune(liste_de_choix, l_jaunes))

    print(liste_de_choix)
    print("<><><><><>")
    print(l_jaunes.values(), l_bleues)

    mot_teste = input("mot testé : ")
    mot_teste = mot_teste.lower()
    if mot_teste == "": break;
    mots_testes.append(mot_teste)

    resultats = input("résultat : ")
    if resultats == "": break;
    resultats = resultats.upper()
    for index, resultat in enumerate(resultats):
        if resultat == 'R':
            l_rouges[index] = mot_teste[index]
        if resultat == 'J' and mot_teste[index] not in l_jaunes:
            l_jaunes[index] += mot_teste[index]
        if resultat == 'B' and mot_teste[index] not in l_bleues:
            if mot_teste[index] not in l_rouges.values() and mot_teste[index] not in l_jaunes.values():
                l_bleues.append(mot_teste[index])

print('FIN')