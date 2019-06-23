from bs4 import BeautifulSoup
import requests


search = input("enter a search term : ")
params ={"q": search}
r = requests.get("https://www.google.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
result = soup.find("ol", {"id": "b_results"})
links = result.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Summary : ", item.find("a").parent.parent.find("p").text)



