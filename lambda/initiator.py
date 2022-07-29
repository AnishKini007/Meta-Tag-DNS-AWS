
from bs4 import BeautifulSoup
import requests
import json
import os
import boto3

dynamodb= boto3.resource('dynamodb')
TAGABLE= os.environ['TAG_TABLE']

def handle(event, context):
    
    print(event)  
    table= dynamodb.Table(TAGABLE)
    url1=event['queryStringParameters']['url']
    tags=event['queryStringParameters']['tag']
    print(url1)
    print(tags)
    def html(url):

        response = requests.get(url)
        return response.text

    urls= url1     

    htmld= html(urls)

    soup = BeautifulSoup(htmld, 'html.parser')

    for tag in soup.find_all("meta"):
        if tag.get("name",None) == tags :
            CON=tag.get("content",None)
            print("Meta Tag present")
            print(CON)
            table.put_item(
                Item={
                    'name':url1,
                    'tag': tags,
                    'content': CON
                })
            return { 'body': json.dumps(CON) }    
        else:
            print("Meta Tag not found")

