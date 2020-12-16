
from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)
from aws_cdk.core import CfnParameter

class RDSStackGold(core.Stack):
    dbid = ''
    def setID(self,idIn):
        self.dbid = idIn
    def getID(self):
        return self.dbid

    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        #vpc = ec2.Vpc(self, "VPC-Customers")
        #vpc = ec2.IVpc("vpc-052b7f771e014e59a")

        #core.Tags.of(rds).add("key", "value", custName='cust1010')

        cust_id = CfnParameter(self, "custId", type="String",
                                          description="The id of the customer.")

        core.Tags.of(self).add("custID", cust_id.value_as_string)

        rds.DatabaseInstance(
            self, "databaseTest",
            database_name="db1",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_12_4
            ),
            vpc=ec2.Vpc.from_lookup(self, vpc_id='vpc-0dd89814b25526eb9', id='vpc-0dd89814b25526eb9',
                                  # This imports the default VPC but you can also
                                  # specify a 'vpcName' or 'tags'.
                                  is_default=False
                                  ),
            port=5432,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.MEMORY6_GRAVITON,
                ec2.InstanceSize.XLARGE4,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=True, multi_az=True
        )
'''
        prod1 = rds.DatabaseInstance(
            self, "databaseProd1",
            database_name="dbprod1",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_16
            ),
            vpc=vpc,
            port=3306,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.MEMORY4,
                ec2.InstanceSize.LARGE,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=False
        )
'''

