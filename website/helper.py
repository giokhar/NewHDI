from datetime import datetime
import requests
import json
from dataMining.helper import validate, BASE_URL

# ==========================
# IMPORTS FROM DATA MINING
# ==========================

def checkList(urls, year):
#   Helper for getRecentOfAll
    for url in urls:
        if not validate(url)['exists']:
            return False
    return True

def getRecentOfAll(ids):
    
    temp_year = datetime.now().year
    end_year = temp_year - 20
    
    while(end_year < temp_year):
        urls = []
        for id in ids:
            urls.append(BASE_URL + "countries/indicators/"+ id + "?date=" + str(temp_year) + "&format=json")

        if checkList(urls, temp_year):
            return temp_year
        temp_year -= 1
        
    return False