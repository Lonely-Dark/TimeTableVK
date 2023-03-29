#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import os
from datetime import datetime

from config import labeler, api
from dateutil import relativedelta
from keyboard.keyboard import MENU_KB
from transliterate import translit
from transliterate.base import registry
from utils import ImageCl, download_full_timetable, LLanguagePack
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import RegexRule
from vkbottle.tools import PhotoMessageUploader

registry.register(LLanguagePack)


@labeler.message(RegexRule(r'(\d\w \d\d$)|(\d\d\w \d\d$)'))
async def extension_labeler(message: Message) -> None:
    """
    Extension for main func, get timetable with date
    :param message: message from user
    :return: None
    """
    mess = message.text.split()
    classe = mess[0].upper()
    classe = translit(classe, language_code='llpack', reversed=True)

    date = mess[1]

    temp_now = datetime.now().replace(day=1)

    if (date == '01' or date == '02') and (datetime.now().day != 1 and
                                           datetime.now().day != 2):
        temp_now += relativedelta.relativedelta(months=1)
    temp_now = temp_now.strftime("%m.20%y")

    date += f".{temp_now}"

    date_check = datetime.strptime(date, "%d.%m.20%y")
    temp_filename = f"rasp-{date}-{classe}.png"
    temp_class = classe[:-1]
    temp_letter = classe[-1]
    file_rsp = os.path.join("img/", temp_filename)

    if date_check.day < datetime.now().day:
        return await message.answer(message="На прошлые дни нельзя посмотреть расписание. Если вам вдруг оно зачем-то "
                                            "понадобилось, напишите администратору @lonely_dark")

    downloaded = await ImageCl.check_download_full_timetable(
        f"rasp-{date}.png")
    if downloaded is False:
        downloaded = await download_full_timetable(date=date)
    if downloaded is False:
        return await message.answer(
            message="Что-то не так, скорее всего на этот день расписания нет. \n Если вы считаете нужным, свяжитесь с "
                    "администратором: @lonely_dark")

    checked_img = await ImageCl.check_cropped_image(temp_filename)
    if checked_img is False:
        image = ImageCl(f"rasp-{date}.png")
        checked_img = await image.crop_one_image(date_check, temp_class,
                                                 temp_letter)
    if checked_img is False:
        return await message.answer(
            message="Что-то не так, скорее всего на этот день расписания нет. \n Если вы "
                    "считаете нужным, свяжитесь с администратором: @lonely_dark")

    uploader = PhotoMessageUploader(api)
    doc = await uploader.upload(file_source=file_rsp, peer_id=message.peer_id)
    await message.answer(message='Держите:', attachment=doc)

    await message.answer(message='Хотите что-то ещё?', keyboard=MENU_KB)
