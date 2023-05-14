#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from vkbottle.dispatch.rules.base import PayloadRule
from keyboard.keyboard import SENDER_KB


@labeler.message(PayloadRule({'action': 'sender'}))
async def sender_labeler(message):
    await message.answer(message=':', keyboard=SENDER_KB)
