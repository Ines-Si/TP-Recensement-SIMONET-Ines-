import csv 
donnee_2008 = []
donnee_2016 = []
donnee_2023 = []
donnee_2021 = [] 
with open('donnees_2008.csv',newline="") as donne2008:
    reader=csv.reader(donne2008,delimiter=',')
    for row in reader:
        donnee_2008.append(row)
print (donnee_2008) 

with open('donnees_2016.csv',newline="") as donne2016:
    reader=csv.reader(donne2016,delimiter=',')
    for row in reader:
        donnee_2016.append(row)
print (donnee_2016) 

with open('donnees_2023.csv',newline="") as donne2023:
    reader=csv.reader(donne2023,delimiter=',')
    for row in reader:
        donnee_2023.append(row)
print (donnee_2023)

with open('donnes_2021.csv',newline="") as donne2021:
    reader=csv.reader(donne2021,delimiter=';')
    for row in reader:
        donnee_2021.append(row)
print (donnee_2021) 

