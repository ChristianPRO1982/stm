import pandas as pd
import os


mots = pd.read_csv('./liste_de_mots.csv')
mots = mots.dropna(subset=['MotsSA'])


#INIT
l_rouges = {}
os.system('clear')
lettres = input('début du jeu : ')
lettres = lettres.lower()
for index, lettre in enumerate(lettres):
    l_rouges[index] = lettre
for index in range(1, len(lettres)):
    mots[index] = mots['MotsSA'].str[index]


#JEU
while True:
    os.system('clear')

    print('--------------------')
    str_match = "".join(l_rouges.values())
    print(str_match.upper())
    print('--------------------')
    print()

    mots = mots[mots['MotsSA'].str.match(f'^{str_match}$')]
    mots = mots.sort_values('Poids',ascending=False)

    print(mots)
    print()
    print("<><><><><>")
    print()

    mot_teste = input("mot testé : ")
    mot_teste = mot_teste.lower()
    if mot_teste == "": break;
    if mot_teste == "1":
        mot = mots.iloc[0]
        mot_teste = mot['MotsSA']
    print("mot testé :", mot_teste)

    resultats = input("résultat  : ")
    if resultats == "": break;

    resultats = resultats.upper()
    for index in range(1, len(mot_teste)):
        if resultats[index] == 'R':
            l_rouges[index] = mot_teste[index]
        
        if resultats[index] == 'B':
            partout = True
            for index2 in range(1, len(mot_teste)):
                if mot_teste[index] == mot_teste[index2] and resultats[index2] == 'J':
                    partout = False
            
            if partout == True:
                for index2 in range(1, len(mot_teste)):
                    mots = mots[mots[index2] != mot_teste[index]]
            else:
                mots = mots[mots[index] != mot_teste[index]]

        if resultats[index] == 'J':
            mots = mots[mots[index] != mot_teste[index]]

print('FIN')