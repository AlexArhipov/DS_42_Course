from sys import argv

def ft_main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK',
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(argv) == 2:
        lists = argv
        lis = lists[1].split(",")
        for a in lis:
            if len(a) == 0:
                return
        for z in lis:
            ss = z.strip()
            if ss.capitalize() in COMPANIES:
                print(ss.capitalize(), "stock price is", STOCKS[COMPANIES[ss.capitalize()]])
            elif ss.upper() in STOCKS:
                for i in COMPANIES:
                    if ss.upper() in COMPANIES[i]:
                        print(COMPANIES[i], "is a ticker symbol for", i)
            else:
                print(ss, "is an unknown company or an unknown ticker symbol")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft_main()