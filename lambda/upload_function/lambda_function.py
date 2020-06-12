import json
import boto3

BUCKET_NAME = 'clint-weather-data'
FILE_NAME = 'current-weather.json'
s3 = boto3.resource('s3')
    
def lambda_handler(event, context):
    s3.Object(BUCKET_NAME, FILE_NAME).put(Body=event['body'])
    
    return {
        'statusCode': 201
    }
