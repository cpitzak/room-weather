import json
import boto3

def lambda_handler(event, context):
    BUCKET_NAME = 'clint-weather-data'
    FILE_NAME = 'current-weather.json'
    s3 = boto3.resource('s3')
    obj = s3.Object(BUCKET_NAME, FILE_NAME)
    body = obj.get()['Body'].read()
    return {
        'statusCode': 200,
        'body': body
    }
