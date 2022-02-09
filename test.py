import boto3 

def AccessDynmoClient():
    dynamodb = boto3.client('dynamodb')
    ddbTableName = 'website'
    response = dynamodb.describe_table(TableName = ddbTableName)
    return response

def test_table():
    response = AccessDynmoClient()
#    print (response)
#    print (response['Table']['TableName'])
    assert response['Table']['TableName']  == 'website', "Invalid Table"
    
def test_key():
    response = AccessDynmoClient()
#    print (response)
#    print (response['Table']['KeySchema'][0]['AttributeName'])
    assert response['Table']['KeySchema'][0]['AttributeName']  == 'pageCount', "Invalid Key"

def test_value():
    dynamodb = boto3.resource('dynamodb')
    ddbTableName = 'website'
    table = dynamodb.Table(ddbTableName)
    response = table.get_item(Key={'pageCount': "count"})
    # print(response["Item"]["visitorCount"])
    value = type(response["Item"]["visitorCount"])
    value = str(value)
    value = value[16:23]
    # print(value)
    assert value == 'Decimal', "Should be decimal"

    
def test_main(event,context):
    test_table()
    test_key()
    test_value()
    return 'Tests Successful'
