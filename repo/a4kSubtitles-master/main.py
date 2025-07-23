# -*- coding: utf-8 -*-

import sys
import os
import importlib
import xbmc
from a4kSubtitles import api

if __name__ == '__main__':
    xbmc.log((str(sys.argv)))
    os.environ.pop(api.api_mode_env_name, '')
    core = importlib.import_module('a4kSubtitles.core')
    core.main(int(sys.argv[1]), sys.argv[2][1:])
