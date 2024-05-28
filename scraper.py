import requests
import yfinance as yf
from bs4 import BeautifulSoup

def scrape_news():
    
    ticker = yf.Ticker("^GSPC") # For the S&P 500 index

    news = ticker.news

    articles = []
    for article in news:
        title = article["title"]
        date = article["providerPublishTime"]
        link = article["link"]

        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the summary from the article content
        summary_element = soup.find("div", class_="some-summary-class")
        if summary_element:
            summary = summary_element.get_text().strip()
        else:
            summary = ""

        article_data = {
            "title": title,
            "summary": summary,
            "date": date
        }
        articles.append(article_data)
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
