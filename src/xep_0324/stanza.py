from sleekxmpp.xmlstream import ElementBase, register_stanza_plugin
from sleekxmpp.stanza import Iq


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
    name = 'set'  # could this be called foo?
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


class GetTokenResponse(ElementBase):
    name = 'getTokenResponse'
    namespace = 'urn:xmpp:iot:provisioning'
    interfaces = set(['token'])
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


# I don't think canControl has a momentary value in the interfaces set...
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


class Credentials(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'credentials'
    namespace = 'urn:xmpp:iot:provisioning'
    interfaces = set(['type', 'value'])


class CanAccess(ElementBase):
    name = 'canAccess'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['credentials', 'serviceToken'])

    def __init__(self, xml=None, parent=None):
        ElementBase.__init__(self, xml, parent)
        self._credentials = set()

    def setup(self, xml=None):
        ElementBase.setup(self, xml)
        self._credentials = set([credential['type']
                                 for credential in self['credentials']])

    def add_credential(self, name, typename, value):
        """
        Add a new credential to CanAccess request.

        Arguments:
            name  -- The name of the credential
            typename -- the credential type
            value -- the value for the credential
        """

        if name not in self._credentials:
            credential = Credentials()

            credential['name'] = name
            credential['value'] = value

            self._credentials.add(name)
            self.iterables.append(credential)
            return credential

        return None

    def get_credentials(self):
        credentials = []
        for credential in self['substanzas']:
            if isinstance(credential, Credentials):
                credentials.append(credential)
        return credentials


class CanAccessResponse(ElementBase):
    """
    canAccessResponse element
    result type='xs:boolean'
    userToken type='xs:string'
    """
    name = 'canAccessResponse'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['result', 'userToken'])


class UserLoggedIn(ElementBase):
    """
    userLoggedIn element
    serviceToken type='xs:string'
    userToken type='xs:string'
    userName type='xs:string'
    name = 'userLoggedIn'
    """
    # TODO put in UserLoggedIn Example Substanza and extra info
    name = 'userLoggedIn'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['serviceToken', 'userToken', 'userName'])


class HasPrivilege(ElementBase):
    # TODO comment about fields and such for implementation
    name = 'hasPrivilege'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['serviceToken', 'userToken', 'privilegeId'])


class HasPrivilegeResponse(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'hasPrivilegeResponse'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['result'])


class DownloadPrivileges(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'downloadPrivileges'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name
    interfaces = set(['serviceToken', 'userToken'])


class DownloadPrivilegesResponse(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'downloadPrivilegesResponse'
    namespace = 'urn:xmpp:iot:provisioning'
    plugin_attrib = name

    def __init__(self, xml=None, parent=None):
        ElementBase.__init__(self, xml, parent)
        self._includes = set()
        self._excludes = set()
        self._privileges = set()

    def add_privilege(self, privilegeId, privilege):
        # self._privileges[privilegeId] = privilege
        if privilege == 'include':
            include_privilege = IncludePrivilege(parent=self)
            include_privilege['id'] = privilegeId
            self.iterables.append(include_privilege)
            return include_privilege
        elif privilege == 'exclude':
            exclude_privilege = ExcludePrivilege(parent=self)
            exclude_privilege['id'] = privilegeId
            self.iterables.append(exclude_privilege)
            return exclude_privilege
        else:
            return None

    def del_privilege(self, privilegeId, privilege):
        pass

    # TODO Proper way of having subelement name='include' type='Privilege'
    # TODO Proper way of having subelement name='exclude' type='Privilege'


class IncludePrivilege(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'include'
    interfaces = set(['id'])
    plugin_attrib = name


class ExcludePrivilege(ElementBase):
    # TODO comment about fields, context, & implementation
    name = 'exclude'
    interfaces = set(['id'])
    plugin_attrib = name


register_stanza_plugin(Iq, CanAccess)
register_stanza_plugin(CanAccess, Credentials, iterable=True)

register_stanza_plugin(Iq, DownloadPrivilegesResponse)

register_stanza_plugin(DownloadPrivilegesResponse,
                       IncludePrivilege, iterable=True)
register_stanza_plugin(DownloadPrivilegesResponse,
                       ExcludePrivilege, iterable=True)
