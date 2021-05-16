import os

from compute.compute import compute


def Aws():

    os.system("aws configure")
    while True:
        os.system('tput setaf 4')
        print('''
                Press 1: Compute
                Press 2: Networking and Content Deliver
                Press 3: Exit from this menu
                ''')
        os.system('tput setaf 7')
        choice = input("\n Enter Your Choice:")
        if choice == '1':
            compute()    
        elif choice == '2':
            pass
        else:
            if choice != '3':
                print("Wrong choice")
            return
        os.system("clear")
Aws()