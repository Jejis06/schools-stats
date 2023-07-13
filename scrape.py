import requests as rq
import json
from bs4 import BeautifulSoup as bs


def getIds(baseUrl, Id):
    res = rq.get(baseUrl + str(Id))

    if res.status_code != 200:
        return None 

    soup = bs(res.content, features="html.parser")
    container = soup.find('div', {"class":"form-group"})
    options = container.find_all("option")

    codes = []
    for option in options:
        try: codes.append(int(option['value']))
        except KeyError: continue

    if len(codes) == 0:
        return None
    return codes

def getSchool(baseUrl, Id):
    res = rq.get(baseUrl + str(Id))

    if res.status_code != 200:
        return None 

    soup = bs(res.content, features="html.parser")
    name = soup.find('h4').contents[0]

    Classes = soup.find("table", {"class":"table-h"}).find_all("tr")


    schoolObj = {
            "name" : name,
            "classes" : []
    }

    for Class in Classes[1:]:
        stats = Class.find_all("td")
        formated = {
                "oddzial": stats[0].contents[0],
                "miejsca": int(stats[1].contents[0]),
                "Pwybor" : int(stats[2].contents[0]),
                "Nwybor" : int(stats[3].contents[0]),
        }
        schoolObj["classes"].append(formated)

    return schoolObj 




def main():
    baseUrl = "https://ponadpodstawowe-plock.nabory.pl/page/statystyki/Statystyki.aspx?szk_id="
    lobby_id = -1


    print("[OBTAINING SCHOOL IDS]", end="")
    ids = getIds(baseUrl, lobby_id) 
    if ids == None: 
        print(" [FAILED]")
        return -1
    print(" [SUCCES]")

    Schools = []

    size = len(ids)
    i = 0

    print("[STARTING DB CREATION]")
    for Id in ids[1:]:
        print(f"DB-BLOCK[{i}/{size}] <-- writing", end="")

        try:
            Schools.append(getSchool(baseUrl, Id))
            print(" [SUCCES]")
        except: print(" [FAILED]")

        i += 1

    with open("db.json","w") as f:
        print("[DB FILE OPENED]")
        json.dump(Schools, f, indent=4)
        print("[FILE WRITTEN]")
        f.close()


    return 1


if __name__ == "__main__":
    if main() == -1: print("program executed with error")
    else: print("program executed with succes")

    




