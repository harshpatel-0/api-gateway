# from GitHub

import boto3
import base64
import json

def lambda_handler(event, context):
    # Bucket
    bucket_name = "hw06-harsh"

    # Check if the body is present in the event
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': "Missing request body"})
        }

    body = json.loads(event['body'])

    # Check if 'file_name' and 'body' are present in the body
    if 'file_name' not in body or 'body' not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': "Missing 'file_name' or 'body' in the request body"})
        }

    file_name = body['file_name']
    file_content_encoded = body['body']

    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Decode the file content from base64
        file_content = base64.b64decode(file_content_encoded)

        # Upload the file to the specified bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        response_message = f"File '{file_name}' successfully uploaded to '{bucket_name}'"
        status_code = 200
    except Exception as e:
        response_message = f"Error uploading object '{file_name}': {str(e)}"
        status_code = 500

    # Return a response
    return {
        'statusCode': status_code,
        'body': json.dumps({'message': response_message})
    }
