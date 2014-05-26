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

class Controll(sleekxmpp.plugins.xep_0325.device):
    def __init__():
        pass

class Sensor(sleekxmpp.plugins.xep_0323.device):
    def __init__():
        pass

if __name__ == '__main__':
    optp = OptionParser()

    # option handling

    # register nescessary plugins
    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0325')
    xmpp.register_plugin('xep_0323')

    # create sensors and controlls

    # begin stuff
    xmpp.connect()
    xmpp.process(block=True)


