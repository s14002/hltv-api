import requests
from bs4 import BeautifulSoup
from python_utils import converters

def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")

"""
def get_fnx_rating():
    rating = get_parsed_page("http://www.hltv.org/player/557-fnx")
    span = rating.find("span", {"style": "font-weight: bold;"})
    return span.text
"""

def get_matches_url():
    return "http://www.hltv.org/match/2305642-immortals-winterfox-esl-pro-league-season-4-north-america"

def get_match_id():
    ma = get_matches_url()[26:33]
    return ma

def get_team_1_id():
    matches = get_parsed_page(get_matches_url())
    du = matches.find("span", {"style": "vertical-align: -15%;max-width:179px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    st = du.find("a", {"style": "color:black;"})["href"]
    do = st[20:]
    return do

def get_team_2_id():
    matches = get_parsed_page(get_matches_url())
    ma = matches.find("span", {"style": "vertical-align: -15%;max-width:172px;display: inline-block;white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"})
    mb = ma.find("a", {"style": "color:black;"})["href"]
    mc = mb[20:]
    return mc

def get_team_1_name():
    matches = get_parsed_page(get_matches_url())
    team1name = matches.find("a", {"style": "color:black;"})
    return team1name.text

def get_team_2_name():
    matches = get_parsed_page(get_matches_url())
    b = matches.find ("div", {"style": "display:table-cell;width:46%;text-align:left"})
    team2name = b.find("a", {"style": "color:black;"})
    return team2name.text

def get_team_1_score():
    matches = get_parsed_page(get_matches_url())
    team1score = matches.find("span", {"style": "vertical-align:30%;"})
    return team1score.text

def get_team_2_score():
    matches = get_parsed_page(get_matches_url())
    team2= matches.find("div", {"style": "display:table-cell;width:46%;text-align:left"})
    team2score = team2.find("span", {"style": "vertical-align:30%;"})
    return team2score.text

def get_best_of_test():
    matches = get_parsed_page(get_matches_url())
    bo = matches.find("div", {"id": "mapformatbox"}).text
    return bo

def get_best_of():
    test = get_best_of_test()
    nb = test[13:14]
    return nb

def get_map_name_1():
    matches = get_parsed_page(get_matches_url())
    map_1 = matches.findAll("img", style= "border-radius: 4px;;")[0]["src"]
    nb = map_1[40:-4]
    #for test in map_1:
        #print(test["src"][40:-4])
    return nb

def get_map_name_2():
    matches = get_parsed_page(get_matches_url())
    map_2 = matches.findAll("img", style= "border-radius: 4px;;")[1]["src"]
    nb2 = map_2[40:-4]

    return nb2

def get_map_name_3():
    matches = get_parsed_page(get_matches_url())
    map_3 = matches.findAll("img", style= "border-radius: 4px;;")[2]["src"]
    nb3 = map_3[40:-4]
    return nb3

def get_map_name(num):
    matches = get_parsed_page(get_matches_url())
    map_3 = matches.findAll("img", style= "border-radius: 4px;;")
    if len(map_3) <= num:
        return None

    nb3 = map_3[num]["src"][40:-4]
    return nb3

def get_win_team():
    matches = get_parsed_page(get_matches_url())
    if int(get_team_1_score()) > int(get_team_2_score()):
        return get_team_1_name()
    elif int(get_team_1_score()) < int(get_team_2_score()):
        return get_team_2_name()
    else:
        return None

def get_lose_team():
    matches = get_parsed_page(get_matches_url())
    if int(get_team_1_score()) < int(get_team_2_score()):
        return get_team_1_name()
    elif int(get_team_1_score()) > int(get_team_2_score()):
        return get_team_2_name()
    else:
        return None

if __name__ == "__main__":
    ###print(get_fnx_rating())#un-use
    #print(get_match_id())
    #print(get_team_1_id()) #OK
    #print(get_team_2_id()) #OK
    #print(get_team_1_name()) #OK
    #print(get_team_2_name()) #OK
    #print(get_team_1_score()) #OK
    #print(get_team_2_score()) #OK
    print(get_best_of()) #OK
    ###print(get_map_name_1())
    ###print(get_map_name_2())
    ###print(get_map_name_3())
    #print(get_map_name(0)) #OK
    #print(get_map_name(1)) #OK
    #print(get_map_name(2)) #OK
    #print(get_win_team()) #OK
    #print(get_lose_team()) #OK

