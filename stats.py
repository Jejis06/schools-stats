import json
import matplotlib.pyplot as plt



names = []
Pwybory = []
Nwybory = []

schools = []

with open("db.json","rb") as f:
    data = json.load(f)
    f.close()


cpw = 0
cnw = 0
for school in data:
    names.append(school["name"])
    pw = 0
    nw = 0
    for Class in school["classes"]:
        pw += Class["Pwybor"]
        nw += Class["Nwybor"]
    Pwybory.append(pw)
    Nwybory.append(nw)

    cpw += pw
    cnw += nw

    schools.append({
        'name':school['name'],
        'pw':pw,
        'nw':nw,
    })


schools = sorted(schools, key = lambda x : -x['pw'])

print(f"kandydujacych : {cpw} :\n\n\n")
j = 1
print("\t\t\t\tStatystyki Pierwszy wybór : ") 
print()
for i in schools:
    print(f"{j}\t{i['name']:120s}{(i['pw']/cpw):%}")
    j += 1

j = 1
schools = sorted(schools, key = lambda x : -x['nw'])
print("\n\n\n\n\t\t\t\tStatystyki kolejne wybory : ") 
print()
for i in schools:
    print(f"{j}\t{i['name']:120s}{(i['nw']/cnw):%}")
    j += 1
        


    

plt.pie(Pwybory, labels = names, autopct='%1.1f%%',  pctdistance=1.1, labeldistance=1.2)
plt.show()
plt.pie(Nwybory, labels = names, autopct='%1.1f%%',  pctdistance=1.1, labeldistance=1.2)
plt.show()
