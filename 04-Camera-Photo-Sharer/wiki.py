import wikipedia
page = wikipedia.WikipediaPage("beach")
print(type(page))
link = page.images[0]
import requests
req = requests.get(link)
with open("the_beach.png", "wb") as file:
    file.write(req.content)