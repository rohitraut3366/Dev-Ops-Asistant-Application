import getpass

from key_script.aws.aws_menu import Aws
from key_script.docker.docker import dockerMain
from key_script.hadoop.hadoop import HadoopMainMenu
from key_script.kubernetes.kubernetes import kube_menu
from key_script.linux.linux_menu import linux

password = getpass.getpass()
if password != "123":
    exit()
path = input("How you want to communicate with this program: [Voice/Keyboard] :")
if path.lower() == 'voice':
    pass
elif path.lower() == 'keyboard':
    while True:
        print("""
Press 1 : AWS
Press 2 : Docker
Press 3 : Hadoop
Press 4 : Kubernetes
Press 5 : Linux/web server
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            Aws()
        elif choice == '2':
            dockerMain()
        elif choice == '3':
            HadoopMainMenu()
        elif choice == '4':
            kube_menu()
        elif choice == '5':
            linux()
        elif choice == '6':
            exit(0)
        else:
            print("Wrong Choice!")

else:
    print("Wrong Choice..")


