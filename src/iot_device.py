#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SleekXMPP: The Sleek XMPP Library
    Implementation of xeps for Internet of Things
    http://wiki.xmpp.org/web/Tech_pages/IoT_systems
    Copyright (C) 2013 Sustainable Innovation, Joachim.lindborg@sust.se
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

import logging
import sleekxmpp
from controls import Controls
from sensors import Sensors

import cli_argparse


LOG_FORMAT = '%(levelname)-8s %(message)s'


class IoTDevice(sleekxmpp.ClientXMPP):
    """
    An IoT device to act as a server and handle sensor data
    and control command requests.
    """

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)

    def session_start(self, event):
        self.send_presence()
        self.get_roster()


# class Control(ControlDevice):
#     def __init__(self, nodeId):
#         self.control_fields = {}
#
#
# class Sensor(SensorDevice):
#     def __init__(self, nodeId, fields):
#         self.nodeId = nodeId



if __name__ == '__main__':
    arg_parser = cli_argparse.gen_args()
    args = cli_argparse.parse_args()

    # logging.basicConfig(level=options.loglevel, format=LOG_FORMAT)

    xmpp = IoTDevice(args.jid, args.password)
    # register nescessary plugins
    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0325')
    xmpp.register_plugin('xep_0323')

    # create sensors and controlls
    sensors = Sensors('thermometer')
    sensors._add_field(name="temperature", typename="numeric", unit="C")
    xmpp['xep_0323'].register_node(nodeId='thermometer',
                                   device=sensors,
                                   commTimeout=10)
    controls = Controls('switch')

    # begin stuff
    xmpp.connect()
    xmpp.process(block=True)
