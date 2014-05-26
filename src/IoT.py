import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp

class IoT(sleekxmpp.ClientXMPP):
    """
    IoT Device
    """

    def __init__(self, jid, password, recipient):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.jjid = jid
        self.recipient = recipient
        self.add_event_handler("session_start", self.start, threaded=True)


    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.send_set()


    def send_set(self, value_type='', name='', value=''):
        self.send_message(mto=self.recipient,
                          mbody="Sending Set Command",
                          mtype='chat')
        print('calling set command')
        self.plugin['xep_0325'].set_command(self.jjid,
                                            self.recipient,
                                            [('lol', 'int', '33')]
                                            )
        print('called set command')



if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")
    optp.add_option("-t", "--to", dest="to",
                    help="JID to send the message to")
    optp.add_option("-m", "--message", dest="message",
                    help="message to send")

    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    if opts.jid is None:
        opts.jid = input("Username: ")
    if opts.password is None:
        opts.password = getpass.getpass("Password: ")
    if opts.to is None:
        opts.to = input("Send To: ")

    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    xmpp = IoT(opts.jid, opts.password, opts.to)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0199') # XMPP Ping
    xmpp.register_plugin('xep_0325') # XMPP Control

    # If you are working with an OpenFire server, you may need
    # to adjust the SSL version used:
    # xmpp.ssl_version = ssl.PROTOCOL_SSLv3

    # If you want to verify the SSL certificates offered by a server:
    # xmpp.ca_certs = "path/to/ca/cert"

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect():
        # If you do not have the dnspython library installed, you will need
        # to manually specify the name of the server if it does not match
        # the one in the JID. For example, to use Google Talk you would
        # need to use:
        #
        # if xmpp.connect(('talk.google.com', 5222)):
        #     ...
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")


