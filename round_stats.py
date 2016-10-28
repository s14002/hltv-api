import requests, re
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

urls = "http://www.hltv.org/?pageid=175&playerid=9220"

matches = get_parsed_page(urls)

def get_round_stats(num):
    ma = matches.findAll("div", {"style": "padding-left:5px;padding-top:5px;"})[num] #6~12
    mb = ma.findAll("div", {"class": "covSmallHeadline"})[1].text
    return mb

m = 6
while m < 13:
    print(get_round_stats(m)) #6~12
    m += 1

