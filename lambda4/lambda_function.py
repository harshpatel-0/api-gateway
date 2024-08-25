# from GitHub

import boto3
import json

def lambda_handler(event, context):

    # Bucket
    bucket_name = "hw06-harsh"
    
    if 'pathParameters' not in event or 'object-name' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': "Missing 'object-name' path parameter"})
        }

    object_name = event['pathParameters']['object-name']

    s3 = boto3.client('s3')

    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        response_message = f"Object '{object_name}' successfully deleted from '{bucket_name}'"
        status_code = 200
    except s3.exceptions.NoSuchKey:
        response_message = f"Object '{object_name}' not found in '{bucket_name}'."
        status_code = 404
    except Exception as e:
        response_message = f"Error deleting object '{object_name}': {str(e)}"
        status_code = 500

    return {
        'statusCode': status_code,
        'body': json.dumps({'message': response_message})
    }
