import json
import boto3
import os

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
ddbTableName = 'website'
table = dynamodb.Table(ddbTableName)

# function 
def lambda_handler(event, context):

    ddbResponse = table.update_item(
        Key={
            'pageCount': 'count'
        },
        UpdateExpression='SET visitorCount = visitorCount + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )
    
   
    responseBody = json.dumps({"count": int(ddbResponse["Attributes"]["visitorCount"])})
    
    
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": responseBody
    }

    
    return apiResponse
    