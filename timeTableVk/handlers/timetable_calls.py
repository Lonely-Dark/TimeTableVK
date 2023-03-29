#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import PayloadRule


@labeler.message(PayloadRule({"action": "calls"}))
@labeler.message(text="Звонки")
@labeler.message(text="звонки")
async def calls_labeler(message: Message) -> None:
    text = """
    Расписание уроков и время:
    
    1 урок: 08:30-09:10
    2 урок: 9:20-10:00
    3 урок: 10:20-11:00
    4 урок: 11:20-12:00
    5 урок: 12:20-13:00
    6 урок: 13:10-13:50
    7 урок: 14:00-14:40
    8 урок: 14:50-15:30
    9 урок: 15:40-16:20
    """

    await message.answer(message=text)
