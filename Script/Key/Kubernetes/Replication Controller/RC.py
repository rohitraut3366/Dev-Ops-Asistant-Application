import os

def replication_controller_service(namespace):
    while True:
        print("""
        Enter 0: RUN YAML FILE
        Enter 1: List RC
        Enter 2: List RC with Labels
        Enter 3: Wide List RC 
        Enter 4: Get YAML file for running RC
        Enter 5: Describe RC
        Enter 6: Expose RC
        Enter 7: Delete RC
        Enter 8: Delete ALL RC
        Enter 9: TO EXIT
        """)
        choice = input("Enter your choice: ")
        if choice == '0':
            yml = input("Enter Path of yaml files: \n")
            with open('rc.yml',"w+") as pod_file:
                pod_file.write(yml)
                os.system(f'kubectl apply -f rc.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get rc -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get rc --show-labels -n {namespace}')
        elif choice == '3':
                os.system(f'kubectl get rc -o wide -n {namespace}')
        elif choice == '4':
            rc_name = input("Enter rc name: ")
            os.system(f'kubectl get rc {rc_name} -o yaml -n {namespace}')
        elif choice == '5':
            rc_name = input("Enter rc Name: ")
            os.system(f'kubectl describe {rc_name} -n {namespace}')
        elif choice == '6':
            rc_name = input("Enter rc_name: ")
            expose_type = input("Enter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('nter port number: ') 
            os.system(f'kubectl expose pod/{rc_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {rc_name} -n {namespace}')
        elif choice == '7':
            rc_name = input("Enter pod_name: ")
            os.system(f'kubectl delete rc {rc_name} -n {namespace}')
        elif choice == '8':
            os.system(f'kubectl delete rc --all -n {namespace}')
        else:
            return
replication_controller_service('default')