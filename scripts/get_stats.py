#!/usr/bin/python3
"""Simple example of get_status request using grpc call directly."""

import sys
import json
import grpc
import re

# Import the generated python functions from the protocol modules generated from the dish's protobuf

try:
   from spacex.api.device import device_pb2
   from spacex.api.device import device_pb2_grpc
except ModuleNotFoundError:
    print("This script requires the generated gRPC protocol modules. See README file for details.",
          file=sys.stderr)
    sys.exit(1)

# Note that if you remove the 'with' clause here, you need to separately
# call channel.close() when you're done with the gRPC connection.

try:
    with grpc.insecure_channel("192.168.100.1:9200") as channel:
        stub = device_pb2_grpc.DeviceStub(channel)
        response = stub.Handle(device_pb2.Request(get_status={}), timeout=10)
except:
    print("########## ERROR: ##########")
    print("##     Dish Not Found     ##")
    print("##  Writing Sample Ouput  ##")
    print("############################")
    file = open('resp.sample', 'r')
    response = file.read()

print(response)
# Some regex subs to manipulate the output from the dish into json format
response = "{\n" + response.split("\n",1)[1] + "}" 
response = re.sub("(\w+) {", r'"\1": {', response)
response = re.sub(r'"?(-?\w+(?:\.?\w+|-?)+)"?', r'"\1"', response)
response = re.sub('(([^{])\n (?!\s[}]))', r'\2,\n', response)

print(response)

# Now that its in json its much easier utilize, you can read it directly into a dictionary or save it as a json file.
re_dict = json.loads(response)

# Heres some examples of how to request specific info using the generated code, including Software version and connection status.
print("Software version:", response.dish_get_status.device_info.software_version)

# Check if connected
print("Not connected" if response.dish_get_status.HasField("outage") else "Connected")


