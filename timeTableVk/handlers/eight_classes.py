#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import EIGHT_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '8_menu'}))
async def eight_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=EIGHT_CLASSES_KB)
