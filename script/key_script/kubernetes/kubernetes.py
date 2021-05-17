from configure_client.configure_client import configure_client_service
from installation.kube_installation import installation
from nodes.node import node_service
from persistant_volume.persistant_volume import pv_service
from persistant_volume_claim.persistant_volume_claim import pvc_service
from pods.pod import pod_service
from replication_controller.replication_controller import replication_controller_service
from replication_set.replica_set import replication_set_service
from role_role_bindings.role_role_bindings import role_role_bindings_service
from secret.secret import secret_service
from service.services import service_service


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
