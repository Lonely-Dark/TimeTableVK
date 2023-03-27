#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import SIX_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '6_menu'}))
async def six_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=SIX_CLASSES_KB)
