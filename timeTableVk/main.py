#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import asyncio
import os

from loguru import logger
from vkbottle import Bot

from config import labeler, api
from handlers import labelers
from middlewares import NoBotMiddleware

logger.info("Starting...")

if os.name == "posix":
    import uvloop
    uvloop.install()

bot = Bot(api=api)

for labelers in labelers:
    bot.labeler.load(labeler)

bot.labeler.message_view.register_middleware(NoBotMiddleware)

asyncio.run(bot.run_polling())
