def print_hi(name):
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    list_of_tuples = sorted(list_of_tuples)
    d = {}
    for i in list_of_tuples:
        if i[0] not in d:
            d[i[0]] = int(i[1])

    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get, reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = d[w]

    for i in sorted_dict:
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')