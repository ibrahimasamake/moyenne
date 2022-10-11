
def demandeNote() :   # demande note
        note = input(": ")
        try:
            noteInt = int(note)
        except  ValueError:
            print("erreur Vous devez entre un nombre")
            return demandeNote()
        return noteInt

def verifieNote(): #verifie si note superieur a 20
    liste =[]
    for i in range(1, 4):
        print(f"Entre note {i}")
        note = demandeNote()
        while note > 20:
            print("erreur nombre superieur 20")
            note = demandeNote()
        liste.append(note)
    return liste

def moyenneGeneral(list): # calcul de la moyenne
    somme = 0
    for i  in range(0,len(list)):
        somme += list[i]
    moyenne = somme/len(list)
    return moyenne

def trieAppreciation(moyenne) :
    moyenneInt = int(moyenne)
    if moyenneInt >= 16:
        print("Tres bien")
    elif moyenneInt >= 14 :
        print("bien")
    elif moyenneInt >= 12 :
        print("Assez bien")
    elif moyenneInt >= 10 :
        print("passable")
    elif moyenneInt < 10:
        print("insuffisant")


listNote = verifieNote()
moyenne = moyenneGeneral(listNote)
print(f"la moyenne est = ",str(round(moyenne,2))) #affichage de la moyenne
trieAppreciation(moyenne)
