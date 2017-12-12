# CIS192 OUPSCCBOT

_by Yoojin Kim_

Bot that scrapes Official Unofficial Penn Squirrel Catching Club (OUPSCC) Facebook Group.

Display meme with greatest number of reactions for given keyword(s).

## Execution

App ID, and App Secret should be set before execution (in scraper.py)

```
python3 app.py
```

## Structure

### feed.py

Defines Feed class that stores message, name, picture, and reactions fields associatied with the feed.

lt and eq are implemented so that Feed can be stored in heapq.

### scraper.py

Scrapes OUPSCC Facebook Group and stores the memes in heapq.

Generator is used to retrieve all the whitespace separated tokens that a message on meme contains.

### app.py

flask framework for bot.

```
'/': Scrape memes
'/search': Enables user to enter keyword(s)
'/result': Display meme with greatest number of reactions
```

## Modules

collections (defaultdict, Counter): Store fields scraped from feeds

re (search): Retreive paging number from url

heapq (heappush, heappop): Store memes in descending order of number of reactions

flask: Framework for bot

json (loads): Retreive feeds as Python object