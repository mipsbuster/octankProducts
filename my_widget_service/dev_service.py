from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_ec2 as ec2,
                     aws_rds as rds,
                     aws_lambda as lambda_)
from aws_cdk.core import CfnParameter

class DevService(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        vpc = ec2.Vpc(self, "VPC-Octank-DEV",cidr="192.168.0.0/24",)

        bucket = s3.Bucket(self, "DevStore")

        handler = lambda_.Function(self, "DevHandler",
                    runtime=lambda_.Runtime.NODEJS_10_X,
                    code=lambda_.Code.asset("resources"),
                    handler="dev.main",
                    environment=dict(
                    BUCKET=bucket.bucket_name)
                    )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(self, "dev-api",
                  rest_api_name="Dev Service",
                  description="This service serves dev.")

        get_devs_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_devs_integration)   # GET /

        dev = api.root.add_resource("{id}")

        # Add new dev to bucket with: POST /{id}
        post_dev_integration = apigateway.LambdaIntegration(handler)

        # Get a specific dev from bucket with: GET /{id}
        get_dev_integration = apigateway.LambdaIntegration(handler)

        # Remove a specific dev from the bucket with: DELETE /{id}
        delete_dev_integration = apigateway.LambdaIntegration(handler)

        dev.add_method("POST", post_dev_integration);  # POST /{id}
        dev.add_method("GET", get_dev_integration);  # GET /{id}
        dev.add_method("DELETE", delete_dev_integration);  # DELETE /{id}

        rds.DatabaseInstance(
            self, "database-dev01",
            database_name="db1",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_12_4
            ),
            vpc=vpc,
            port=5432,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.MEMORY4,
                ec2.InstanceSize.LARGE,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=False
        )