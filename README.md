# CIS192 OUPSCCBOT

Bot that scrapes Official Unofficial Penn Squirrel Catching Club (OUPSCC) Facebook Group.

Display meme with greatest number of reactions for given keyword(s).

# Structure

feed.py
Defines Feed class that stores message, name, picture, and reactions fields associatied with the feed
__lt__ and __eq__ are implemented so that Feed can be stored in heapq

scraper.py
Scrapes OUPSCC Facebook Group and stores the memes in heapq

app.py
flask framework for bot

'/': Scrape memes

'/search': Enables user to enter keyword(s)

'/result': Display meme with greatest number of reactions

# Modules

collections (defaultdict, Counter): Store fields scraped from feeds

heapq (heappush, heappop): Store memes in descending order of number of reactions

flask: Framework for bot
