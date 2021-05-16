import json
import os
import subprocess


def Key():
    while True:
        os.system('tput setaf 4')
        print("""
        Press 1: to create Key
        Press 2: to delete Key
        Press 3: to describe key pairs
        Press 4: Exit from this menu
        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice : ")
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
        Press 1: Create security Group
        Press 2: Describe security Group
        Press 3: Delete security Group
        Press 4: Add rule of security Group
        Press 5: Delete rule of security Group
        Press 6: Exit from this menu
        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice")
        if choice == '1':
            description = input("Enter Description of sg : ")
            group_name = input("Enter sg group Name : ")
            os.system("aws ec2  create-security-group --description {} --group-name {}".format(description, group_name))
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
        Enter 1: Describe volumes
        Enter 2: Create volumes
        Enter 3: Delete volume
        Enter 4: Attach volume
        Enter 5: Detach volume
        Enter 6: Modify volume
        Enter 7: Transfer volume to other AZ
        Enter 8: Transfer volume to Other Region
        Press 9: Exit from this menu
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
        elif choice == "7" or choice == "8":
            volume_id = input("Enter Volume ID: ")
            output = json.loads(subprocess.getout('aws ec2 describe-volumes --volume-ids {}'.format(volume_id)))
            if choice == "7":
                az = input("Enter availability zone: ")
                os.system("aws ec2 create-volume --availability-zone {} --snapshot-id {}".format(az,
                                                                                                 output["Volumes"][0][
                                                                                                     'SnapshotId']))
            if choice == '8':
                source_region = input("Enter source region : ")
                source_snapshot = input("Enter source snapshot id: ")
                destination_region = input("Enter destination region: ")
                os.system(
                    "aws ec2 copy-snapshot --source-region  {} --source-snapshot-id {} --destination-region {} ".format(
                        source_region, source_snapshot, destination_region))
            subprocess.getout("aws")
        elif choice == "9":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def instance():
    while True:
        os.system('tput setaf 4')
        print("""
            Press 1: Get information about your instances
            Press 2: launch an EC2 instance
            Press 3: Start an instance
            Press 4: Stop an instance
            Press 5: Terminate an instance
            Press 6: Exit from this menu
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
    while True:
        print("""
        Press 1: Describe Images
        Press 2: Create Amazon Machine Image
        Press 3: Make Image Public
        Press 4: Make Image Private 
        Press 5: Delete Amazon Machine Image
        Press 6: Exit from this menu
        """)
        choice = input("Enter your Choice: ")
        if choice == '1':
            os.system("aws ec2 describe-images --image-ids {}".format(input("Enter image id: ")))
        elif choice == '2':
            instance_id = input("Enter instance id : ")
            ami_name = input("Enter AMI Name: ")
            description = input("Enter Description of  instance : ")
            os.system(
                "aws ec2 create-image --instance-id {} --name '{}' --description '{}' --no-reboot".format(instance_id,
                                                                                                          ami_name,
                                                                                                          description))
        elif choice == '3':
            image_id = input("Enter Image ID: ")
            os.system("aws ec2 deregister-image --image-id {}".format(image_id))
        else:
            if choice != '6':
                print("Wrong choice")
            return
        input("Enter to continue......")
        os.system("clear")


def Snapshots():
    while True:
        print("""
            Press 1: Display All Snapshot
            Press 2: Display snapshot attribute
            Press 3: create-snapshot
            Press 4: delete-snapshot
            Press 5: copy-snapshot
            Press 6: return
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            os.system("aws ec2 describe-snapshots")
        elif choice == '2':
            attribute = input("Enter attribute : ")
            snapshot_id = input("Enter snapshot_id: ")
            os.system(
                "aws ec2 describe-snapshot-attributes --attribute {}   --snapshot-id {}".format(attribute, snapshot_id))
        elif choice == '3':
            volume_id = input("volume_id : ")
            description = input("Snapshot description: ")
            key, value = input("Enter tag key and value: eg key=value ").split("=")
            os.system(
                f"aws ec2 create-snapshot --volume-id {volume_id} --description {description} --tag-specifications "
                f"'ResourceType=snapshot,Tags=[Key={key}, Value={value}]'")
        elif choice == '4':
            snapshot_id = input("Enter snapshot_id: ")
            os.system(f"aws ec2 delete-snapshot --snapshot-id {snapshot_id}")
        elif choice == '5':
            source_region = input("Enter source region : ")
            source_snapshot = input("Enter source snapshot id: ")
            destination_region = input("Enter destination region: ")
            os.system(
                "aws ec2 copy-snapshot --source-region  {} --source-snapshot-id {} --destination-region {} ".format(
                    source_region, source_snapshot, destination_region))
        else:
            if choice != '6':
                print("Wrong Choice")
            return
        input("Enter to continue......")
        os.system("clear")


def ElasticIPS():
    while True:
        print("""
        Enter 1: Display All IP
        Enter 2: Allocate ElasticIPS
        Enter 3: Associate ElasticIPS
        Enter 4: disassociate-address ElasticIPS
        Enter 5: release-address ElasticIPS
        Press 6: return
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            os.system("aws ec2 describe-addresses")
        elif choice == '2':
            os.system("aws ec2 allocate-address")
        elif choice == '3':
            instance_id = input("instance id: ")
            ipaddress = input("Elastic ip address: ")
            os.system(f"aws ec2 associate-address --instance-id {instance_id} --public-ip {ipaddress}")
        elif choice == '4':
            ipaddress = input("Elastic ip address: ")
            os.system(f"aws ec2 disassociate-address --public-ip {ipaddress}")
        elif choice == '5':
            ipaddress = input("Elastic ip address: ")
            os.system(f"aws ec2 release-address --public-ip {ipaddress}")
        else:
            return
        input("Enter to continue......")
        os.system("clear")


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


def EC2Menu():
    while True:
        os.system('tput setaf 4')
        print('''
                Press 1: FOR KEY PAIR
                Press 2: FOR SECURITY GROUP	
                Press 3: FOR EC2 INSTANCES
                Press 4: FOR VOLUMES
                Press 5: FOR AMI
                Press 6: FOR Snapshot
                Press 7: FOR Elastic IPS
                Press 8: FOR Network InterFaces
                Press 9: FOR Target Groups
                Press 10: FOR Auto Scaling Launch Configuration
                Press 11: FOR Auto Scaling Group
                Press 12: RETURN
                ''')
        os.system('tput setaf 7')
        choice = input("\n Enter Your Choice:")
        if choice == '1':
            Key()
        elif choice == '2':
            securityGroup()
        elif choice == '3':
            instance()
        elif choice == '4':
            volume()
        elif choice == '5':
            AMI()
        elif choice == '6':
            Snapshots()
        elif choice == '7':
            ElasticIPS()
        elif choice == '8':
            NetworkInterfaces()
        elif choice == '9':
            TargetGroups()
        elif choice == '10':
            AutoScalingLaunchConfiguration()
        elif choice == '11':
            AutoScalingGroups()
        elif choice == '12':
            return
        else:
            print("Wrong choice")
        os.system("clear")
