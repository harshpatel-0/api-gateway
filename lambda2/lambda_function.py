# from GitHub!

import boto3
import json

def lambda_handler(event, context):
    # Bucket
    bucket_name = "hw06-harsh"

    # Create an S3 client
    s3 = boto3.client('s3')

    # List objects in the specified bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Extract only the object keys
    objects = [obj['Key'] for obj in response.get('Contents', [])]

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(objects)
    }
