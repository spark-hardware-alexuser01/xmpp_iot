import argparse
import logging


def gen_args(arg_parser=None):
    if arg_parser is None:
        arg_parser = argparse.ArgumentParser(description='IoT Device')

    # XMPP Account and Authentication
    arg_parser.add_argument('-j', '--jid', dest='jid', required=True,
                            help='IoT Device\'s JID to be used.')
    arg_parser.add_argument('-p', '--password', dest='password',
                            required=True, help='Password for used JID')

    # IoT configuration
    arg_parser.add_argument('-nc', '--nodeid-control', dest='nodeid_control',
                            help='NodeId to be used for Controller')
    arg_parser.add_argument('-ns', '--nodeid-sensor', dest='nodeid_sensor',
                            help='NodeId to be used for Sensor')

    # Logging
    arg_parser.add_argument('-q', '--quiet',
                            action='store_const',
                            dest='loglevel',
                            const=logging.ERROR,
                            default=logging.INFO,
                            help='set logging to ERROR')

    arg_parser.add_argument('-d', '--debug',
                            action='store_const',
                            dest='loglevel',
                            const=logging.DEBUG,
                            default=logging.INFO,
                            help='set logging to DEBUG')

    # krg_parser.add_argument('-v', '--verbose',
    #                         help='set logging to COMM',
    #                         action='store_const',
    #                         dest='loglevel',
    #                         const=5,
    #                         default=logging.INFO)

    return arg_parser


def parse_args(arg_parser):
    return arg_parser.parse_args()
