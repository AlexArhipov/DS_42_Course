# coding: utf-8
# -*- coding: utf-8 -*-

def replas(s):
    return s.replace(', ', '$ ')

def re_replas(s):
    return s.replace('$ ', ', ')

def change_replas(s):
    return s.replace(',', '\t')

def reade_and_wite():
    with open('ds.tsv', 'w') as fs:
        with open('ds.csv', 'r') as f:
            results = []
            for line in f:
                line = replas(line)
                line = change_replas(line)
                line = re_replas(line)
                fs.write(line + '\n')

            fs.close()
            # words = line.split(',')
            # results.append((words[0], words[1],words[2],words[3],words[4],))
        # for rows in results:
        #     for i in rows:
        #         print(i,"****")

            # for parsed_item in rows:
            #     parsed_item = parsed_item.replace(',', ':')  # Change rows to parsed_item
                # writer.writerow(parsed_item)
        # print(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reade_and_wite()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
