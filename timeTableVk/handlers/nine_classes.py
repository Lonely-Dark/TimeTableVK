#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import NINE_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '9_menu'}))
async def nine_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=NINE_CLASSES_KB)
