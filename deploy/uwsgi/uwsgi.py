#!/usr/bin/env python3

import argparse
from pathlib import Path
import configparser

from src.api import create_app
from config import Config

parser = argparse.ArgumentParser()
parser.add_argument('--config_path', default='/usr/local/src/halaltrading/config.ini', help='Absolute Config Path')
args = parser.parse_args()

config_file = Path(args.config_path)
if not config_file.is_file():
    print("ERROR: Provide valid config file")
    print("You provide '{0}'".format(args.config_path))
    exit(1)

config = configparser.ConfigParser()
config.read(args.config_path)

Config.SECRET_KEY = config.get('DEFAULT', 'SECRET_KEY', fallback='tirzok1234')
Config.DEBUG_TOOLBAR_ENABLED = config.get('DEFAULT', 'DEBUG_TOOLBAR_ENABLED', fallback=True)
Config.REST_URL_PREFIX = config.get('DEFAULT', 'REST_URL_PREFIX', fallback='/api')
Config.API_VERSION = config.get('DEFAULT', 'API_VERSION', fallback='1')

Config.ADMIN_PASSWORD = config.get('ADMIN', 'password', fallback='admin')

application = create_app(Config())
