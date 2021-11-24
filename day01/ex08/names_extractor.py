# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sys import argv

def return_csv():
    if len(argv) == 2:
        find_path = argv[1]
        with open('employees.tsv', 'w') as fs:
            fs.write("Name" + '\t' + "Surname" + '\t' + "E-mail" + '\n')
            with open(find_path, 'r') as f:
                for line in f:
                    e_mail = line[:-1]
                    name = line[ : line.find(".")].capitalize()
                    line = line[len(name): ]
                    surname = line[1 : line.find("@")].capitalize()
                    fs.write(name + '\t' + surname + '\t' + e_mail + '\n')
                f.close()
            fs.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    return_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
