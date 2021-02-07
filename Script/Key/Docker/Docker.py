"""
Enter 1 : Install Docker
Enter 2 : Image Operation
Enter 3 : Container Operation
Enter 5 :
"""

def main():
    serverIp = input()
    remoteUser = input()
    authType = input('Enter type of authentication  [password/key]: ')
    if authType.lower() == 'password':
        remoteUserPassword = input('Enter remote user password: ')
    elif authType.lower() == 'key':
        Key_location = input('Enter key location from / : ')
    else:
        print('Wrong Input')
    with open(''):
        file.

