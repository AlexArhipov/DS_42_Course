# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sys import argv
class Research(object):
    def __init__(self, av_file_path):
        self.file_path = av_file_path
    def file_reader(self):
        try:
            file = open(self.file_path)
        except IOError as e:
            return 'не удалось открыть файл'
        else:
            with open(self.file_path, 'r') as t:
                caunt = 0
                for line in t:
                    caunt += 1
                    if line.find(',') == -1:
                        return 'неверный формат файла'
                    if caunt > 1 and len(line) > 3:
                        line = line[:-1]
                    if (len(line) != 3 or ((line[0] not in '01') or (line[2] not in '01'))) and caunt > 1:
                        return 'неверный формат файла'
                if caunt < 2:
                    return 'неверный формат файла'
                t.close()
            with open(self.file_path, 'r') as f:
                s = ''
                for line in f:
                    s += line
                f.close()
                return s


def first_class():
    if len(argv) == 2:
        a = Research(argv[1])
        print(a.file_reader())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_class()