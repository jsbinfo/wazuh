import argparse
import sys

from engine_test.conf.store import ConfigDatabase


def run(args):

    try:
        # Get the configuration database
        ConfigDatabase(args['config_file'], create=True)
    except Exception as ex:
        sys.exit(f"Error adding integration: {ex}")


def configure(subparsers):

    parser = subparsers.add_parser("create-config", help='Creates a new empty configuration file, if not exists')
    parser.set_defaults(func=run)
