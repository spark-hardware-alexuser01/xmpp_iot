
from sleekxmpp.test import *
import src.xep_0324 as xep_0324

namespace = 'sn'

class TestProvisioningStanzas(SleekTest):
    def setUp(self):
        pass

    def testDownloadPrivilegesResponse(self):
        iq = self.Iq()
        iq['type'] = 'result'
        iq['from'] = 'spam@camalot.gov/model'
        iq['to'] = 'eggs@camalot.gov'
        iq['id'] = '1'
        iq['result'].add_privilege('Sensors', 'include')

        print(iq)
