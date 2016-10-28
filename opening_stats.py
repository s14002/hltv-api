import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=175&playerid=1"

matches = get_parsed_page(urls)

def get_opening_stats(num):
    ma = matches.findAll("div", {"style": "padding-left:5px;padding-top:5px;"})[num] #13~18
    mb = ma.findAll("div", {"class": "covSmallHeadline"})[1].text
    return mb

m = 13
while m < 19:
    print(get_opening_stats(m)) #13~18
    m += 1

