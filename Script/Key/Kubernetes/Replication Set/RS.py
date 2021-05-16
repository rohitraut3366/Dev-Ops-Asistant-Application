import os

def replication_set_service(namespace):
    while True:
        print("""
        Enter 0: RUN YAML FILE
        Enter 1: List RS
        Enter 2: List RS with Labels
        Enter 3: Wide List RS 
        Enter 4: Get YAML file for running RS
        Enter 5: Describe RS
        Enter 6: Expose RS
        Enter 7: Delete RS
        Enter 8: Delete ALL RS
        Enter 9: TO EXIT
        """)
        choice = input("Enter your choice: ")
        if choice == '0':
            yml = input("Enter Data: \n")
            os.system(f'kubectl apply -f rs.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get rs -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get rs --show-labels -n {namespace}')
        elif choice == '3':
                os.system(f'kubectl get rs -o wide -n {namespace}')
        elif choice == '4':
            rs_name = input("Enter rs name: ")
            os.system(f'kubectl get rs {rs_name} -o yaml -n {namespace}')
        elif choice == '5':
            rs_name = input("Enter rs Name: ")
            os.system(f'kubectl describe {rs_name} -n {namespace}')
        elif choice == '6':
            rs_name = input("Enter rc_name: ")
            expose_type = input("Enter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('Enter port number: ') 
            os.system(f'kubectl expose pod/{rs_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {rs_name} -n {namespace}')
        elif choice == '7':
            rs_name = input("Enter pod_name: ")
            os.system(f'kubectl delete rs {rs_name} -n {namespace}')
        elif choice == '8':
            os.system(f'kubectl delete rs --all -n {namespace}')
        else:
            return
