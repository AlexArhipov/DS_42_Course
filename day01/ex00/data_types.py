#!/bin/sh/python3
# coding: utf-8
def data_types():
    a = 1
    b = "2"
    c = 3.3
    d = False
    e = [1, 2, 3, 4]
    f = { 1:"1", 2:"3"}
    g = (1, 2, 3, 4)
    m = {1, 2, 3, 4}
    n = [type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(m)]
    s = ""
    for i in n:
        s += i.__name__ + ', ';
    s = '[' + s[:-2] + ']'

    print (s)
if __name__ == '__main__':
    data_types()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
