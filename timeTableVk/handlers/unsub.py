#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from config import db
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({'action': 'unsubscribe'}))
async def unsub_labeler(message):
    await db.update({'peer_id': message.peer_id, 'allow_send': False})
    await message.answer(message='Вы успешно отписались от рассылки!')
