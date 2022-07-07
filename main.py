from pystyle import Write, Colors, Add, Colorate
from zelda_banner import zelda_banner
from search import search

text = "This is a beautiful banner\nmade with pystyle"

banner = Add.Add(zelda_banner, "", 4)
print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

searched = Write.Input("What do you want to search ? -> ", Colors.red_to_yellow, interval=0.025, hide_cursor=False)

url_image = search(searched)

open = Write.Input("Open the image in your webbrowser ? (yes/no) -> ", Colors.red_to_yellow, interval=0.025, hide_cursor=False)

if open == "yes":
    import webbrowser
    webbrowser.open(url_image)