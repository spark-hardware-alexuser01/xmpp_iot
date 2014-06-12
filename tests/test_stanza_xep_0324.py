from sleekxmpp import Iq, Message
from sleekxmpp.test import SleekTest
from sleekxmpp.xmlstream import register_stanza_plugin

import src.xep_0324.stanza as xep_0324


class TestProvisioningStanzas(SleekTest):
    """
    Tests creating and manipulating all of the stanzas to the current spec
    for IoT Provisiong (i.e. XEP 0324).
    """

    def setUp(self):
        register_stanza_plugin(Iq, xep_0324.IsFriend)
        register_stanza_plugin(Iq, xep_0324.IsFriendResponse)
        register_stanza_plugin(Message, xep_0324.Unfriend)
        register_stanza_plugin(Message, xep_0324.Friend)

    def testCreateIsFriend(self):
        iq = self.Iq()

        iq['type'] = 'get'
        iq['from'] = 'device@clayster.com/device'
        iq['to'] = 'provisioning.clayster.com'
        iq['id'] = str(9)
        iq['isFriend']['jid'] = 'client1@clayster.com'

        self.check(iq, """
            <iq type='get'
                from='device@clayster.com/device'
                to='provisioning.clayster.com'
                id='9'>
                <isFriend xmlns='urn:xmpp:iot:provisioning' jid='client1@clayster.com'/>
            </iq>
            """)

    def testCreateIsFriendResponse(self):
        iq = self.Iq()

        iq['type'] = 'result'
        iq['from'] = 'provisioning.clayster.com'
        iq['to'] = 'device@clayster.com/device'
        iq['id'] = str(9)
        iq['isFriendResponse']['jid'] = 'client1@clayster.com'
        iq['isFriendResponse']['result'] = 'true'

        self.check(iq, """
            <iq type='result'
                from='provisioning.clayster.com'
                to='device@clayster.com/device'
                id='9'>
                <isFriendResponse xmlns='urn:xmpp:iot:provisioning' jid='client1@clayster.com' result='true'/>
            </iq>
            """)

    def testCreateUnfriend(self):
        msg = self.Message()

        msg['from'] = 'provisioning.clayster.com'
        msg['to'] = 'device@clayster.com'
        msg['unfriend']['jid'] = 'client2@clayster.com'

        self.check(msg, """
            <message from='provisioning.clayster.com'
                to='device@clayster.com'>
                <unfriend xmlns='urn:xmpp:iot:provisioning' jid='client2@clayster.com'/>
            </message>
            """)

    def testCreateFriend(self):
        msg = self.Message()

        msg['from'] = 'provisioning.clayster.com'
        msg['to'] = 'device@clayster.com'
        msg['friend']['jid'] = 'client2@clayster.com'

        self.check(msg, """
            <message from='provisioning.clayster.com'
                to='device@clayster.com'>
                <friend xmlns='urn:xmpp:iot:provisioning' jid='client2@clayster.com'/>
            </message>
            """)
    # def testDownloadPrivilegesResponse(self):
    #     iq = self.Iq()
    #     iq['type'] = 'result'
    #     iq['from'] = 'spam@camalot.gov/model'
    #     iq['to'] = 'eggs@camalot.gov'
    #     iq['id'] = '1'
    #     iq['result'].add_privilege('Sensors', 'include')

    #     print(iq)
