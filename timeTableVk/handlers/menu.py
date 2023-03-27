#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from config import labeler
from keyboard.keyboard import MENU_KB


@labeler.message(text=['привет', 'помощь', 'начать', 'клавиатура', 'клава', 'старт', 'start',
                       '/start', 'Привет', 'Помощь', 'Клавиатура', 'Клава', 'Старт', 'Start'])
async def menu_labeler(message):
    await message.answer("Приветствую! Нажмите на одну из кнопок ниже для получения расписания"
                         " на завтра", keyboard=MENU_KB)
