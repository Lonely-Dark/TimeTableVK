#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import TEN_CLASSES_KB
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'command': '10_menu'}))
async def ten_labeler(message):
    await message.answer(message='Выбирайте:', keyboard=TEN_CLASSES_KB)
