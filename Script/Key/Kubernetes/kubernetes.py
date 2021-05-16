import os
from Installation.kube_installation import installation
from Nodes.node import node_service
from PV.PV import pv_service
from Pods.Pod import pod_service
from PVC.PVC import pvc_service
from ReplicationController.RC import replication_controller_service
from ReplicationSet.RS import replication_set_service
from Secret.Secret import secret_service
from Services.Services import service_service
from configure_client.configure_client import configure_client_service
from role_role_bindings.role_role_bindings import role_role_bindings_service


def kube_menu():
    while True:
        print("""
        Enter 1: For install Kubernetes multi Node Cluster
        Enter 2: For configure Client Program in your system
        Enter 3: For Pod
        Enter 4: For PVC #TO DO: implementation
        Enter 5: For PV #TO DO: Impl
        Enter 6: For ReplicationController
        Enter 7: For Replica Set
        Enter 8: For Secret #TO DO: IMPL
        Enter 9: For Service #TO DO: IMPL
        Enter 10: For Node #TO DO: IMPL
        Enter 11: Role and ROle Bindings #TO DO: IMPL
        Enter 12: Return to Previous Menu
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            installation()

        elif choice == '2':
            configure_client_service()
        elif choice == '3':
            pod_service()

        elif choice == '4':
            pvc_service()

        elif choice == '5':
            pv_service()

        elif choice == '6':
            replication_controller_service()

        elif choice == '7':
            replication_set_service()

        elif choice == '8':
            secret_service()

        elif choice == '9':
            service_service()

        elif choice == '10':
            node_service()

        elif choice == '11':
            role_role_bindings_service()

        else:
            if choice != '12':
                print("Wrong Choice!")
            return
