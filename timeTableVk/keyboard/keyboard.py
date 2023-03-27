#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from vkbottle import Keyboard, Text

MENU_KB = Keyboard(inline=True)
MENU_KB.add(Text("5-ые", {"command": "5_menu"}))
MENU_KB.add(Text("6-ые", {"command": "6_menu"}))
MENU_KB.add(Text("7-ые", {"command": "7_menu"}))
MENU_KB.add(Text("8-ые", {"command": "8_menu"}))
MENU_KB.row()
MENU_KB.add(Text("9-ые", {"command": "9_menu"}))
MENU_KB.add(Text("10-ые", {"command": "10_menu"}))
MENU_KB.add(Text("11-ые", {"command": "11_menu"}))
MENU_KB.row()
MENU_KB.add(Text("Звонки", {"action": "calls"}))
MENU_KB.add(Text("Расписание", {"action": "timetable"}))

MENU_KB = MENU_KB.get_json()

FIVE_CLASSES_KB = Keyboard(inline=True)
FIVE_CLASSES_KB.add(Text("5А", {"class": "5A"}))
FIVE_CLASSES_KB.add(Text("5Б", {"class": "5B"}))
FIVE_CLASSES_KB.add(Text("5В", {"class": "5C"}))
FIVE_CLASSES_KB.add(Text("5Г", {"class": "5D"}))
FIVE_CLASSES_KB.row()
FIVE_CLASSES_KB.add(Text("Назад", {"action": "back"}))

FIVE_CLASSES_KB = FIVE_CLASSES_KB.get_json()

SIX_CLASSES_KB = Keyboard(inline=True)
SIX_CLASSES_KB.add(Text("6А", {"class": "6A"}))
SIX_CLASSES_KB.add(Text("6Б", {"class": "6B"}))
SIX_CLASSES_KB.add(Text("6В", {"class": "6C"}))
SIX_CLASSES_KB.add(Text("6Г", {"class": "6D"}))
SIX_CLASSES_KB.row()
SIX_CLASSES_KB.add(Text("Назад", {"action": "back"}))

SIX_CLASSES_KB = SIX_CLASSES_KB.get_json()

SEVEN_CLASSES_KB = Keyboard(inline=True)
SEVEN_CLASSES_KB.add(Text("7А", {"class": "7A"}))
SEVEN_CLASSES_KB.add(Text("7Б", {"class": "7B"}))
SEVEN_CLASSES_KB.add(Text("7В", {"class": "7C"}))
SEVEN_CLASSES_KB.add(Text("7Г", {"class": "7D"}))
SEVEN_CLASSES_KB.row()
SEVEN_CLASSES_KB.add(Text("Назад", {"action": "back"}))

SEVEN_CLASSES_KB = SEVEN_CLASSES_KB.get_json()

EIGHT_CLASSES_KB = Keyboard(inline=True)
EIGHT_CLASSES_KB.add(Text("8А", {"class": "8A"}))
EIGHT_CLASSES_KB.add(Text("8Б", {"class": "8B"}))
EIGHT_CLASSES_KB.add(Text("8В", {"class": "8C"}))
EIGHT_CLASSES_KB.add(Text("8Г", {"class": "8D"}))
EIGHT_CLASSES_KB.row()
EIGHT_CLASSES_KB.add(Text("Назад", {"action": "back"}))

EIGHT_CLASSES_KB = EIGHT_CLASSES_KB.get_json()

NINE_CLASSES_KB = Keyboard(inline=True)
NINE_CLASSES_KB.add(Text("9А", {"class": "9A"}))
NINE_CLASSES_KB.add(Text("9Б", {"class": "9B"}))
NINE_CLASSES_KB.add(Text("9В", {"class": "9C"}))
NINE_CLASSES_KB.add(Text("Назад", {"action": "back"}))

NINE_CLASSES_KB = NINE_CLASSES_KB.get_json()

TEN_CLASSES_KB = Keyboard(inline=True)
TEN_CLASSES_KB.add(Text("10А", {"class": "10A"}))
TEN_CLASSES_KB.add(Text("10Б", {"class": "10B"}))
TEN_CLASSES_KB.add(Text("10В", {"class": "10C"}))
TEN_CLASSES_KB.add(Text("10Г", {"class": "10D"}))
TEN_CLASSES_KB.row()
TEN_CLASSES_KB.add(Text("Назад", {"action": "back"}))

TEN_CLASSES_KB = TEN_CLASSES_KB.get_json()

ELEVEN_CLASSES_KB = Keyboard(inline=True)
ELEVEN_CLASSES_KB.add(Text("11А", {"class": "11A"}))
ELEVEN_CLASSES_KB.add(Text("11Б", {"class": "11B"}))
ELEVEN_CLASSES_KB.add(Text("11В", {"class": "11C"}))
ELEVEN_CLASSES_KB.add(Text("11Г", {"class": "11D"}))
ELEVEN_CLASSES_KB.row()
ELEVEN_CLASSES_KB.add(Text("Назад", {"action": "back"}))

ELEVEN_CLASSES_KB = ELEVEN_CLASSES_KB.get_json()
