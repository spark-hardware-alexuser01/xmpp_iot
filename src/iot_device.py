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
import thermic
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
        self.register_plugin('xep_0030')
        self.register_plugin('xep_0004')  # Data Forms
        self.register_plugin('xep_0060')  # PubSub
        self.register_plugin('xep_0199')  # XMPP Ping
        self.register_plugin('xep_0325')
        self.register_plugin('xep_0323')

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

class Thermometer(Sensors):
    def __init__(self, nodeId):
        Sensors.__init__(self, nodeId)
        self.temps = thermic.find_sensors()

    def refresh(self, fields):
        self._set_momentary_timestamp(self._get_timestamp())
        self._add_field_momentary_data('temperature', str(self.temps[0].tempc))

if __name__ == '__main__':
    arg_parser = cli_argparse.gen_args()
    args = cli_argparse.parse_args(arg_parser)

    logging.basicConfig(level=args.loglevel, format=LOG_FORMAT)

    xmpp = IoTDevice(args.jid, args.password)
    # register nescessary plugins

    # create sensors and controlls
    thermometer = Thermometer('thermometer')
    thermometer._add_field(name="temperature", typename="numeric", unit="C")
    thermometer.refresh({})
    xmpp['xep_0323'].register_node(nodeId=thermometer.nodeId,
                                   device=thermometer,
                                   commTimeout=10)
    xmpp['xep_0030'].add_feature(feature='urn:xmpp:iot:sensordata',
                                 node='foo',
                                 jid=xmpp.boundjid.full)
    # begin stuff
    xmpp.connect()
    xmpp.process(block=True)
