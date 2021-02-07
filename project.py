import boto3
ec2 = boto3.resource('ec2')
ec2.instances.all()

client = boto3.client('cloudwatch')
for instance in ec2.instances.all():
   print(instance.id)

response = client.get_metric_data(
    MetricDataQueries=[
        
    ]
)