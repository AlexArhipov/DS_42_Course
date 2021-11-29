
class Must_read(object):
    try:
        with open('data.csv', 'r') as f:
            for line in f:
                print(line, end='')
    except:
        print('Нет файла')

def first_class():
    Must_read

if __name__ == '__main__':
    first_class()
