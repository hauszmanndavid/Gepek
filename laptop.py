file = ("gep.txt","r")

Llaptop = []

for i in file:
    if(i[-1]=='\n'):
        Llaptop.append(i[:-1].split('\t'))
    else:
        Llaptop.append(i[:-1].split('\t'))
  
del Llaptop[0]

#1



#2
osszeg=0
for i in range(len(Llaptop)):
   osszeg += int(Llaptop[i][3])

print("Átlag ennyi merevlemez van a gépeken: ", round(osszeg/len(Llaptop),2))


#3
'''keres = 0

for i in range(Llaptop):
    if(keres == (Llaptop[i][1])):
        print("Van 1TB gép")
    else:
        print("Nincs 1TB gép")

#4
colos = 0



#5
statisztika = 0

'''
