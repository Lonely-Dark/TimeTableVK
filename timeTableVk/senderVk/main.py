#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import asyncio
import os
import random
from configparser import ConfigParser

import tinydb
from loguru import logger

from img import download_full_timetable
from vkbottle import PhotoMessageUploader, API
from datetime import datetime, timedelta
import aioschedule as schedule


async def _main(peer_id: int, api):
    # Get current date
    date = datetime.now()
    if datetime.today().weekday() == 5:
        date += timedelta(days=1)
    date += timedelta(days=1)
    date = date.strftime("%d.%m.20%y")

    await download_full_timetable(date)

    uploader = PhotoMessageUploader(api)
    source = os.path.join("img/", f"rasp-{date}.png")
    doc = await uploader.upload(peer_id=peer_id, file_source=source)

    await api.messages.send(peer_id=peer_id, message=f"Актуальное расписание на {date}", attachment=doc, random_id=random.randint(1, 1000))


async def main():
    db = tinydb.TinyDB('db.json')

    config = ConfigParser()
    config.read(os.path.join(os.getcwd(), '.ini'))
    TOKEN = config['DEFAULT']['TOKEN']

    api = API(TOKEN)

    for i in db:
        if i['allow_send'] is True:
            try:
                await _main(i['peer_id'], api)
            except Exception as e:
                logger.error(e)

if __name__ == "__main__":
    schedule.every().day.at("15:00").do(main())
    asyncio.run(schedule.run_pending())
