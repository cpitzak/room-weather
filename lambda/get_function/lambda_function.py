import json
import boto3

BUCKET_NAME = 'clint-weather-data'
FILE_NAME = 'current-weather.json'
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    obj = s3.Object(BUCKET_NAME, FILE_NAME)
    body = obj.get()['Body'].read()
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://clintpitzak.com',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': body
    }
