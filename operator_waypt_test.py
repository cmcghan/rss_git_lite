#! /usr/bin/env python
# Copyright 2017-2018 by University of Cincinnati
# Copyright 2014-2016 by California Institute of Technology
# All rights reserved. See LICENSE file at:
# https://github.com/cmcghan/rss_git_lite
"""
=== Summary of contents ===
"""

# Note that the following may only work if you run this python script from the directory in which it resides...
#
# This is done so you can use the import command on other/separate modules (this is adding it to the beginning like it should've automagically done for you); remember to create an empty __init__.py in the local directory for this to load properly
import os
import sys # for sys.exit() and sys.path.append()
sys.path.append(os.getcwd()) # modify sys.path to include current directory
sys.path.append(os.getcwd() + '/common') # modify sys.path to include ./common directory
import ws4pyRosMsgSrvFunctions_gen as ws4pyROS
import getConnectionIPaddress as gC

from time import sleep

if __name__ == '__main__':

    connection = gC.getConnectionIPaddress()

    try:
        #
        # example code for sending waypoints to pseudoDL
        #
        ws_waypts_out = ws4pyROS.PubClient(connection)
        ws_waypts_out.connect('/operator/waypoint_list','nav_msgs/Path',ws4pyROS.pack_waypoints)
#        ws_waypts_out.connect('/operator/waypoint_list','nav_msgs/Path',pack_waypoints)
        sleep(3)
        waypoints_to_send = [ [1.0, 2.0], [7.0, 2.0], [6.0, 3.0], [-1.0, 2.0], [1.0, 2.0] ] # list of lists
        ws_waypts_out.send_pieces([waypoints_to_send, 1]) # send waypoint(s), waytype=1 ([x,y] points, no set orientation)
                
        sleep(3)
    except KeyboardInterrupt:
        ws_waypts_out.close()
