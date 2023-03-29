#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from datetime import datetime, timedelta

from config import labeler, api
from loguru import logger
from utils.img import ImageCl, download_full_timetable
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import PayloadRule
from vkbottle.tools import PhotoMessageUploader


@labeler.message(PayloadRule({"action": "timetable"}))
@labeler.message(text="Расписание")
@labeler.message(text="расписание")
async def timetables_all_labeler(message: Message) -> None:
    """
    Get all timetable for all classes
    :param message: Message from user
    :return: None
    """
    # Get current date
    date = datetime.now()
    if datetime.today().weekday() == 5:
        date += timedelta(days=1)
    date += timedelta(days=1)

    temp_date = date.strftime("%d.%m.20%y")
    filename_timetable = f"img/rasp-{temp_date}.png"
    if await ImageCl.check_download_full_timetable(filename=filename_timetable) is False:
        if await download_full_timetable(date=temp_date) is False:
            for i in range(5):
                date += timedelta(days=1)
                temp_date = date.strftime("%d.%m.20%y")
                filename_timetable = f"img/rasp-{temp_date}.png"

                downloaded = await download_full_timetable(date=temp_date)
                if downloaded is True:
                    await message.answer(message=f"На завтрашний день к сожалению расписания нет. Вот на {temp_date}:")
                    break
            else:
                return await message.answer(
                    message="Что-то не так, скорее всего на этот день расписания нет. \n Если вы "
                            "считаете нужным, свяжитесь с администратором: @lonely_dark")

    uploader = PhotoMessageUploader(api)
    doc = await uploader.upload(peer_id=message.peer_id, file_source=filename_timetable)

    await message.answer(message="Держите", attachment=doc)
