# from GitHub!

import boto3
import json

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all buckets
    bucket_list = s3.list_buckets()

    # Extract bucket names
    buckets = [bucket['Name'] for bucket in bucket_list['Buckets']]

    # Return the list of bucket names in JSON format
    return {
        'statusCode': 200,
        'body': json.dumps(buckets)
    }
