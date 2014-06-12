from sleekxmpp import Iq
from sleekxmpp.test import SleekTest
from sleekxmpp.xmlstream import register_stanza_plugin

import src.xep_0324.stanza as xep_0324

namespace = 'sn'

class TestProvisioningStanzas(SleekTest):
    """
    Tests creating and manipulating all of the stanzas to the current spec
    for IoT Provisiong (i.e. XEP 0324).
    """

    def setUp(self):
        register_stanza_plugin(Iq, xep_0324.IsFriend)
        register_stanza_plugin(Iq, xep_0324.IsFriendResponse)

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

    # def testDownloadPrivilegesResponse(self):
    #     iq = self.Iq()
    #     iq['type'] = 'result'
    #     iq['from'] = 'spam@camalot.gov/model'
    #     iq['to'] = 'eggs@camalot.gov'
    #     iq['id'] = '1'
    #     iq['result'].add_privilege('Sensors', 'include')

    #     print(iq)
