import boto3

region_name = 'us-east-1'
# Declare boto3 client
client = boto3.client('ec2', region=region_name)

# Get list of all instance IDs
all_instances = client.describe_instances()
all_instances_ids = [x['Instances'][0]['InstanceId'] for x in all_instances['Reservations']]

def event_handler(event, context):
    action=event['action']
    if 'stop' in action.lower():
        client.stop_instances(InstanceIds=all_instances_ids)
        print('stopped your instances: ' + str(all_instances_ids))
    else:
        client.start_instances(InstanceIds=all_instances_ids)
        print('started your instances: ' + str(all_instances_ids))
