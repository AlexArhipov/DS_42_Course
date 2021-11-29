import random

class Research:
    def __init__(self, av_file_path):
        self.file_path = av_file_path
        self.has_header = True
        has_header = True
        self.lists = []

    # @staticmethod
    def file_reader(self):
        try:
            with open(self.file_path, 'r') as t:
                caunt = 0
                for line in t:
                    if caunt == 0 and len(line) < 5:
                        self.has_header = False
                        caunt += 1
                    caunt += 1
                    if line.find(',') == -1:
                        return 'неверный формат файла'
                    if caunt > 1 and len(line) > 3:
                        line = line[:-1]
                    if (len(line) != 3 or ((line[0] not in '01') or (line[2] not in '01'))) and caunt > 1:
                        return 'неверный формат файла'
                if caunt < 2:
                    return 'неверный формат файла'
            self.lists = []
            with open(self.file_path, 'r') as f:
                caunt = 0
                if self.has_header == False:
                    caunt = 1
                for line in f:
                    if caunt > 0:
                        self.lists.append(list(map(int, line.split(','))))
                    caunt += 1
                return self.lists
        except IOError as e:
            return 'не удалось открыть файл'
    class Calculations:
        def __init__(self, ex_lists):
            self.lista = ex_lists
        def counts(self):
            if self=='не удалось открыть файл':
                return
            if isinstance(self, list):
                resh = 0
                orel = 0
                for i in self:
                    cautn = 0
                    for j in i:
                        if cautn == 0:
                            resh += j
                        else:
                            orel += j
                        cautn += 1
                return [resh,orel]
        def fractions(self):
            if self=='не удалось открыть файл':
                print('не удалось открыть файл')
                return
            if isinstance(self, list):
                resh = 0
                orel = 0
                for i in self:
                    cautn = 0
                    for j in i:
                        if cautn == 0:
                            resh += j
                        else:
                            orel += j
                        cautn += 1
                sums = resh + orel
                return [(resh*100)/sums,(orel*100)/sums]