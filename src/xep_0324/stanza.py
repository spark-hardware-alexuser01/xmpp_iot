from sleekxmpp.xmlstream import ET, ElementBase, register_stanza_plugin  

class Provisioning(ElementBase): 
   """
   A stanza class for IoT Provisioning 

   example
   <iq type = 'get'
   from='device@clayster.com/device'
   to='provisioning.clayster.com'
   id='9'>
   <isFriend xmlns='urn:xmpp:iot:provisioning' jid='client1@clayster.com'/>
   </iq>
   """
   name = 'set' #could this be called foo?
   namespace = 'urn:xmpp:iot:provisioning'
   plugin_attrib = 'provisioning'
   interfaces = set()

"""skipped 3.1: Delegating Trust, seemed complicated"""

class FriendRequest(ElementBase):
   name = 'isFriend'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['jid'])
   plugin_attrib = name 

class Unfriend(ElementBase):
   name = 'unfriend'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['jid'])
   plugin_attrib = name 

class RecommendFriend(ElementBase):
   name = 'friend'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['jid'])
   plugin_attrib = name 

"""I did not do rejecting read-outs because it was an
   extension of sensor data, however I studied it for
   a while, and realized I have no idea how to do the 
   nodes part, saw some examples of how it might
   be done through sensor data"""

class GetToken(ElementBase): 
   name = 'getToken'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(tuple())
   plugin_attrib = name

class GetTokenChallenge(ElementBase):
   name = 'getTokenChallenge'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['seqnr'])
   plugin_attrib = name


class CanRead(ElementBase):
   name = 'canRead'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['jid', 'serviceToken', 'userToken', 'momentary'])
   plugin_attrib = name

#I don't think canControl has a momentary value in the interfaces set...
class CanControl(ElementBase):
   name = 'canControl'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(['jid', 'serviceToken', 'userToken'])
   plugin_attrib = name

class ClearCache(ElementBase): 
   name = 'clearCache'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(tuple())
   plugin_attrib = name

class CredentialParameter(ElementBase):
   """Parameter elements that act as credentials.
         JidCredentialParameter
         Ip4CredentialParameter
         Ip6CredentialParameter
         HostNameCredentialParameter
         X509CertificateCredentialParameter
         UserNameCredentialParameter
         LongitudeCredentialParameter
         LatitudeCredentialParameter
         AltitudeCredentialParameter
         SsoCredentialParameter
         ProtocolCredentialParameter
   """
   namespace = 'urn:xmpp:iot:provisioning'
   name = 'credentialParameter'
   plugin_attrib = name
   interfaces = set(['type', 'value'])

class JidCredentialParameter(ElementBase):
   name = 'jid'
   plugin_attrib = name

class Ip4CredentialParameter(ElementBase):
   name = 'ip4'
   plugin_attrib = name

class Ip6CredentialParameter(ElementBase):
   name = 'ip6'
   plugin_attrib = name

class HostNameCredentialParameter(ElementBase):
   name = 'hostName'
   plugin_attrib = name

class X509CertificateCredentialParameter(ElementBase):
   name = 'x509Certificate'
   plugin_attrib = name

class UserNameCredentialParameter(ElementBase):
   name = 'userName'
   plugin_attrib = name

class LongitudeCredentialParameter(ElementBase):
   name = 'longitude'
   plugin_attrib = name

class LatitudeCredentialParameter(ElementBase):
   name = 'latitude'
   plugin_attrib = name

class AltitudeCredentialParameter(ElementBase):
   name = 'altitude'
   plugin_attrib = name

class SsoCredentialParameter(ElementBase):
   name = 'sso'
   plugin_attrib = name

class ProtocolCredentialParameter(ElementBase):
   name = 'protocol'
   plugin_attrib = name

