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
    linkMatch = re.compile(r'href="(\S*)"')
    links = []
    linkTags = []

    #grab the first 10 link tags
    #the link tags have the class "storylink", limit to 10 matches
    linkTags = soup.find_all(attrs={'class': 'storylink'}, limit=10)

    #convert thelink tags to strings so we can use regex to extract the links
    linkTags = list(map(str, linkTags))

    #use regex to find all matches (the first and only one will be what we need)
    #findall() returns a list of matches, so use the first one by default
    for tag in linkTags:
        #grab all regex matches
        match = linkMatch.findall(tag)
        link = match[0]
        #if the match starts with http, it is a link to an external site and can be passed directly.
        #else it is to a comment section of HN, like the "Ask HN" posts
        if not link[:4] =="http":
            link = "https://news.ycombinator.com/" + link
        links.append(link)
    #gitTest
    return links
