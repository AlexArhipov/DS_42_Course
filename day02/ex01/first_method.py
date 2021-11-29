# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Research(object):
    def file_reader():
        try:
            with open('data.csv', 'r') as f:
                s = ''
                for line in f:
                    s += line
            return s
        except:
            print('Нет файла')

def first_class():
    print(Research.file_reader())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_class()