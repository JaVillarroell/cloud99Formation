import json
import boto3

def handler(event, context):
    return {
        'status code': 200,
        'body': json.dumps("Hello from Lambda")
    }
