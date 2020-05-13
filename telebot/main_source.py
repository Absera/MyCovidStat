import requests
from bs4 import BeautifulSoup
import datetime

######################################################
# 					Stat Functions					 #
######################################################



srcUrl = 'https://www.worldometers.info/coronavirus/'
request = requests.get(srcUrl)
src = request.content

soup = BeautifulSoup(src, 'lxml') 


def get_world_stat(msg):


    worldStat = []
    worldStatDict = {}
    worldStatFinal = 'World Status\n\n'
    
    divs = soup.find_all('div', {'class' : 'maincounter-number'})
    
    for i in range(len(divs)):
        
        spans = divs[i].find_all('span')
        
        worldStat.append(spans[0].text)

    wordsDict = {
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
    worldStatFinal += f'\n\nDate: {datetime.datetime.now()}\nSource: https://www.worldometers.info/'
    return worldStatFinal



def get_top10_stat(msg):
    countryStat = []
    countryStatFinal = '\n\n\nTop 10 Countries\n'

    id = {'id': 'main_table_countries_today'}
    table = soup.find('table', id)

    row = table.findAll('tr')
    row = row[9:19]

    for i in range(len(row)):
        data = row[i].findAll('td')
        data = data[0:6]

        for j in range(len(data)):

            countryStat.append(data[j].text)
            for item in countryStat:
                if item == '':
                    itemIndex = countryStat.index(item)
                    countryStat[itemIndex] = '-'
            
    wordsDict = {
        'country_name' : 'Name',
        'total_cases' : 'Total Cases',
        'new_cases' : 'New Cases',
        'total_death' : 'Total Deaths',
        'new_death' : 'New Death'
    }

    countryStatDict = {
        1 : {
        'country_name' : countryStat[0:5][0],
        'total_cases' : countryStat[0:5][1],
        'new_cases' : countryStat[0:5][2],
        'total_death' : countryStat[0:5][3],
        'new_death' : countryStat[0:5][4]
        },
        
        2 : {
        'country_name' : countryStat[6:11][0],
        'total_cases' : countryStat[6:11][1],
        'new_cases' : countryStat[6:11][2],
        'total_death' : countryStat[6:11][3],
        'new_death' : countryStat[6:11][4]
        },
        3 : {
        'country_name' : countryStat[12:17][0],
        'total_cases' : countryStat[12:17][1],
        'new_cases' : countryStat[12:17][2],
        'total_death' : countryStat[12:17][3],
        'new_death' : countryStat[12:17][4]
        },
        4 : {
        'country_name' : countryStat[18:23][0],
        'total_cases' : countryStat[18:23][1],
        'new_cases' : countryStat[18:23][2],
        'total_death' : countryStat[18:23][3],
        'new_death' : countryStat[18:23][4]
        },
        5 : {
        'country_name' : countryStat[24:29][0],
        'total_cases' : countryStat[24:29][1],
        'new_cases' : countryStat[24:29][2],
        'total_death' : countryStat[24:29][3],
        'new_death' : countryStat[24:29][4]
        },
        6 : {
        'country_name' : countryStat[30:35][0],
        'total_cases' : countryStat[30:35][1],
        'new_cases' : countryStat[30:35][2],
        'total_death' : countryStat[30:35][3],
        'new_death' : countryStat[30:35][4]
        },
        7 : {
        'country_name' : countryStat[36:41][0],
        'total_cases' : countryStat[36:41][1],
        'new_cases' : countryStat[36:41][2],
        'total_death' : countryStat[36:41][3],
        'new_death' : countryStat[36:41][4]
        },
        8 : {
        'country_name' : countryStat[42:47][0],
        'total_cases' : countryStat[42:47][1],
        'new_cases' : countryStat[42:47][2],
        'total_death' : countryStat[42:47][3],
        'new_death' : countryStat[42:47][4]
        },
        9 : {
        'country_name' : countryStat[48:53][0],
        'total_cases' : countryStat[48:53][1],
        'new_cases' : countryStat[48:53][2],
        'total_death' : countryStat[48:53][3],
        'new_death' : countryStat[48:53][4]
        },
        10 : {
        'country_name' : countryStat[54:59][0],
        'total_cases' : countryStat[54:59][1],
        'new_cases' : countryStat[54:59][2],
        'total_death' : countryStat[54:59][3],
        'new_death' : countryStat[54:59][4]
        },
        }
    

    for keyi in  countryStatDict:
        countryStatFinal += f'\n       {str(keyi)}'
        for keyj in countryStatDict[keyi]:
            countryStatFinal += f'\n{wordsDict[keyj]} : {countryStatDict[keyi][keyj]}'
        countryStatFinal += '\n\n+----------------------+\n'
    countryStatFinal += f'\n\nDate: {datetime.datetime.now()}\nSource: https://www.worldometers.info/'
    return countryStatFinal
