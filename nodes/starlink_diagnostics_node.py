#!/usr/bin/python3

import rospy
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue
from starlink_grpc.get_starlink_stats import get_diagnostics

def publish_diagnostic_message(diagnostic_data):
    # Initialize ROS node
    rospy.init_node('diagnostic_publisher')

    # Create diagnostic array message
    diag_array = DiagnosticArray()
    diag_array.header.stamp = rospy.Time.now()

    # Create diagnostic status message for each key-value pair in dictionary
    for key, value in diagnostic_data.items():
        # Create diagnostic status message and set its values
        diag_status = DiagnosticStatus()
        diag_status.name = key
        diag_status.message = value.get('message', '')
        diag_status.level = value.get('level', DiagnosticStatus.OK)
        diag_status.values = []

        # Create key-value messages for each item in the subdictionary
        for k, v in value.items():
            if k != 'level' and k != 'message':
                key_value = KeyValue()
                key_value.key = k
                key_value.value = str(v)
                diag_status.values.append(key_value)

        # Add diagnostic status message to diagnostic array
        diag_array.status.append(diag_status)

    # Create ROS publisher for diagnostic array message
    pub = rospy.Publisher('/diagnostics', DiagnosticArray, queue_size=10)

    # Publish diagnostic array message repeatedly
    while not rospy.is_shutdown():
        diag_array.header.stamp = rospy.Time.now()
        pub.publish(diag_array)
        rospy.sleep(1)

if __name__ == '__main__':
   # diagnostic_data = {'example1': {'level': DiagnosticStatus.OK, 'message': 'This is an example diagnostic message.', 'value1': 10, 'value2': 20},
   #                   'example2': {'level': DiagnosticStatus.ERROR, 'message': 'This is another example diagnostic message.', 'value1': 30, 'value2': 40}}
    diagnostic_data = get_diagnostics("192.168.100.1")
    print(diagnostic_data)
    publish_diagnostic_message(diagnostic_data)

