file = open("gep2.txt","r", encoding="UTF-8")


Llaptop = []

for i in file:
    if(i[-1]=='\n'):
        Llaptop.append(i[:-1].split('\t'))
    else:
        Llaptop.append(i.split('\t'))
  
del Llaptop[0]

#1



#2
osszeg=0
for i in range(len(Llaptop)):
   osszeg += int(Llaptop[i][2])
   
print("Átlag ennyi merevlemez van a gépeken: ", round(osszeg/len(Llaptop),2))


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
egygb = []
kettogb = []
haromgb = []
negygb = []

for i in range(len(Llaptop)):
    if list[i][2] == 1024:
        egygb.append(list[i][2])
    elif list[i][2] ==2048:
        kettogb.append(list[i][2])
    elif list[i][2] ==3072:
        haromgb.append(list[i][2])
    elif list[i][2] ==4096:
        negygb.append(list[i][2])

print(len(egygb),len(kettogb),len(haromgb),len(negygb))



