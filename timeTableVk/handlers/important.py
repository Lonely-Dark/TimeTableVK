#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import json
import os
from datetime import timedelta, datetime

from config import labeler, api
from utils.img import ImageCl, download_timetable
from vkbottle import PhotoMessageUploader
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import PayloadRule


# Shitcode
@labeler.message(
    PayloadRule({'class': '5A'}) | PayloadRule({'class': '5B'}) | PayloadRule({'class': '5C'}) | PayloadRule(
        {'class': '5D'}) | PayloadRule({'class': '6A'}) | PayloadRule({'class': '6B'}) | PayloadRule(
        {'class': '6C'}) | PayloadRule({'class': '6D'}) | PayloadRule({'class': '7A'}) | PayloadRule(
        {'class': '7B'}) | PayloadRule({'class': '7C'}) | PayloadRule({'class': '7D'}) | PayloadRule(
        {'class': '8A'}) | PayloadRule({'class': '8B'}) | PayloadRule({'class': '8C'}) | PayloadRule(
        {'class': '8D'}) | PayloadRule({'class': '9A'}) | PayloadRule({'class': '9B'}) | PayloadRule(
        {'class': '9C'}) | PayloadRule({'class': '10A'}) | PayloadRule({'class': '10B'}) | PayloadRule(
        {'class': '10C'}) | PayloadRule({'class': '10D'}) | PayloadRule({'class': '11A'}) | PayloadRule(
        {'class': '11B'}) | PayloadRule({'class': '11C'}) | PayloadRule({'class': '11D'}))
async def important_labeler(message: Message) -> None:
    """
    Get a timetable for next day
    :param message: message from user
    :return: None
    """
    # Get current date
    date = datetime.now()
    if datetime.today().weekday() == 5:
        date += timedelta(days=1)
    date += timedelta(days=1)

    # Date in str, class, letter, filename
    temp_date = date.strftime("%d.%m.20%y")
    message.payload = json.loads(message.payload)
    temp_class = message.payload['class'][:-1]
    temp_letter = message.payload['class'][-1]
    filename_rsp = f"rasp-{temp_date}.png"
    temp_filename = f"rasp-{temp_date}-{message.payload['class']}.png"

    # Check if timetable downloaded and check image cropped
    downloaded = await ImageCl.check_download_full_timetable(filename_rsp)
    if downloaded is False:
        downloaded = await download_timetable(date=temp_date)
    if downloaded is False:
        return await message.answer(
            message="Что-то не так, скорее всего на этот день расписания нет. \n Если вы "
                    "считаете нужным, свяжитесь с администратором: @lonely_dark")

    checked_img = await ImageCl.check_cropped_image(temp_filename)
    if checked_img is False:
        image = ImageCl(filename_rsp)
        checked_img = await image.crop_one_image(date, temp_class, temp_letter)
    if checked_img is False:
        return await message.answer(
            message="Что-то не так, скорее всего на этот день расписания нет. \n Если вы "
                    "считаете нужным, свяжитесь с администратором: @lonely_dark")

    image_name = f"rasp-{temp_date}-{message.payload['class']}.png"
    temp_path = os.path.join("img/", image_name)

    uploader = PhotoMessageUploader(api)

    doc = await uploader.upload(peer_id=message.peer_id, file_source=temp_path)

    await message.answer(message="Расписание:", attachment=doc)
    await message.answer(message="Хотите ещё? Нажмите на клавиатуру.", keyboard=MENU_KB)
