liste=["A","R","A","W","W","A","W","A","R","W","W","R","A","G","A","R"]
compteur=0
compteur2=0
compteur3=0
for lettre in liste:
    if lettre== "A":
        compteur= compteur +1
    elif lettre=="R":
        compteur2=compteur2 +1
    elif lettre=="W":
        compteur3=compteur3 +1

print ("il y a", compteur, "A")
print ("il y a", compteur2 ,"R")
print ("il y a", compteur3 , "W")