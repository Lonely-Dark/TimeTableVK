#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from config import db
from tinydb import where
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'action': 'subscribe'}))
async def sub_labeler(message):
    await db.update({'allow_send': True}, where('peer_id') == message.peer_id)
    await message.answer(message='Вы успешно подписались на рассылку!')
