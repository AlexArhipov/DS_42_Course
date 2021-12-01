import os
from sys import argv
import requests
from bs4 import BeautifulSoup
import time
import cProfile

def main():
    if len(argv) == 3:
        ticker = argv[1].lower()
        my_field = argv[2]
        url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
        response = requests.get(url, headers={'User-Agent': 'Custom'})
        if response.status_code == 404:
            raise Exception('такой сылки нет')
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string
        if title == 'Symbol Lookup from Yahoo Finance':
            raise Exception('тикер не найден')
        quotes = soup.find_all('span')
        caunt = 99
        s = []
        time.sleep(3)
        for quote in quotes:
            if quote.text == my_field:
                caunt = 0
            if caunt < 6:
                s.append(quote.text)
                caunt += 1
        print(tuple(s))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # cProfile.run('main()')
