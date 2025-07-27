# -*- coding: utf-8 -*-
import sys
from modules.router import routing, sys_exit_check
import requests
import urllib3.util.connection
# from modules.kodi_utils import logger

urllib3.util.connection.HAS_IPV6 = False
routing(sys)
if sys_exit_check(): sys.exit(1)

