# CIS192 OUPSCCBOT

Bot that scrapes Official Unofficial Penn Squirrel Catching Club (OUPSCC) Facebook Group.

Display meme with greatest number of reactions for given keyword(s).

## Structure

__feed.py__

Defines Feed class that stores message, name, picture, and reactions fields associatied with the feed

lt and eq are implemented so that Feed can be stored in heapq


__scraper.py__

Scrapes OUPSCC Facebook Group and stores the memes in heapq

__app.py__

flask framework for bot
```
'/': Scrape memes
'/search': Enables user to enter keyword(s)
'/result': Display meme with greatest number of reactions
```
## Modules

collections (defaultdict, Counter): Store fields scraped from feeds

heapq (heappush, heappop): Store memes in descending order of number of reactions

flask: Framework for bot
