import sys
import requests
from pystyle import Center, Box, Colorate, Colors, Write

def search(searched):
    print("\n \n")

    one = requests.get(f"https://botw-compendium.herokuapp.com/api/v2/entry/{searched}")

    f = one.json()

    if f["data"] != {}:
        data = f["data"]

        name = searched
        category = data["category"]

        if category == "creatures" or category == "monster":

            try: 
                f = data["common_locations"] 
            except KeyError: 
                data["common_locations"] = None

            if data["common_locations"] != None:
                locations = list(data["common_locations"])
            else:
                locations = ["None"]
            locations_text = ""

            try: 
                f = data["drops"] 
            except KeyError: 
                data["drops"] = None

            if data["drops"] != None:
                drops = list(data["drops"])
            else:
                drops = ["None"]
            drops_text = ""

            url_image = data["image"]

            for y in range(len(locations)):
                locations_text += locations[y]
                locations_text += ", "

            for y in range(len(drops)):
                drops_text += drops[y]
                drops_text += ", "

            text = f"The {name.upper()} :\n\nCategory : {category}, \nLocations : {locations_text}\nDrops : {drops_text}\nImage : {url_image}"
        
        elif category == "equipment":
            locations = list(data["common_locations"])
            locations_text = ""
            url_image = data["image"]
            attack = data["attack"]
            defense = data["defense"]

            for y in range(len(locations)):
                locations_text += locations[y]
                locations_text += ", "
            
            text = f"The {name.upper()} :\n\nCategory : {category} \nLocations : {locations_text}\nAttack : {attack}\nDefense : {defense}\nImage : {url_image}"
        
        elif category == "materials":
            locations = list(data["common_locations"])
            locations_text = ""
            url_image = data["image"]
            effect = data["cooking_effect"]
            hearts = data["hearts_recovered"]

            for y in range(len(locations)):
                locations_text += locations[y]
                locations_text += ", "
            
            text = f"The {name.upper()} :\n\nCategory : {category} \nLocations : {locations_text}\nCooking Effect : {effect}\nHearts Recovered : {hearts} \nImage : {url_image}"
        
        else:
            locations = list(data["common_locations"])
            locations_text = ""
            url_image = data["image"]
            drops = list(data["drops"])
            drops_text = ""
            
            for y in range(len(drops)):
                drops_text += drops[y]
                drops_text += ", "

            for y in range(len(locations)):
                locations_text += locations[y]
                locations_text += ", "
            
            text = f"The {name.upper()} :\n\nCategory : {category} \nLocations : {locations_text}\nDrops : {drops_text} \nImage : {url_image}"
        

        print(Colorate.Horizontal(Colors.yellow_to_red, Box.DoubleCube(text), 1))
        return url_image

    else:
        return search2(searched)

def search2(searched):
    all = requests.get("https://botw-compendium.herokuapp.com/api/v2/all").json()
    list_result = []
    number_result = 0
    
    creatures = all["data"]["creatures"]
    for u in range(len(creatures["food"])):
        if searched in creatures["food"][u]["name"]:
            list_result.append(creatures["food"][u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {creatures['food'][u]['name']}", 1))
            number_result += 1
    
    for u in range(len(creatures["non_food"])):
        if searched in creatures["non_food"][u]["name"]:
            list_result.append(creatures["non_food"][u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {creatures['non_food'][u]['name']}", 1))
            number_result += 1
    
    equipment = all["data"]["equipment"]
    for u in range(len(equipment)):
        if searched in equipment[u]["name"]:
            list_result.append(equipment[u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {equipment[u]['name']}", 1))
            number_result += 1
    
    material = all["data"]["materials"]
    for u in range(len(material)):
        if searched in material[u]["name"]:
            list_result.append(material[u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {material[u]['name']}", 1))
            number_result += 1
            
    
    monster = all["data"]["monsters"]
    for u in range(len(monster)):
        if searched in monster[u]["name"]:
            list_result.append(monster[u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {monster[u]['name']}", 1))
            number_result += 1
    
    treasure = all["data"]["treasure"]
    for u in range(len(treasure)):
        if searched in treasure[u]["name"]:
            list_result.append(treasure[u]["name"])
            print(Colorate.Horizontal(Colors.yellow_to_red, f"   {number_result}. {treasure[u]['name']}", 1))
            number_result += 1

    if len(list_result) != 0:
        searched = int(Write.Input("\n \nWhat do you want to see ? (1, 2, 3, ...) -> ", Colors.red_to_yellow, interval=0.025, hide_cursor=False))

    return search(list_result[searched])


