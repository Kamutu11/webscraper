from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.motorauthority.com/news/super-cars").text
soup = BeautifulSoup(html, 'lxml')
cards = soup.find_all("li", class_="")
ul = soup.find("ul", class_="items-list")
large = soup.find_all("li", class_="large")
slot = soup.find_all("li", class_="nativo-slot")
ad = soup.find_all("li", class_="adv-spacer")



for card in cards:
    if card in ul:
        if card == [large] or [slot] or [ad] :
            carName = card.div.a.text
            carDet = card.div.p.text
            carImg = card.a.img["data-src"]
            print(f"Car Name: {carName}")
            print(f"Car Details: {carDet}")
            print(f"ImgUrl: {carImg}")

            print("")