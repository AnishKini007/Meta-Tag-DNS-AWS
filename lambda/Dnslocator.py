import dns.resolver
import boto3
import os
import json

dynamodb= boto3.resource('dynamodb')
DNSTABLE= os.environ['DNS_TABLE']

def handler(event, context):
    table= dynamodb.Table(DNSTABLE)
    print(event)
    domain=event['queryStringParameters']['domain']
    txt=event['queryStringParameters']['txtrecord']
    ids='TXT'

    resolve=dns.resolver.resolve(domain,ids)
    for data in resolve:
        strn= str(data)
        print(ids, ':', strn)
        if strn == txt:
            print("You found it")
            table.put_item(
                Item={
                    'name':domain,
                    'type':ids,
                    'record':strn
                }
            )
            return { 'body': json.dumps(strn) }        
    
        else:
            print("Not the right record")
        