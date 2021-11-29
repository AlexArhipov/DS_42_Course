from make_report import *

class Analytics(Research.Calculations):
    def predict_random(m):
        line = ''
        with open("file.txt", 'w') as f:
            ret = []
            for i in range(m):
                ch = random.randrange(0, 2, 1)
                f.write(line + '\n')
                line = str(ch)+','+str(pow(ch-1, 2))
                ret.append(list(map(int, line.split(','))))
            return (ret)
    # def predict_random(self):
    def predict_last(self):
        if self == 'не удалось открыть файл':
            print('не удалось открыть файл')
            return
        for i in self:
            j = i
        print(j)