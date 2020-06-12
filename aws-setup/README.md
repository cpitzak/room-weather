# Create the Execution role
1. Open [Roles page](https://console.aws.amazon.com/iam/home#/roles$new?step=type)
2. Click create role
3. Select Lambda (allows lambda function to call AWS services on your behalf)
4. Next: Permissions
5. search for "AWSLambdaExecute" and select
6. Next, next
7. Role name: lambda-s3-role
8. Click create role

# Lambda function for upload data
1. Services->Lambda
2. name: upload-weather
3. Python 3.8
4. Use an existing role: lambda-s3-role
5. create function

# Lambda function for getting weather
1. same as "Lambda function for upload data" but with name: get-weather
2. 

# Create S3 bucket
1. Bucket name: clint-weather-data
2. permission as default: block all public access
3. click create bucket

# API Gateway
0. Action->Create resource and then choose a name
1. REST API click build
2. REST api radio selected
3. New API selected
4. API name: room-weather
5. Endpoint type: Regional
6. Click create API
7. Actions->Create Method and select: PUT
8. Integration Type: Lambda Function
9. Check: Use Lambda Proxy Integration
10. lambda function name: upload-weather
11. click save
12. on left side: click Models
13. Click create
14. model name: putWeather
15. content-type: application/json
16. see schema file in this repo named "putWeather"
17. Click on your "PUT" method
18. Method execution
19. Settings, API Key Required: true
20. Request body, content-type: application/json
21. Request body, select model name: putWeather

## Public method for get weather
1. Service->API Gateway
2. Action->Create resource
3. Action->Create Method (see steps from API Gateway)

## Create API Key
1. API->Gateway->room-weather
2. Actions->Create API key
3. name: raspberryPi
4. Auto Generate

## Create Usage Plan
To protect yourself from accidentally calling it too much. This is optional
1. name: RaspberryPiPlan
2. requests per second: 2
3. burst: 3
4. 172,800 requests per day (2 * seconds in a day)
5. Next
6. Add API stage: room-weather
7. Add api key to plan: raspberryPi

## Create Stage
1. name the stage: room-weather
2. Enable throttling: choose a reasonable limit
3. Go to Usage Plan and add this stage to your useage plan

## Certification Manager to for a custom domain name for your API
1. Services->AWS Certification Manager
2. Provision Certificates
3. Request public certificate
4. add three domain scenarios i.e.
    * clintpitzak.com
    * *.clintpitzak.com
    * www.clintpitzak.com
5. Select verification method

## Custom domain name
1. API Gateway->Custom domain names
2. api.clintpitzak.com
3. Regional
4. TLS 1.2
5. clintpitzak.com ACM certificate
6. create
7. copy API Gateway domain name
8. In your domain manager of where you registered your domain name, go to the DNS section. Add CNAME record for your custom domain name. i.e. 
    * name: api.clintpitzak.com.
    * CNAME
    * 10m
    * myapigatewayaddress.amazonaws.com.
    Note: the periods at the end of the domain names are intentional
9. Go back to the custom domain. Click on your custom domain
10. Click API Mapping, add new mapping
11. Select your api and stage