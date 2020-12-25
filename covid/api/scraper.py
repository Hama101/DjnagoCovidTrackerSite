import requests
from bs4 import BeautifulSoup


# function that trackes covid-19 by contrey
def covidStat(country):
    print("Hello Covid-19 tracker !")
    page = requests.get(
        f"https://www.worldometers.info/coronavirus/country/{country}/")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(class_="content-inner")
    img =main.find('img')
    infos = main.find_all(id="maincounter-wrap")
    values = [info.find('span') for info in infos]
    final = {
        'img':img['src'],
        "country" : country ,
        'Coronavirus Cases': values[0].get_text(),
        'Deaths': values[1].get_text(),
        'Recovered':values[2].get_text(),
    }
    return final

