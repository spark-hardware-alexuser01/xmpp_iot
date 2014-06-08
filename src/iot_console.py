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

import cli_argparse


LOG_FORMAT = '%(levelname)-8s %(message)s'
log = logging.getLogger(__name__)


class IoTConsole(sleekxmpp.ClientXMPP):
    """
    An IoT console to act as a user interface to send commands/requests
    to IoT devices that have controls or sensors.
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
        # self.register_plugin('xep_0324')

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

        xmpp['xep_0323'].request_data(from_jid=xmpp.boundjid.full,
                                      to_jid='dev00@localhost/monkey',
                                      callback=sensor_readout)
        # xmpp['xep_0324'].can_access(credentials=to_jid='dev00@localhost/monkey')


def call_can_access():
    pass


def sensor_readout(from_jid, result, nodeId, timestamp, fields, error_msg):
    log.DEBUG('sensor_readout()')


if __name__ == '__main__':
    arg_parser = cli_argparse.gen_args()
    args = cli_argparse.parse_args(arg_parser)

    logging.basicConfig(level=args.loglevel, format=LOG_FORMAT)

    xmpp = IoTConsole(args.jid, args.password)

    xmpp.connect()
    xmpp.process(block=True)
