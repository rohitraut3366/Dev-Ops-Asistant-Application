import getpass
import os
import subprocess




def webserverMain():
    while True:
        print("\n\t\t\tEnter 1 to Configure on Local System\n\t\t\tEnter 2 to Configure on remote system\n\t\t\tEnter 3 to configure on docker container\n\t\t\tEnter 4 to return")

        choice = input("\t\t\tEnter  your choice: ")
        if choice == "1":
            output = os.system("cat /etc/release-os")
            container_name = input("\t\t\tEnter container name/id: ")
            # LocalwebDocker(output, container_name)
        elif choice == "2":
            ip = input("\t\t\tEnter IP address: ")
            username = input("\t\t\tEnter username: ")
            key_or_pass = input("\t\t\tLogin in VM using key/password: ")
            if key_or_pass == "password":
                password = getpass.getpass()
                output = subprocess.getoutput(
                    "sshpass -p {} ssh {}@{} cat /etc/release-os".format(password, username, ip))
                # remoteWbs(output, username, password, ip)
            elif key_or_pass.lower() == "key":
                path = input("\t\t\tEnter remote os login key path [path/key.pem] ")
                output = subprocess.getoutput("ssh -i {} {}@{} cat /etc/release-os".format(path, username, ip))
                # cloudWbs(output, username, path, ip)
            else:
                print("\t\t\tWrong choice")
        elif choice == "3":
            vm = input("\t\t\tVM is local/remote where docker is running : ")
            if vm == "local":
                con_name = input("\t\t\tEnter container name/ID :")
                output = subprocess.getoutput("docker exec {} cat /etc/release-os".format(con_name))
                # LocalwebDocker(output, con_name)
            elif vm == "remote":
                ip = input("\t\t\tEnter VM IP address: ")
                username = input("\t\t\tEnter username: ")
                key_or_pass = input("\t\t\tLogin to VM using key/password: ")
                if key_or_pass == "password":
                    password = input("\t\t\tEnter vm password: ")
                    con_name = input("\t\t\tEnter container name: ")
                    output = subprocess.getoutput(
                        "sshpass -p {} ssh {}@{} docker exec {} cat /etc/release-os".format(password, username, ip,
                                                                                            con_name))
                    # PasswordwebDocker(username, password, ip, output, con_name)
                elif key_or_pass.lower() == "key":
                    path = input("\t\t\tEnter key path [path/key.pem]")
                    con_name = input("\t\t\tEnter container Name: ")
                    output = subprocess.getoutput(
                        "ssh -i {} {}@{} docker exec {} cat /etc/release-os".format(path, username, ip, con_name))
                    # KeywebDocker(path, username, ip, output, con_name)
                else:
                    print("\t\t\tWrong choice!")
            else:
                print("\t\t\tWrong choice!")
        else:
            return
