from sleekxmpp.xmlstream import ET, ElementBase, register_stanza_plugin


class Control(ElementBase):
    """
    A stanza class for IoT Control XEP

    example
    <iq type='set'
        from='master@clayster.com/amr'
        to='digital.output@clayster.com'
        id='1'>
        <set xmlns='urn:xmpp:iot:control' xml:lang='en'
            <boolean name='Output' value='true'/>
        </set>
    </iq>
    """

    name = 'set'

    namespace = 'urn:xmpp:iot:control'

    plugin_attrib = 'control'

    interfaces = set()


class ControlSet(ElementBase):
    pass


class BooleanParam(ElementBase):
    name = 'boolean'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'boolean'


class ColorParam(ElementBase):
    name = 'color'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'color'


class DateParam(ElementBase):
    name = 'date'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'date'


class DateTime(ElementBase):
    name = 'dateTime'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'dateTime'


class Double(ElementBase):
    name = 'double'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'double'


class Duration(ElementBase):
    name = 'duration'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'duration'


class Int(ElementBase):
    name = 'int'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'int'


class Long(ElementBase):
    name = 'long'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'long'


class String(ElementBase):
    name = 'string'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'string'


class Time(ElementBase):
    name = 'time'
    namespace = 'urn:xmpp:iot:control'
    interfaces = set(('name', 'value'))
    plugin_attrib = 'time'
