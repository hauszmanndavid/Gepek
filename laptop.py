file = open("gep.txt","r", encoding="UTF-8")
file2 = open("gep.txt","w")

Llaptop = []

for i in file2:
    if(i[-1]=='\n'):
        Llaptop.append(i[:-1].split('\t'))
    else:
        Llaptop.append(i.split('\t'))
  
del Llaptop[0]

#1



#2



#3
keres = 0

for i in range(len(Llaptop)):
    if(keres == (Llaptop[i][3])):
        print("Van 1TB gép")
    else:
        print("Nincs 1TB gép")

#4
colos = 0

for colos in range(Llaptop):
    colos == (Llaptop[i][1])
    
print("A legnagyobb colos kijelző: ")


#5
giga = 0

for i in range(len(Llaptop)):
    (giga.append(Llaptop[i][2]))

print("Ennyi 1GB: ", giga.count, "Ennyi 2GB: ", giga.count,  "Ennyi 3GB: ", giga.count, "Ennyi 4GB: ", giga.count)


