# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json

from . import AWSObject


class AutoScalingGroup(AWSObject):
    props = {
        'AvailabilityZones': (list, True),
        'Cooldown': (basestring, False),
        'DesiredCapacity': (basestring, False),
        'HealthCheckGracePeriod': (int, False),
        'HealthCheckType': (basestring, False),
        'LaunchConfigurationName': (basestring, True),
        'LoadBalancerNames': (list, False),
        'MaxSize': (basestring, True),
        'MinSize': (basestring, True),
        'NotificationConfiguration': (basestring, False),
        'Tags': (list, True),
        'VPCZoneIdentifier': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::AutoScalingGroup"
        sup = super(AutoScalingGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class LaunchConfiguration(AWSObject):
    props = {
        'BlockDeviceMappings': (list, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceMonitoring': (bool, False),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'RamDiskId': (basestring, False),
        'SecurityGroups': (list, False),
        'SpotPrice': (basestring, False),
        'UserData': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::LaunchConfiguration"
        sup = super(LaunchConfiguration, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class ScalingPolicy(AWSObject):
    props = {
        'AdjustmentType': (basestring, True),
        'AutoScalingGroupName': (basestring, True),
        'Cooldown': (basestring, False),
        'ScalingAdjustment': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::ScalingPolicy"
        sup = super(ScalingPolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Trigger(AWSObject):
    props = {
        'AutoScalingGroupName': (basestring, True),
        'BreachDuration': (basestring, True),
        'Dimensions': (list, True),
        'LowerBreachScaleIncrement': (basestring, False),
        'LowerThreshold': (basestring, True),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'Period': (basestring, True),
        'Statistic': (basestring, True),
        'Unit': (basestring, False),
        'UpperBreachScaleIncrement': (basestring, False),
        'UpperThreshold': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::Trigger"
        sup = super(UpperThreshold, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)