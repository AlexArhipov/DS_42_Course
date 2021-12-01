import os
from sys import argv
import requests
from bs4 import BeautifulSoup
import time
import cProfile
import pstats
import io

def main():
    if len(argv) == 3:
        ticker = argv[1].lower()
        my_field = argv[2]
        url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
        response = requests.get(url, headers={'User-Agent': 'Custom'})
        if response.status_code == 404:
            raise Exception('такой сылки нет')
        soup = BeautifulSoup(response.text, "html.parser") #lxml
        title = soup.title.string
        if title == 'Symbol Lookup from Yahoo Finance':
            raise Exception('тикер не найден')
        quotes = soup.find_all('span')
        caunt = 99
        s = []
        # time.sleep(3)
        for quote in quotes:
            if quote.text == my_field:
                caunt = 0
            if caunt < 6:
                s.append(quote.text)
                caunt += 1
        print(tuple(s))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    my_result = main()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()
    with open('profiling-tottime.txt', 'w+') as f:
        f.write(s.getvalue())
    # profiling-sleep.txt     - base
    # profiling-tottime.txt   - without sleep
    # profiling-http.txt      - other http library
    # profiling-ncalls.txt    -
    # pstats - cumulative.txt