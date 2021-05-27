import os


def configure_client_service():
    print("""
    Press 1: Display Current Context
    Press 2: Delete cluster
    Press 3: Delete Context
    Press 4: Delete user
    Press 5: rename context
    Press 6: set an individual value in a config file
    Press 7: set Cluster
    Press 8: Set context
    Press 9: set Credentials
    Press 10: Unset individual Value
    Press 11: use context
    Press 12: View
    Press 13: return previous menu
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        os.system("kubectl config current-context")
    elif choice == '2':
        os.system(f"kubectl config delete-cluster {input('Enter cluster name: ')}")
    elif choice == '3':
        os.system(f"kubectl config delete-context {input('Enter context name: ')}")
    elif choice == '4':
        os.system(f"kubectl config delete-user {input('Enter user name: ')}")
    elif choice == '5':
        os.system(f"kubectl config rename-context {input('Enter old context name: ')}"
                  f" {input('Enter new context name: ')}")
    elif choice == '6':
        os.system(f"kubectl config set {input('Enter key')} {input('Enter value')} {input('Extra options: ')}")
    elif choice == '7':
        os.system(f"kubectl config set-cluster {input('cluster name: ')}  "
                  f"--certificate-authority={input('path/to/certificate/authority: ')} --embed-certs")
    elif choice == '8':
        os.system(f"kubectl config set-context {input('context name: ')} "
                  f" --cluster={input('cluster nickname')}"
                  f"--user={input('user nickname: ')}"
                  f"--namespace={input('namespace: ')}")
    elif choice == '9':
        os.system(f"kubectl config set-credentials {input('Enter credentials ref name: ')} "
                  f"--client-certificate={input('path to credentials: ')} "
                  f"--client-key={input('client key : ')}"
                  f"--username={input('username: ')} ")
    elif choice == '10':
        os.system(f"kubectl config unset {input('Enter key to unset: ')}")
    elif choice == '11':
        os.system(f'kubectl config use-context {input("Enter context name: ")}')
    elif choice == '12':
        os.system(f"kubectl config view")
    elif choice == '13':
        return
    else:
        print("wrong choice! try again...")


