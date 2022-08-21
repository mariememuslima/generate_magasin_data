from random import choice,randrange,randint
from faker import Faker
import datetime
import csv

def make_csv(file,row):
    with open (file,'a') as f:
        writer = csv.writer(f,delimiter=';')
        writer.writerow(row)
        f.close()

faker = Faker()
liste_files =["vendeur.csv", "produit.csv","client.csv","commandes.csv"]
surname_gender =[{'name':'aida','gender':'f'},{'name':'boury','gender':'f'},{'name':'adama','gender':'f'},{'name':'momar','gender':'m'},{'name':'massar','gender':'m'},{'name':'khadija','gender':'f'},{'name':'rashid','gender':'m'},{'name':'salma','gender':'f'},{'name':'sokhna','gender':'f'},{'name':'aliou','gender':'m'},{'name':'ibrahima','gender':'m'},{'name':'moustapha','gender':'m'},{'name':'marieme','gender':'f'},{'name':'awa','gender':'f'},{'name':'amy','gender':'f'},{'name':'babacar','gender':'m'}]
names = ['pouye','diop','fall','camara','diouf','diallo','gueye','toure','siby','bathily']
products=['cereal','riz','fromage','mixeur','panier','fruit','brocoli','eye-liner','stylos','farine','ble','yet','carotte']
area_code='+221'

for file in liste_files:
    # randoms products
    if (file.split('.')[0])=="produit":
       make_csv(file,['designataire','prix'])
       for _ in range(20):
          make_csv(file,[choice(products),"{}{}{}{}".format(*[randrange(10) for i in range(4)])])
    #    Datas for the seller
    elif (file.split('.')[0])=="vendeur":
        make_csv(file,['prenom','nom','telephone','sexe'])
        for _ in range(20):
            name=choice(surname_gender)
            make_csv(file,[name.get('name'),choice(names),"({}) {}{}-{}{}{}-{}{}-{}{}".format(area_code, *[randrange(10) for i in range(9)]),name.get('gender')])
    # Datas for costumers
    elif (file.split('.')[0])=="client":
        make_csv(file,['prenom','nom','telephone','sexe'])
        for _ in range(20):
            name=choice(surname_gender)
            make_csv(file,[name.get('name'),choice(names),"({}) {}{}-{}{}{}-{}{}-{}{}".format(area_code, *[randrange(10) for i in range(9)]),name.get('gender')])
    # commands informations
    else :
        make_csv(file,["client","vendeur",'date',"produits","quantite"])
        for _ in range(20):
            make_csv(file,[choice(surname_gender)["name"],choice(surname_gender)["name"],datetime.date(randint(2005,2021), randint(1,12),randint(1,28)),choice(products),randint(1,20)])
 
