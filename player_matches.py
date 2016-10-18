import requests
from bs4 import BeautifulSoup
from python_utils import converters
import re

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

def get_matches_url():
    return "http://www.hltv.org/match/2305887-kinguin-eu4ia-dreamhack-zowie-%20open-winter-2016-closed-qualifier"
def get_match_id():
    ma = get_matches_url()[26:33]
    return ma

def get_player_id():
    matches = get_parsed_page(get_matches_url())
    ma = matches.findAll("div", {"class": "text-center", "style": "background-color:white;width:105px;float:left;margin-left:4px;border: 1px solid rgb(189, 189, 189);border-radius: 5px;padding:2px;"})[9] #0~9
    ta = ma.find("a")["href"]
    l = len(ta)
    elta = ta[8:]
    transInt = re.match("\d*",elta)
    da = transInt.group()
    if l >= 23:
        return ta[22:]
    elif l < 23:
        return da

def get_kill():
    matches = get_parsed_page(get_matches_url())
    sa = matches.find("div", {"class": "covSmallHeadline", "style": "font-weight:normal;width:10%;float:left;;text-align:center"})

    return sa


#print(get_match_id())
#print(get_player_id())
print(get_kill())
