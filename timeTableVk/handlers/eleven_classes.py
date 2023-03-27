#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import ELEVEN_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '11_menu'}))
async def eleven_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=ELEVEN_CLASSES_KB)
