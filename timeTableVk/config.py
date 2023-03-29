#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import os
import sys
from configparser import ConfigParser

from loguru import logger
from vkbottle import API
from vkbottle.bot import BotLabeler
from vkbottle import CtxStorage

config = ConfigParser()
config.read(os.path.join(os.getcwd(), '.ini'))

TOKEN = config['DEFAULT']['TOKEN']
GROUP_ID = config['DEFAULT']['GROUP_ID']

api = API(token=TOKEN)
labeler = BotLabeler()

logger.remove()
logger.add(os.path.join("logs", "log.log"), format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level="DEBUG", retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: <level>{message}</level>",
           level="DEBUG", colorize=True)

ctx_storage = CtxStorage()