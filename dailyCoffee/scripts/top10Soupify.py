from bs4 import BeautifulSoup
import urllib.request as ur
import re

def HNTop10():
    """
    grabs top 10 stories from hackernews
    returns them as a list of links in string format
    """
    #grab Hacker News and use beautiful soup to find top 10 links

    HN = ur.urlopen("https://news.ycombinator.com/").read()
    soup = BeautifulSoup(HN)

    #grab the first 10 link tags
    #the link tags have the class "storylink", limit to 10 matches
    linkTags = soup.find_all(attrs={'class': 'storylink'}, limit=10)

    #convert thelink tags to strings so we can use regex to extract the links
    linkTags = list(map(str, linkTags))
    linkMatch = re.compile(r'(http\S*)"')

    #use the compiled regex to find all matches (the first and only one will be what we need)
    #findall() returns a list of matches, so use the first one by default
    links = [linkMatch.findall(tag)[0] for tag in linkTags]

    return links
