nbr=0
n=0
i=0
note=[]
while n<=20:
    n=float(input("Entrer une note : "))

    if n>=20 and n<=20:
        note.insert(i,n)
        i+=1
    else:

            break
    nbr+=1
moy=sum(note)/nbr
print("La listes des notes des eleves est : ",note)
print("Le nombre de note de cette liste est : ",nbr)
print("La note minimal de cette liste est : ", min)
print("La note maximal de cette liste est : ", max)
print("La moyeene des notes est : ", moy)
