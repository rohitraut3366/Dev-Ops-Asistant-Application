import os

from key_script.aws.compute.compute import compute


def Aws():
    os.system("clear")
    os.system("aws configure")
    while True:
        os.system('tput setaf 4')
        print('''
\tPress 1: Compute\n\tPress 2: Networking and Content Deliver # In Progress\n\tPress 3: Exit from this menu
                ''')
        os.system('tput setaf 7')
        choice = input("\n\tEnter Your Choice:")
        if choice == '1':
            compute()
        elif choice == '2':
            pass
        elif choice == '3':
            return
        else:
            print("\tWrong choice")
            print("\tTry Again")
        os.system("clear")
