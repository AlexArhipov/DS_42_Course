#!/usr/bin/env python3
import timeit

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def repets(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
              'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    repets_time = timeit.timeit(f'repets({emails})', setup='from __main__ import repets', number=90000000)
    comprehensions_time = timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=90000000)
    # print(repets(emails))
    # print(comprehensions(emails))
    if repets_time < comprehensions_time:
        print('it is better to use a loop\n', str(repets_time) + 'vs' + str(comprehensions_time))
    else:
        print('it is better to use a list comprehension\n', str(comprehensions_time) + ' vs ' + str(repets_time), sep = '')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
