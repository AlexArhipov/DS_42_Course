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
        first = first.upper()
        for i in COMPANIES:
            if first == COMPANIES[i]:
                return print(i, STOCKS[first])
        else:
            print('Unknown company')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft_main()
