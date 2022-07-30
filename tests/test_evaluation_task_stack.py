from aws_cdk.assertions import Template , Match

from evaluation_task.evaluation_task_stack import EvaluationTaskStack

from tests import app

stack_= EvaluationTaskStack(app, 'EvaluationTaskStack')
template = Template.from_stack(stack_)
DYNAMODB_TABLE = 'AWS::DynamoDB::Table'

def test_keyschema():
    template.has_resource_properties(
        DYNAMODB_TABLE,
        {'keySchema': Match.array_equals(
            [{'AttributeName': 'name', 'KeyType': 'HASH'}]
        )}
    )

# from evaluation_task.evaluation_task_stack import EvaluationTaskStack

# # example tests. To run these tests, uncomment this file along with the example
# # resource in evaluation task/evaluation task_stack.py
# def test_sqs_queue_created():
#     app = core.App()
#     stack = EvaluationTaskStack(app, "evaluation-task")
#     template = assertions.Template.from_stack(stack)

# #     template.has_resource_properties("AWS::SQS::Queue", {
# #         "VisibilityTimeout": 300
# #     })

# import unittest
# import dns.resolver
# import boto3
# import os
# import json

# from lambdas.Dnslocator import handler

# from lambdas.initiator import handle

# class TestApp(unittest.TestCase):

#     def meta_event(self, domain, txt ):
#         return{
            
#         "resource":"/record",
#         "path":"/record",
#         "httpMethod":"POST",
#         "headers":{
#             "Accept":"*/*",
#             "Accept-Encoding":"gzip, deflate, br",
#             "CloudFront-Forwarded-Proto":"https",
#             "CloudFront-Is-Desktop-Viewer":"true",
#             "CloudFront-Is-Mobile-Viewer":"false",
#             "CloudFront-Is-SmartTV-Viewer":"false",
#             "CloudFront-Is-Tablet-Viewer":"false",
#             "CloudFront-Viewer-ASN":"24309",
#             "CloudFront-Viewer-Country":"IN",
#             "Host":"9rzvsutt1m.execute-api.us-east-1.amazonaws.com",
#             "Postman-Token":"ae70f60a-57c6-4e7a-8761-f1ed89e1fa78",
#             "User-Agent":"PostmanRuntime/7.29.2",
#             "Via":"1.1 5bf0b8a023a727320fd7ec1cb14d300a.cloudfront.net (CloudFront)",
#             "X-Amz-Cf-Id":"ge4p_AunvYV1p1A7YUATHLGxOoMm-QkXTJiLiarpKO1MjIcieK8QXQ==",
#             "X-Amzn-Trace-Id":"Root=1-62e3c625-107069f62c56a8214fad37de",
#             "X-Forwarded-For":"49.206.7.146, 64.252.145.147",
#             "X-Forwarded-Port":"443",
#             "X-Forwarded-Proto":"https"
#         },
#         "multiValueHeaders":{
#             "Accept":[
#                 "*/*"
#             ],
#             "Accept-Encoding":[
#                 "gzip, deflate, br"
#             ],
#             "CloudFront-Forwarded-Proto":[
#                 "https"
#             ],
#             "CloudFront-Is-Desktop-Viewer":[
#                 "true"
#             ],
#             "CloudFront-Is-Mobile-Viewer":[
#                 "false"
#             ],
#             "CloudFront-Is-SmartTV-Viewer":[
#                 "false"
#             ],
#             "CloudFront-Is-Tablet-Viewer":[
#                 "false"
#             ],
#             "CloudFront-Viewer-ASN":[
#                 "24309"
#             ],
#             "CloudFront-Viewer-Country":[
#                 "IN"
#             ],
#             "Host":[
#                 "9rzvsutt1m.execute-api.us-east-1.amazonaws.com"
#             ],
#             "Postman-Token":[
#                 "ae70f60a-57c6-4e7a-8761-f1ed89e1fa78"
#             ],
#             "User-Agent":[
#                 "PostmanRuntime/7.29.2"
#             ],
#             "Via":[
#                 "1.1 5bf0b8a023a727320fd7ec1cb14d300a.cloudfront.net (CloudFront)"
#             ],
#             "X-Amz-Cf-Id":[
#                 "ge4p_AunvYV1p1A7YUATHLGxOoMm-QkXTJiLiarpKO1MjIcieK8QXQ=="
#             ],
#             "X-Amzn-Trace-Id":[
#                 "Root=1-62e3c625-107069f62c56a8214fad37de"
#             ],
#             "X-Forwarded-For":[
#                 "49.206.7.146, 64.252.145.147"
#             ],
#             "X-Forwarded-Port":[
#                 "443"
#             ],
#             "X-Forwarded-Proto":[
#                 "https"
#             ]
#         },
#         "queryStringParameters":{
#             "domain":domain,
#             "txtrecord":txt
#         },
#         "multiValueQueryStringParameters":{
#             "domain":[
#                 "flipkart.com"
#             ],
#             "txtrecord":[
#                 "\"clojars flipkartoss\""
#             ]
#         },
#         "pathParameters":"None",
#         "stageVariables":"None",
#         "requestContext":{
#             "resourceId":"q4skoy",
#             "resourcePath":"/record",
#             "httpMethod":"POST",
#             "extendedRequestId":"WBvl4EsvIAMF_Rg=",
#             "requestTime":"29/Jul/2022:11:36:05 +0000",
#             "path":"/prod/record",
#             "accountId":"237743610432",
#             "protocol":"HTTP/1.1",
#             "stage":"prod",
#             "domainPrefix":"9rzvsutt1m",
#             "requestTimeEpoch":1659094565472,
#             "requestId":"02203448-47b0-4844-b5cc-b5a96b815d81",
#             "identity":{
#                 "cognitoIdentityPoolId":"None",
#                 "accountId":"None",
#                 "cognitoIdentityId":"None",
#                 "caller":"None",
#                 "sourceIp":"49.206.7.146",
#                 "principalOrgId":"None",
#                 "accessKey":"None",
#                 "cognitoAuthenticationType":"None",
#                 "cognitoAuthenticationProvider":"None",
#                 "userArn":"None",
#                 "userAgent":"PostmanRuntime/7.29.2",
#                 "user":"None"
#             },
#             "domainName":"9rzvsutt1m.execute-api.us-east-1.amazonaws.com",
#             "apiId":"9rzvsutt1m"
#         },
#         "body":"None",
#         "isBase64Encoded":False
#         }
               
        

#     def test_meta(self):

#         response= handler(self.meta_event("flipkart.com",'"clojars flipkartoss"'), "")
#         expected_response = {
#             "\"clojars flipkartoss\""
#         }

#         self.assertEqual(response, expected_response)