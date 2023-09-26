

#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import re 
import csv
import os
import datetime

dir  = os.getcwd()




def scraper(URL,URLNOAA,LOCC):
    rNOAA = requests.get(URLNOAA)
    r= requests.get(URL)

    aviCast = BeautifulSoup(r.content, 'html5lib')
    Weather = BeautifulSoup(rNOAA.content, 'html5lib')

    data=[]
    HTemp = 0
    table = aviCast.find('div')
    tableNOAA = Weather.find('p',{'class' : 'temp temp-high'})



    HTemp = re.findall(r'\d+', str(tableNOAA))


    print(HTemp[0])
    data.append( table.find('td', attrs = {'class' : 'details left'}))
    c=0
    print(data)
    
    table.find('div', attrs={'class': 'hazard-rating-container'})
    
    h_rating = re.findall(r'High|Considerable|Moderate|Low|None|No Rating',str(table.img['src']))

    while "" in data:
        data.remove("")
    direction = re.findall(r'NA|NW|NE|SW|SE|S|N|W|E', str(data[0]))
    print(direction[0])
    data[0] = re.findall(r'\d+', str(data[0]))
    
   
    print(data)
    tocsv = {}
    tocsv['Date'] = datetime.datetime.now().date()
    tocsv['New Snow'] = int(data[0][0])
    try:
        tocsv['Wind L'] = data[0][1]
        tocsv['Wind H'] = data [0][2]
    except:
        tocsv['Wind L'] = 'NA'
        tocsv['Wind H'] = 'NA'
    try:
        tocsv['Direction'] = direction[0]
    except:
        tocsv['Direction'] = "N/A"
    tocsv['Temp'] = HTemp[0]
    try:
        tocsv['Danger'] = h_rating[0]
            
    except:
        tocsv['Danger'] = 'None'
    filename = LOCC
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['Date','New Snow','Wind L','Wind H','Direction','Temp','Danger'])
        w.writerow(tocsv)

try:
    scraper("https://www.mtavalanche.com/forecast/bridgers","https://forecast.weather.gov/MapClick.php?lat=45.29665000000006&lon=-108.91414999999995#.ZDhpO3bMK3A", dir + '/bridger.csv')
    scraper("https://www.mtavalanche.com/forecast/northern-gallatin","https://forecast.weather.gov/MapClick.php?lon=-110.98519999999996&lat=45.46195413858578#detailed-forecast",dir + '/northern-gallatin.csv')
    scraper("https://www.mtavalanche.com/forecast/northern-madison","https://forecast.weather.gov/MapClick.php?lon=-111.37391198351382&lat=45.332802563598165#detailed-forecast", dir + '/northern-madison.csv')
    scraper("https://www.mtavalanche.com/forecast/southern-madison","https://forecast.weather.gov/MapClick.php?lon=-111.2721355117673&lat=44.98236153381072#detailed-forecast",dir + '/southern-madison.csv')
    scraper("https://www.mtavalanche.com/forecast/southern-gallatin","https://forecast.weather.gov/MapClick.php?lon=-111.0984325073243&lat=45.08282136429102#detailed-forecast",dir + '/southern-gallatin.csv')
    scraper("https://www.mtavalanche.com/forecast/lionhead","https://forecast.weather.gov/MapClick.php?lon=-111.30645604248043&lat=44.71433192428469#detailed-forecast",dir + '/lionhead.csv')
    scraper("https://www.mtavalanche.com/forecast/cooke-city","https://forecast.weather.gov/MapClick.php?lon=-109.91440389404296&lat=45.049904852156004#detailed-forecast",dir  +'/cooke-city.csv')
    scraper("https://www.mtavalanche.com/index.php/forecast/centennials","https://forecast.weather.gov/MapClick.php?lon=-111.61148071289064&lat=44.55867416024307#.XBE8RyckpHQ",dir + '/centennials.csv')
except:
    print("fail")