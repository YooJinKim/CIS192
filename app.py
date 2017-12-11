from flask import Flask, render_template, redirect, request, url_for
from scraper import *
from queue import PriorityQueue
import logging

app = Flask(__name__)
global feeds
global counter


@app.route('/')
def template():
    global feeds
    global counter
    scraper = Scraper()
    feeds = scraper.feeds
    counter = scraper.counter
    return redirect(url_for('search'))


@app.route('/search')
def search():
    return render_template('layout.html')


@app.route('/result', methods=['POST'])
def typed():
    global feeds
    global counter
    que = PriorityQueue()
    counts = PriorityQueue()
    text = request.form['text']
    if not text:
        feed = feeds[''].queue[0]
        que.put(feed)
        counts.put((feed[0], counter['']))
    else:
        for token in text.split():
            token = token.upper()
            if token in feeds:
                feed = feeds[token].queue[0]
                que.put(feed)
                counts.put((feed[0], counter[token]))
    if que.queue:
        (_, message, name, picture, reactions) = que.get()
        (_, count) = counts.get()
        return render_template(
            'result.html', name=name, reactions=reactions, count=count,
            message=message, meme=picture)
    else:
        return render_template('failure.html')


@app.route('/log/<msg>/<mode>')
def log(msg, mode):
    app.logger.debug(msg)
    return('LEVEL:{}\nLogged: {}'.format(mode, msg))


def main():
    app.debug = True
    log_handler = logging.FileHandler('my_flask.log')
    log_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(log_handler)
    app.run()

app.secret_key = ':\xbb\x13\xf5\xbap\xa4\x80\x08\xa8\x82\x8fS\xa2I\xc2\xcd:\x1b\xfa4k%\xa5'

if __name__ == '__main__':
    main()
