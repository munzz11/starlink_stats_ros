# starlink_stats

## Overview

This ROS node is responsible for connecting to your local Starlink dish, querying its grpc server to retrieve diagnostic data, then transforming that data into a ROS diagnostics message. It was written in Python and runs as a ROS node.

## Prerequisites

- ROS installed on your system (tested on ROS Melodic and Noetic)
- Python 3.x
- Starlink Dish
- Your dishs generated python code, from its .protobuf. Read more about how to interact with your dishs grpc server [here](https://github.com/sparky8512/starlink-grpc-tools/wiki/gRPC-Protocol-Modules)

## Installation

1. Create a ROS workspace (if you haven't already done so):
`
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
`

