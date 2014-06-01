"""
    SleekXMPP: The Sleek XMPP Library
"""

import logging

from sleekxmpp.plugins.base import BasePlugin

log = logging.getLogger(__name__)


class XEP_0324(BasePlugin):

    """
    XEP-0324: IoT Provisioning
    """

    name = 'xep_0324'
    description = 'XEP-0324: Internet of Things - Provisioning'
    dependencies = set(['xep_0030', 'XEP_0323', 'xep_0325'])

    default_config = {
        'threaded': True
    }

    def plugin_init(self):
        """ Start the XEP-0324 plugin """

        # Register Handlers

    def plugin_end(self):
        """ Stop the XEP-0324 plugin """

    def get_token(self):
        pass

    def get_token_resp(self):
        pass

    def get_token_challenge(self):
        pass

    def get_token_challenge_respons(self):
        pass

    def token_challenge(self):
        pass

    def token_challenge_resp(self):
        pass

    def is_friend(self):
        pass

    def is_friend_resp(self):
        pass

    def friend(self):
        pass

    def unfriend(self):
        pass

    def can_read(self):
        pass

    def can_read_resp(self):
        pass

    def can_control(self):
        pass

    def can_control_resp(self):
        pass

    def clear_cache(self):
        pass

    def clear_cache_resp(self):
        pass

    def can_access(self):
        pass

    def can_access_resp(self):
        pass

    def user_logged_in(self):
        pass

    def has_privilege(self):
        pass

    def has_privilege_resp(self):
        pass

    def download_priveleges(self):
        pass

    def download_priveleges_resp(self):
        pass
