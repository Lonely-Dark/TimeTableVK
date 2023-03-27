#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import FIVE_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '5_menu'}))
async def five_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=FIVE_CLASSES_KB)
