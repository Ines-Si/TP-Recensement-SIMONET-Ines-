import csv 
donnee_2008 = []
donnee_2016 = []
donnee_2023 = []


with open('donnees_2008.csv',newline="", encoding = "utf-8") as donne2008:
    reader=csv.reader(donne2008,delimiter=',')
    for row in reader:
        donnee_2008.append(row)


with open('donnees_2016.csv',newline="", encoding ="utf-8") as donne2016:
    reader=csv.reader(donne2016,delimiter=',')
    for row in reader:
        donnee_2016.append(row)

with open('donnees_2023.csv',newline="", encoding ="utf-8") as donne2023:
    reader=csv.reader(donne2023,delimiter=';')
    for row in reader:
        donnee_2023.append(row)


del donnee_2008[0]
del donnee_2016[0]
del donnee_2023[0]

ville_bourgogne_2008 = []

for row in donnee_2008:
    if "Bourgogne" in row :
        ville_bourgogne_2008.append([row[6], int(row[9])])

print ("ville bourgogne plus population ", ville_bourgogne_2008)
ville_bourgogne_2008.sort(key=lambda x: x[1]) 
ville_grande_pop_2008 = ville_bourgogne_2008[-10:]
print("Les 10 ville avec une grande population ", ville_grande_pop_2008)


ville_bourgogne_2016 = []
for row in donnee_2016:
    if "Bourgogne-Franche-Comté" in row: 
        ville_bourgogne_2016.append([row[6], int(row[9])])
print ("ville bourgogne plus population ", ville_bourgogne_2016)
ville_bourgogne_2016.sort(key=lambda x: x[1])  
ville_grande_pop_2016 = ville_bourgogne_2016[-10:]
print("Les 10 villes avec grande population :", ville_grande_pop_2016)

ville_bourgogne_2023 = []
for row in donnee_2023:
    if "Bourgogne-Franche-Comté" in row: 
        ville_bourgogne_2023.append([row[7], int(row[10])])
print ("ville bourgogne plus population ", ville_bourgogne_2023)
ville_bourgogne_2023.sort(key=lambda x: x[1])  
ville_grande_pop_2023 = ville_bourgogne_2023[-10:]
print("Les 10 villes avec grande population :", ville_grande_pop_2023)

