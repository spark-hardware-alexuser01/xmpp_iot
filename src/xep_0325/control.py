
import logging

import sleekxmpp
from sleekxmpp.stanza import Iq
from sleekxmpp.xmlstream.handler import Callback
from sleekxmpp.xmlstream.matcher import StanzaPath
from sleekxmpp.xmlstream import register_stanza_plugin, ElementBase, ET
from sleekxmpp.plugins import BasePlugin

import stanza

log = logging.getLogger(__name__)



class XEP_0325(BasePlugin):
    """
    XEP-0325 Internet of Things Control
    """

    name = 'xep_0325'
    description = 'XEP-0325 Internet of Things Control'
    dependencies = set([])

    def plugin_init(self):
        register_stanza_plugin(Iq, stanza.Int)
        register_stanza_plugin(Iq, stanza.Boolean)
        register_stanza_plugin(Iq, stanza.String)

    def send_int(self, ifrom=None, block=True, timeout=None, callback=None, \
                 name='', value=None):
        iq = self.xmpp.Iq()
        iq['type'] = 'set'
        iq['from'] = ifrom
        iq['control']['int']['name'] = str(name)
        iq['control']['int']['value'] = str(value)

        if not block:
            return iq.send(block=block, timeout=timeout, callback=callback)


    def send_boolean(self, ifrom=None, block=True, timeout=None, callback=None, \
                 name='', value=None):
        iq = self.xmpp.Iq()
        iq['type'] = 'set'
        iq['from'] = ifrom
        iq['control']['boolean']['name'] = str(name)
        iq['control']['boolean']['value'] = str(value)

        if not block:
            return iq.send(block=block, timeout=timeout, callback=callback)

    def send_string(self, ifrom=None, block=True, timeout=None, callback=None, \
                 name='', value=None):
        iq = self.xmpp.Iq()
        iq['type'] = 'set'
        iq['from'] = ifrom
        iq['control']['string']['name'] = str(name)
        iq['control']['string']['value'] = str(value)

        if not block:
            return iq.send(block=block, timeout=timeout, callback=callback)
