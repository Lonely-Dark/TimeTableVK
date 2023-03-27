#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import SEVEN_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '7_menu'}))
async def seven_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=SEVEN_CLASSES_KB)
