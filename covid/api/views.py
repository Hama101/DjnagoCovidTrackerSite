from django.shortcuts import render
from . import scraper as s
import requests as r
from bs4 import BeautifulSoup
# Create your views here.

def nav(request):
    return render(request , 'base.html')


def home(request):
    return render(request,'home.html')

def showCovid(request):
    try:
        country = request.POST['country']
        infos = s.covidStat(country)
        page = r.get(f"https://www.worldometers.info/coronavirus/country/{country}/")
        soup = BeautifulSoup(page.content, 'html.parser')
        main = soup.find(class_="content-inner")
        img =main.find('img')
        infos = main.find_all(id="maincounter-wrap")
        values = [info.find('span') for info in infos]

        dict = {
            'img':img['src'],
            "country" : country ,
            'Coronavirus_Cases': values[0].get_text(),
            'Deaths': values[1].get_text(),
            'Recovered':values[2].get_text(),
        }
        return render(request,'showcovid.html',dict)
    except :
        return render(request,'error.html')