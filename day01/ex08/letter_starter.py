
from sys import argv

def return_letter():
    if len(argv) == 2:
        find_emain = argv[1]
        with open('employees.tsv', 'r') as f:
            for line in f:
                if line.find(find_emain) != -1:
                    name = line[ : line.find("\t")].capitalize()
                    print("Dear", name, "welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
            f.close()

if __name__ == '__main__':
    return_letter()