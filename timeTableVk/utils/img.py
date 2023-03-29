#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

import os.path
import time
from datetime import datetime

import aiohttp
from PIL import Image, UnidentifiedImageError
from aiofile import async_open
from loguru import logger

LETTERS = 'ABCD'
DIFF = 744
STRINGS = [288, 1022, 1754, 2488, 3296, 4102, 4916]
COLUMNS = [57, 814, 1575, 2334, 3093]


class ImageCl(object):
    def __init__(self, filename: str, path="img/"):
        """
        Work with timetable
        :param filename: is filename for timetable
        :param path: this a path to filename
        """

        self.filename_image = filename
        self.path = path
        self.full_path_image = os.path.join(path, filename)

        # Get logger
        self.logger = logger

    async def crop_one_image(self, date: datetime, order: str,
                             letter: str) -> bool:
        """
        Simple crop the image:
        :param date: datetime, is a date to covert
        :param order: str, is a class
        :param letter: str, this a letter for class
        :return: bool
        """
        try:
            image = Image.open(self.full_path_image)
        except UnidentifiedImageError:
            self.logger.warning(
                f"Image is corrupted, delete the image {self.filename_image}")
            os.system(f"rm {self.full_path_image}")
            return False
        except FileNotFoundError:
            self.logger.warning(f"File {self.full_path_image} not found")
            return False

        # Convert date to standard format: day.month.year
        date_str = date.strftime("%d.%m.20%y")
        new_filename = f"rasp-{date_str}-{order}{letter}.png"

        # Crop and save the image
        let = LETTERS.index(letter)
        ij = image.crop((COLUMNS[let], STRINGS[int(order) - 5],
                         COLUMNS[let + 1], STRINGS[int(order) - 5] + DIFF))
        ij.save(os.path.join(self.path, new_filename))

        self.logger.info(f"Successfully write image with name: {new_filename}")
        return True

    @staticmethod
    async def check_download_full_timetable(filename: str,
                                            path="img/") -> bool:
        """
        Checking if the schedule has been downloaded for two hours ago
        :param filename: is a name for timetable
        :param path: is a path to file
        :return: bool
        """

        if os.path.isfile(os.path.join(path, filename)) is True:
            return time.time() - os.path.getmtime(
                os.path.join(path, filename)) < 7200
        else:
            return False

    @staticmethod
    async def check_cropped_image(filename: str, path="img/") -> bool:
        """
        Checking if the image has been cropped for two hours ago
        :param filename: is a name for image
        :param path: is a path to image
        :return: bool
        """

        spl = os.path.join(path, filename)
        if os.path.isfile(spl) is True:
            return time.time() - os.path.getmtime(spl) < 7200
        else:
            return False


async def download_timetable(date: str, add_date=False, path="img/") -> bool:
    """
    Download timetable from timetable site
    :param date: is a date to download
    :param add_date: if add_date is False, this a full date, if True this isn't
    full date, add to date month and year
    :param path: this a path to save a full timetable
    :return: bool
    """

    url = f"https://сдо.амтэк35.рф/shedule/{date}"
    if add_date is False:
        url += ".png"
        filename = f"rasp-{date}.png"
    else:
        url += datetime.now().strftime(".%m.20%y")
        url += ".png"

        filename = f"rasp-{date}"
        filename += datetime.now().strftime(".%m.20%y")
        filename += ".png"

    session = aiohttp.ClientSession()
    async with session.get(url) as response:
        data = (await response.read())
        resp = response.status

    if resp == 404:
        await session.close()
        logger.critical(f"Error: 404 response from {url}")
        return False
    else:
        await session.close()
        async with async_open(os.path.join(path, filename), "wb") as b:
            await b.write(data)
        return True
