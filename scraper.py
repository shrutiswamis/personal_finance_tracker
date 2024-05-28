import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'https://finance.yahoo.com/topic/stock-market-news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    news_items = soup.select('.js-stream-content .js-content-wrapper')

    for item in news_items:
        title = item.select_one('h3 a').text.strip() # Extract the title of the news article
        summary = item.select_one('p').text.strip() # Extract the summary of the news article
        date = item.select_one('.date-time').text.strip() # Extract the date of the news article

        article = {
            'title': title,
            'summary': summary,
            'date': date
        }
        articles.append(article)

    print(articles)
    return articles

def scrape_stock_prices():
    url = 'https://finance.yahoo.com/most-active/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    stock_prices = []
    stock_table = soup.select_one('table')
    rows = stock_table.select('tbody tr')

    for row in rows:
        cells = row.select('td')
        symbol = cells[0].text.strip() # Extract the stock symbol
        name = cells[1].text.strip() # Extract the stock name
        price = cells[2].text.strip() # Extract the stock price
        change = cells[3].text.strip() # Extract the stock price change
        percent_change = cells[4].text.strip() # Extract the stock price percent change
        volume = cells[5].text.strip() # Extract the stock volume 

        stock_price = {
            'symbol': symbol,
            'name': name,
            'price': price,
            'change': change,
            'percent_change': percent_change,
            'volume': volume
        }
        stock_prices.append(stock_price)
    
    return stock_prices
