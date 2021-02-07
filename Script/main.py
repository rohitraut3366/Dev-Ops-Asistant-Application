import getpass, os, subprocess

password = getpass.getpass()
if password != "123":
    exit()
path = input("How you want to communate with this program: [Voice/Keyboard] :")
if path.lower() == 'voice':
    pass
elif path.lower() == 'keyboard':
    pass
else:
    print("Wrong Choice..")