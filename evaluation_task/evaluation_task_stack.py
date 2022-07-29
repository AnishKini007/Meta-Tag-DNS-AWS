from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _alambda,
    aws_dynamodb as _dynamodb,
    aws_apigateway as api_gw
)
from constructs import Construct

class EvaluationTaskStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tag_table = _dynamodb.Table(self, "Meta_Table",
        partition_key=_dynamodb.Attribute(name="name",type=_dynamodb.AttributeType.STRING))

        dns_table= _dynamodb.Table(self, "DNS_Table",
        partition_key= _dynamodb.Attribute(name="name",type=_dynamodb.AttributeType.STRING))

        dualist= _alambda.PythonFunction(
            self,
            "Initiator",
            entry="./lambda/",
            runtime=_lambda.Runtime.PYTHON_3_9,
            index="initiator.py",
            handler="handle"
        )

        sentinel= _alambda.PythonFunction(
            self,
            "dnslocator",
            entry="./lambda/",
            runtime= _lambda.Runtime.PYTHON_3_9,
            index="Dnslocator.py",
            handler="handler"
        )

        dualist.add_environment("TAG_TABLE",tag_table.table_name)
        sentinel.add_environment("DNS_TABLE",dns_table.table_name)

        tag_table.grant_read_write_data(dualist)
        dns_table.grant_read_write_data(sentinel)

        TAG= api_gw.LambdaRestApi(
            self,
            'Meta-Api',
            handler=dualist,
            proxy=False
        )
        Tags= TAG.root.add_resource("tags")
        Tags.add_method("POST")

        DNS= api_gw.LambdaRestApi(
            self,
            'DNS-Api',
            handler=sentinel,
            proxy=False
        )
        record= DNS.root.add_resource("record")
        record.add_method("POST")
        

        

        

        
