#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from vkbottle import BaseMiddleware
from vkbottle.bot import Message
from tinydb import where
from config import db


class DatabaseCheck(BaseMiddleware[Message]):

    async def pre(self):
        if not await db.search(where('peer_id') == self.event.peer_id):
            await db.insert({'peer_id': self.event.peer_id, 'allow_send': True})
