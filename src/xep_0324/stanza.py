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
   interfaces = set(('jid'))
   #plugin_attrib = ?

class Unfriend(ElementBase):
   name = 'unfriend'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(('jid'))
   #plugin_attrib = ?

class recommendFriend(ElementBase):
   name = 'friend'
   namespace = 'urn:xmpp:iot:provisioning'
   interfaces = set(('jid'))
   #plugin_attrib = ?

"""I did not do rejecting read-outs because it was an
   extension of sensor data, however I studied it for
   a while, and realized I have no idea how to do the 
   nodes part, saw some examples of how it might
   be done through sensor data"""

