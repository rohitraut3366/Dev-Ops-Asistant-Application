import os


def Key():
    while True:
        os.system('tput setaf 4')
        print("""
                Enter 1 to create Key
                Enter 2 to delete Key
                Enter 3 to describe key pairs
                Enter 4 to exit
            """)
        os.system('tput setaf 7')
        choice = input("        Enter your choice : ")
        if choice == "1":
            key_name = input("\t\tEnter Key-name: ")
            os.system(
                "aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}.pem".format(key_name,
                                                                                                           key_name))
        elif choice == "2":
            key_name = input("\tEnter Key-name: ")
            os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        elif choice == "3":
            os.system("aws ec2 describe-key-pairs")
        elif choice == "4":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def securityGroup():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 To create security Group
        Enter 2 To describe security Group
        Enter 3 To delete security Group
        Enter 4 To add rule of security Group
        Enter 5 To delete rule of security Group
        Enter 6 To exit
        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice")
        if choice == '1':
            description = input("Enter Description of sg : ")
            Group_name = input("Enter sg group Name : ")
            os.system("aws ec2  create-security-group --description {} --group-name {}".format(description, Group_name))
        elif choice == '2':
            os.system("aws ec2 describe-security-groups")
        elif choice == '3':
            Id = input("Enter sg Id: ")
            os.system(" aws ec2 delete-security-group --group-id {}".format(Id))
        elif choice == '4':
            print("\tEnter 1 for ingress \n\tEnter 2 for egress")
            add = input("Enter your choice : ")
            security_id = input("\tEnter security id: ")
            protocol = input("\tEnter protocol: ")
            port = input("\tEnter Port: ")
            cidr = input("\tEnter Cidr: ")
            if add == "1":
                os.system(
                    "aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif add == "2":
                os.system(
                    "aws ec2 authorize-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == '5':
            print("Enter 1 for ingress \nEnter 2 for egress")
            delete = input("Enter your choice : ")
            security_id = input("            Enter security id: ")
            protocol = input("          Enter protocol: ")
            port = input("          Enter Port: ")
            cidr = input("          Enter Cidr: ")
            if delete == "1":
                os.system(
                    "aws ec2 revoke-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif delete == "2":
                os.system("aws ec2 revoke-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                    security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == '6':
            break
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def volume():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 To describe volumes
        Enter 2 To create volumes
        Enter 3 To delete volume
        Enter 4 To attach volume
        Enter 5 To detach volume
        Enter 6 To modify volume
        Enter 7 To exit
            """)
        os.system('tput setaf 7')
        choice = input("Enter your Choice: ")
        if choice == "1":
            os.system("aws ec2 describe-volumes")
        elif choice == "2":
            az = input("Enter AZ : ")
            size = input("size: ")
            os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az, size))
        elif choice == "3":
            volume_id = input("Enter Volume ID : ")
            os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
        elif choice == "4":
            device = input("Enter  device Name: ")
            instance_id = input("Instance ID: ")
            volume_id = input("Volume ID: ")
            os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(device, instance_id,
                                                                                                  volume_id))
        elif choice == "5":
            volume_id = input("Volume ID: ")
            os.system("aws ec2 detach-volume --volume-id {} --force".format(volume_id))
        elif choice == "6":
            print("modify size only supported others features are coming soon")
            size = input("Enter size: ")
            volume_id = input("Enter Volume ID: ")
            os.system("aws ec2 modify-volume --volume-id {} --size {}".format(volume_id, size))
        elif choice == "7":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def instance():
    while True:
        os.system('tput setaf 4')
        print("""
            Enter 1 To get information about your instances
            Enter 2 To launch an EC2 instance
            Enter 3 To Start an instance
            Enter 4 To Stop an instance
            Enter 5 To terminate an instance
            Enter 6 To exit
            """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("aws ec2 describe-instances")
        elif choice == "2":
            image_id = input("Enter image-id : ")
            cnt = int(input("How many instance you want to launch: "))
            key_name = input("Enter your key name: ")
            subnet_id = input("Enter subnet-id : ")
            instance_type = input("Enter instance type: ")
            security_group_id = input("Security Group: ")
            os.system(
                "aws ec2 run-instances --image-id {} --instance-type {}"
                " --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(
                    image_id, instance_type, cnt, subnet_id, key_name, security_group_id))
            print("Instance Launched !!!")
        elif choice == "3":
            id2 = input("Enter your instance id :")
            os.system("aws ec2 start-instances --instance-ids {}".format(id2))
        elif choice == "4":
            id3 = input("Enter your instance id :")
            os.system("aws ec2 stop-instances --instance-ids {}".format(id3))
        elif choice == "5":
            Id = input("Enter instance id: ")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(Id))
        else:
            print("Wrong Choice")
            return
        input("Enter to continue......")
        os.system("clear")


def AMI():
    print("""
    Enter 1 : List All Images
    Enter 2: Describe Images
    Enter 3 : Create Amazon Machine Image
    Enter 4 : Make Image Public
    Enter 5: Make Image Private 
    Enter 6 : Delete Amazon Machine Image
    """)
    choice = input("Enter your Choice: ")
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '1':
        instance_id = input("Enter instance id : ")
        ami_name = input("Enter AMI Name: ")
        description = input("Enter Description of  instance : ")
        os.system("aws ec2 create-image --instance-id {} --name '{}' --description '{}' --no-reboot".format(instance_id, ami_name, description))
    elif choice == '2':
        image_id = input("Enter Image ID: ")
        os.system("aws ec2 deregister-image --image-id {}".format(image_id))
    else:
        print("Wrong Choice")


def Snapshots():
    print("""
    Enter 1 : Create Snapshot
    Enter 2 : Delete Snapshot
    Enter 3 : 
    """)


def ElasticIPS():
    pass


def NetworkInterfaces():
    pass


def LoadBalancers():
    pass


def TargetGroups():
    pass


def AutoScalingLaunchConfiguration():
    pass


def AutoScalingGroups():
    pass
