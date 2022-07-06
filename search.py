import requests
import sys
from pystyle import Center, Box, Colorate, Colors

def search(searched):
    print("\n \n")

    one = requests.get(f"https://botw-compendium.herokuapp.com/api/v2/entry/{searched}")

    f = one.json()

    if f["data"] != {}:
        data = f["data"]

        name = searched
        category = data["category"]
        locations = list(data["common_locations"])
        locations_text = ""
        drops = list(data["drops"])
        drops_text = ""
        url_image = data["image"]
    else:
        print(Colorate.Horizontal(Colors.yellow_to_red, "Not find.", 1))
        sys.exit()

    for y in range(len(locations)):
        locations_text += locations[y]
        locations_text += ", "

    for y in range(len(drops)):
        drops_text += drops[y]
        drops_text += ", "
   

    text = f"The {name.upper()} :\n\nCategory : {category} \nLocations : {locations_text}\nDrops : {drops_text}\nImage : {url_image}"
    print(Colorate.Horizontal(Colors.yellow_to_red, Box.DoubleCube(text), 1))


