import os
from flask import Flask, render_template, url_for, send_from_directory
from scraper import scrape_news, scrape_stock_prices

app = Flask(__name__, static_folder='static')

app.secret_key = '7420uhde34793'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/news')
def news():
    articles = scrape_news()
    print(articles)
    return render_template('news.html', articles=articles)

@app.route('/stocks')
def stocks():
    stock_prices = scrape_stock_prices()
    return render_template('stocks.html', stock_prices=stock_prices)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)



if __name__ == '__main__':
    app.run(debug=True)