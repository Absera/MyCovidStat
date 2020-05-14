import requests
from bs4 import BeautifulSoup
import datetime

##########################################################
# 	This is the main source of the information           #
#   functions in this file retrieves data from <srcUrl>  #
#   and are called in the main <app.py>	        		 #
##########################################################


srcUrl = 'https://www.worldometers.info/coronavirus/'
request = requests.get(srcUrl)
src = request.content

soup = BeautifulSoup(src, 'lxml') 

def get_world_stat(msg):


    worldStat = []
    worldStatDict = {}
    worldStatFinal = 'World Status\n\n'
    
    divs = soup.find_all('div', {'class' : 'maincounter-number'}) # div tag info of the <url>
    
    for i in range(len(divs)):
        
        spans = divs[i].find_all('span')
        
        worldStat.append(spans[0].text)

    wordsDict = { # refers to keys in the dict <worldstatdict> vs the displayed one
        'total_case' : 'Total Cases',
        'death' : 'Total Deaths',
        'recovered' : 'Recovered',
    }

    worldStatDict = {
        'total_case' : worldStat[0],
        'death' : worldStat[1],
        'recovered' : worldStat[2]
    }
    

    for key in worldStatDict:
        worldStatFinal += f'{wordsDict[key]} : {worldStatDict[key]}\n'
    
    date = datetime.datetime.now()
    time = date.strftime("%a %I:%M %p, %b - %Y")
    countryStatFinal += f'\nDate: {time}'
    countryStatFinal += f'\nSource: worldometers.info'

    return worldStatFinal



def get_top10_stat(msg):
    countryStat = []
    countryStatFinal = '\n\n\nTop 10 Countries\n'

    id = {'id': 'main_table_countries_today'} # id of the table in the <url>
    table = soup.find('table', id)

    row = table.findAll('tr')
    row = row[9:19] # slices in the table startinf from number 1 to number 10 excluding others

    for i in range(len(row)):
        data = row[i].findAll('td')
        data = data[0:6] # slices only the data i want, like only <total case, new case, death, new death>

        for j in range(len(data)):

            countryStat.append(data[j].text)
            for item in countryStat:
                if item == '': # replace '' with '-' if there is no info yet
                    itemIndex = countryStat.index(item)
                    countryStat[itemIndex] = '-'

    statList = [ # at first all data was contained in one list # so i sliced it for each country
    countryStat[0:5], 
    countryStat[6:11], 
    countryStat[12:17], 
    countryStat[18:23], 
    countryStat[24:29], 
    countryStat[30:35], 
    countryStat[36:41], 
    countryStat[42:47], 
    countryStat[48:53], 
    countryStat[54:59]
    ]

    countryList = [x for x in statList] # takes the above <statList> and contain them in one list

    allTop10Info = []

    for item in countryList:
        item.insert(0, countryList.index(item) +1)
        allTop10Info.append(item)


    wordsDict = { # used to refer in the dict <countryStatDict>
        'country_name' : 'Country Name',
        'total_cases' : 'Total Cases',
        'new_cases' : 'New Cases',
        'total_death' : 'Total Deaths',
        'new_death' : 'New Death'
    }

    countryStatDict = { # adds all info in form of dictionary from the list <allTop10Info>
    i[0]:{
    'country_name':i[1],
    'total_cases':i[2],
    'new_cases':i[3],
    'total_death':i[4],
    'new_death':i[5]

    } for i in allTop10Info # important
    }

    for keyi in  countryStatDict: # orders all the info in a easy-to-read way
        countryStatFinal += f'\n       {str(keyi)}'
        for keyj in countryStatDict[keyi]:
            countryStatFinal += f'\n{wordsDict[keyj]} : {countryStatDict[keyi][keyj]}'
        countryStatFinal += '\n\n+----------------+\n'

    date = datetime.datetime.now()
    time = date.strftime("%a %I:%M %p, %b - %Y")
    countryStatFinal += f'\nDate: {time}'
    countryStatFinal += f'\nSource: worldometers.info'

    return countryStatFinal







