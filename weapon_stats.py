import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=175&playerid=9220"

matches = get_parsed_page(urls)

def get_weapon_stats(num):
    ma = matches.findAll("div", {"style": "padding-left:5px;padding-top:5px;"})[num] #19~23
    mb = ma.findAll("div", {"class": "covSmallHeadline"})[1].text
    return mb

m = 19
while m < 24:
    print(get_weapon_stats(m)) #19~23
    m += 1

