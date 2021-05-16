import os

from Compute.EC2.EC2 import EC2Menu


def compute():
    while True:
        os.system('tput setaf 4')
        print('''
                Press 1: EC2
                Press 2: Elastic BeanStalk
                ''')
        os.system('tput setaf 7')
        choice = input("\n Enter Your Choice:")
        if choice == '1':
            EC2Menu()
        elif choice == '2':
            pass
        else:
            print("Wrong choice")
        os.system("clear")
