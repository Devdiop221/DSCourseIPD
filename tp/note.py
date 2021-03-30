liste = []
while True:
    note = float(input("Saisir une note ou -1 pour quitter: "))
    if note==-1: break
    liste.append(note)
    print ("Le nombre de note entré: ",len(liste))
    print ("La note la plus elevée est: ",max(liste))
    print ("La note la plus basse est: ",min(liste))
    print("La moyenne de toute les notes est ", sum(liste)/float(len(liste)))
