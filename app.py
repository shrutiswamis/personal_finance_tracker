from flask import Flask, render_template
from scraper import scrape_news, scrape_stock_prices

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/news')
def news():
    articles = scrape_news()
    return render_template('news.html', articles=articles)

@app.route('/stocks')
def stocks():
    stock_prices = scrape_stock_prices()
    return render_template('stocks.html', stock_prices=stock_prices)

if __name__ == '__main__':
    app.run(debug=True)