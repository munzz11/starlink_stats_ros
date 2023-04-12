# starlink_stats

## Overview

This ROS node is responsible for connecting to your local Starlink dish, querying its grpc server to retrieve diagnostic data, then transforming that data into a ROS diagnostics message. It was written in Python and runs as a ROS node.

## Prerequisites

- ROS installed on your system (tested on ROS Melodic and Noetic)
- Python 3.x
- Starlink Dish
- Your dishs generated python code, from its .protobuf. Read more about how to interact with your dishs grpc server [here](https://github.com/sparky8512/starlink-grpc-tools/wiki/gRPC-Protocol-Modules)

## Installation

1. Clone this package into your existing ROS worksapce
2. Copy the 'spacex' folder containing your dishs grpc code into the src folder so that it looks like bellow: 
```bash
THIS PACKAGE
└── src
    ├── spacex
    │   ├── api
    │   │   ├── common
    │   ... ...
    └── starlink_grpc
        ├── get_starlink_stats.py
        └── __init__.py
```
3. Make sure the spacex folder is initialized as a python module with __init__'s, if not you can use the setup.sh script which will initialize.
4. In the base folder of this package, run `pip install -e`
5. Build your catkin_workspace
6. Now launch the node using `rosrun starlink_stats_ros starlink_diagnostics_node.py` or buy adding to your larger ROS launchfile arcitecture. 

## Notes:
- The device running this node will need to be able to access the 192.168.100.1 address of the dish.
- If you're just using the stock starlink router, it typically has a route preconfigured onboard for devices on its 192.168.1.x network to be able to access the dish.
- If you run `nmap 192.168.100.1` the output should look like: 
```bash
Nmap scan report for mbmoxac (192.168.100.1)
Host is up (0.0041s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
9200/tcp open  wap-wsp
```

