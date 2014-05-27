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
from optparse import OptionParser
import sleekxmpp
from sleekxmpp.plugins.xep_0325 import device as ControlDevice
from sleekxmpp.plugins.xep_0323 import device as SensorDevice

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

def generate_options():
    optp = OptionParser()

    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)
    # optp.add_option('-t', '--pingto', help='set jid to ping',
    #                 action='store', type='string', dest='pingjid',
    #                 default=None)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")

    # IoT
    optp.add_option("-n", "--nodeid", dest="nodeid",
                    help="I am a device get ready to be called", default=None)
    return optp

def process_options(optp):

    options, args = optp.parse_args()
    if len(args) == 0:
        optp.print_help()
        optp.exit()

    return tuple(options, args)


if __name__ == '__main__':

    optp = generate_options()
    options, args = process_options(optp)

    logging.basicConfig(level=options.loglevel, format=LOG_FORMAT)

    xmpp = IoTDevice(options.jid, options.password)
    # register nescessary plugins
    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0325')
    xmpp.register_plugin('xep_0323')

    # create sensors and controlls

    # begin stuff
    xmpp.connect()
    xmpp.process(block=True)
