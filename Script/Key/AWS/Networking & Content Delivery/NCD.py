import os
from CloudFront import CloudFront
from Route53 import Route53
from VPC import VPC

while True:
    print("""
    Press 1: CloudFormation 
    Press 2: Route53
    Press 3: VPC 
    """)
    choice = input("Enter your Choice: 1")
    if choice == '1':
        CloudFront.cloudFront()
    elif choice == '2':
        Route53.Route53()
    elif choice == '3':
        VPC.VPC()
    else:
        exit(0)
