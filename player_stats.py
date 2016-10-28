import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=175&playerid=10000"

matches = get_parsed_page(urls)

def get_player_stats(num):
    ma = matches.findAll("div", {"style": "padding-left:5px;padding-top:5px;"})[num]
    mb = ma.findAll("div", {"class": "covSmallHeadline"})[1].text
    return mb

#0~5 Overall_stats
#6~12 Round_stats
#13~18 Opening_stats
#19~23 Weapon_stats

m = 0
while m <= 23:
    print(get_player_stats(m))
    m += 1

