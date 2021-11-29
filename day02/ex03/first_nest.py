from sys import argv

class Research:
    def __init__(self, av_file_path):
        self.file_path = av_file_path
        self.has_header = True
        has_header = True
        self.lists = []

    # @staticmethod
    def file_reader(self):
        try:
            file = open(self.file_path)
        except IOError as e:
            return 'не удалось открыть файл'
        else:
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
            t.close()
            self.lists = []
            with open(self.file_path, 'r') as f:
                caunt = 0
                if self.has_header == False:
                    caunt = 1
                for line in f:
                    if caunt > 0:
                        self.lists.append(list(map(int, line.split(','))))
                    caunt += 1
                f.close()
                return self.lists
    class Calculations:
        def __init__(self, ex_lists):
            self.lista = ex_lists
        def counts(self):
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
                print(resh,orel)
        def fractions(self):
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
                print((resh*100)/sums,(orel*100)/sums)

def first_class():
    if len(argv) == 2:
        a = Research(argv[1])
        print(a.file_reader())
        # print(a.__dict__)
        a.Calculations.counts(a.file_reader())
        a.Calculations.fractions(a.file_reader())

if __name__ == '__main__':
    first_class()