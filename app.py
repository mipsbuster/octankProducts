#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import CfnParameter

from my_widget_service.my_widget_service_stack import MyWidgetServiceStack
from rdstack_bronze import RDSStackBronze
from rdsstack_silver import RDSStackSilver
from rdsstack_gold import RDSStackGold
from my_development_service_stack import MyDevServiceStack
from core_octank_stack import CoreStack

global _custID

prod = core.Environment(account="610880146692", region="us-east-2")
app = core.App()
CoreStack(app,"core", env=prod)
#MyWidgetServiceStack(app, "my-widget-service", env=prod)
RDSStackBronze(app, "product-bronze", env=prod)
RDSStackSilver(app, "product-silver", env=prod)
RDSStackGold(app, "product-gold", env=prod)
#MyDevServiceStack(app, "product-dev", env=prod)

app.synth()
