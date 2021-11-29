from sys import argv
from analytics import *
from make_report import *


def first_class():
    if len(argv) == 2 and len(argv[1].split(','))==2 and (argv[1].split(',')[1]).isdigit():
        try:
            inpt = argv[1].split(',')
            with open(inpt[0], 'r') as t:
                a = Research(inpt[0])
                # print(a.file_reader())
                # print(a.__dict__)
                rez_coin = (a.Calculations.counts(a.file_reader()))
                coin_out_pr = a.Calculations.fractions(a.file_reader())
                rand = Analytics.predict_random(int(inpt[1]))
                resh = 0
                orel = 0
                for i in rand:
                    cautn = 0
                    for j in i:
                        if cautn == 0:
                            resh += j
                        else:
                            orel += j
                        cautn += 1
                # Analytics.predict_last(a.file_reader())
                sum_coin = int(rez_coin[0]) + int(rez_coin[1])
                resh_coin = rez_coin[0]
                orel_coin = rez_coin[1]
                resh_pr = coin_out_pr[0]
                orel_pr = coin_out_pr[1]
                tekst = "We have made "+ str(sum_coin) +" observations from tossing a coin: "+ str(orel_coin)+\
                " of them were tails and "+ str(resh_coin)+ " of them were heads.The probabilities are "+\
                str(orel_pr) +"% and " + str(resh_pr)+ "%, respectively.Our forecast is that in the next "+ \
                str(inpt[1]) + " observations we will have: " + str(resh) + " tail and "+ str(orel) + " heads."
                print(tekst)
        except:
            return

if __name__ == '__main__':
    first_class()