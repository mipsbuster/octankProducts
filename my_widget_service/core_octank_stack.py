from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)
from aws_cdk.core import CfnParameter

class CoreStack(core.Stack):

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        vpc = ec2.Vpc(self, "VPC-Octank-Customers")
        #core.Tags.of(rds).add("key", "value", custName='cust1010')
        cust_id = CfnParameter(self, "custId", type="String",
                                          description="The id of the customer.")