#!/usr/bin/python3

import sys
import json
import grpc
import re
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue

def get_diagnostics(dish_ip):
    
    try:
        from spacex.api.device import device_pb2
        from spacex.api.device import device_pb2_grpc
    except ModuleNotFoundError:
        return({'Starlink': {'level': DiagnosticStatus.ERROR, 'ERROR': 'Generate rpc modules not found'}})
           
    try:
        with grpc.insecure_channel(dish_ip + ":9200") as channel:
            stub = device_pb2_grpc.DeviceStub(channel)
            response = stub.Handle(device_pb2.Request(get_status={}), timeout=10)
    except:
        return({'Starlink': {'level': DiagnosticStatus.ERROR, 'ERROR': 'Dish not found or exceeding 10s response timeout'}})
    
    try:
        response = "{\n" + str(response).split("\n",1)[1] + "}"
        response = re.sub("(\w+) {", r'"\1": {', response)
        response = re.sub('"?(-?\w+(?:\.?\w+|-?|\+?)+)"?', r'"\1"', response)
        response = re.sub('(([^{])\n (?!\s[}]))', r'\2,\n', response)
        response = json.loads(response)
    except:
        print(response)
        return({'Starlink': {'level': DiagnosticStatus.ERROR, 'ERROR': 'Malformed response from dish'}})

    return(response)
