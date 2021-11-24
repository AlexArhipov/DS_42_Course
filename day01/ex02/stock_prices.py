# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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
        name_script, first = argv
        first = first.capitalize()
        if first not in COMPANIES:
            print('Unknown company')
        elif COMPANIES[first] in STOCKS:
            print(STOCKS[COMPANIES[first]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
