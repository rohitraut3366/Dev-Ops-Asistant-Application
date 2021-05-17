import os
import subprocess

from script.key_script.linux.logical_volume_manager.lvm import LVM
from script.key_script.linux.webservers.webserver import webserverMain


def key_pass():
    ipAddress = input("Enter IP of target System :")
    username = input("UserName: ")
    auth_type = input("Enter Authentication type-->  [key/password] : ")

    if auth_type.lower() == "key":
        key_path = input("Enter key and path from base directory: ")
        cmd = input("Enter cmd : ")
        os.system(f"ssh -i  {key_path} {username}@{ipAddress} sudo {cmd}")
    elif auth_type.lower() == "password" or auth_type.lower() == "pass":
        print("Setting Up environment please wait")
        subprocess.getoutput("yum install sshpass -y")
        password = input("Enter password: ")
        cmd = input("Enter cmd : ")
        os.system(f"ssh -p {password} {username}@{ipAddress} sudo {cmd}")
    else:
        print("Not Valid")
        return


def linux():
    print("""
    Press 1: For Running any command
    Press 2: For Logical Volume Manager
    Press 3: Apache Webserver Configuration
    Press 4: Exit
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        key_pass()
    elif choice == '2':
        LVM()
    elif choice == '3':
        webserverMain()
    elif choice == '4':
        return
    else:
        print("Wrong Choice!")
    input("Enter to continue...")
    os.system("clear")


