import os


def pod_service(namespace='default'):
    while True:
        print("""
        Enter 0: run yaml file
        Enter 1: List Pod
        Enter 2: List Pod with Labels
        Enter 3: Wide List Pod 
        Enter 4: Get YAML file for running Pod
        Enter 5: Describe Pod
        Enter 6: Create Pod
        Enter 7: Expose Pod
        Enter 8: Delete Pod
        Enter 9: Delete All Pods
        Enter 10: see Logs of Pod
        Enter 11: To Exit 
        """)
        choice = input("Enter your choice: ")
        if choice == '0':
            yml = input("Enter: \n")
            with open('pod.yml', "w+") as pod_file:
                pod_file.write(yml)
            os.system(f'kubectl apply -f pod.yml -n {namespace}')
        elif choice == '1':
            os.system(f'kubectl get pods -n {namespace}')
        elif choice == '2':
            os.system(f'kubectl get pod --show-labels -n {namespace}')
        elif choice == '3':
            os.system(f'kubectl get pod -o wide -n {namespace}')
        elif choice == '4':
            pod_name = input("Enter pod_name: ")
            os.system(f'kubectl get pod {pod_name} -o yaml -n {namespace}')
        elif choice == '5':
            pod = input("Enter Pod Name: ")
            os.system(f'kubectl describe {pod} -n {namespace}')
        elif choice == '6':
            pod_name = input("Enter pod_name: ")
            image = input('Enter image name: ')
            os.system(f"kubectl run {pod_name} --image {image} -n {namespace}")
        elif choice == '7':
            pod_name = input("Enter pod_name: ")
            expose_type = input("Enter expose type [NodePort/ClusterIP/LoadBalancer]: ")
            port = input('Enter port number: ')
            os.system(f'kubectl expose pod/{pod_name} --type={expose_type} --port={port} -n {namespace}')
            os.system(f'kubectl get svc {pod_name} -n {namespace}')
        elif choice == '8':
            pod_name = input("Enter pod_name: ")
            os.system(f'kubectl delete pod {pod_name} -n {namespace}')
        elif choice == '9':
            os.system(f'kubectl delete pod --all -n {namespace}')
        elif choice == '10':
            pod_name = input("Enter pod_name: ")
            os.system(f'kubectl logs pod {pod_name} -n {namespace}')
        else:
            if choice != "11":
                print("Wrong Choice")
            return
