from aws_cdk import core
from . import widget_service
from aws_cdk.core import CfnParameter

class MyWidgetServiceStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cust_id = CfnParameter(self, "custId", type="String",
                                          description="The id of the customer.")
        product_id = CfnParameter(self, "prodId", type="String",
                                          description="The id of the prod.")

        core.Tags.of(self).add("custID", cust_id.value_as_string)
        widget_service.WidgetService(self, "WidgetsService")

        print(cust_id.value_as_string)





