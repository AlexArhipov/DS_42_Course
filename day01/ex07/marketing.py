# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv

def call_center(clients, participants,recipients):
    clients_send_kit = set(clients) - set(recipients)
    print(list(clients_send_kit))

def potential_clients(clients, participants, recipients):
    no_clients = set(participants) - set(clients)
    print(list(no_clients))

def loyalty_program(clients, participants, recipients):
    clients_no_participants = set(clients) - set(participants)
    print(list(clients_no_participants))

def ft_clinet():
    if len(argv) == 2:
        clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
        participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
        recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
        if argv[1] == "call_center":
            call_center(clients, participants, recipients)
        elif argv[1] == "potential_clients":
            potential_clients(clients, participants, recipients)
        elif argv[1] == "loyalty_program":
            loyalty_program(clients, participants, recipients)
        else:
            print("Error name task")
    else:
        print("Error name task")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft_clinet()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
