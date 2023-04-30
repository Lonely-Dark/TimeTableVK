import os

import aiohttp
from aiofile import async_open
from loguru import logger


async def download_full_timetable(date: str, path: str = "img/") -> bool:
    """
    Download full timetable from lyceum
    :param date: string, date to download
    :param path: string, path to download
    :return: boolean, True if successful, False otherwise
    """

    url = f"https://сдо.амтэк35.рф/shedule/{date}.png"
    filename = f"rasp-{date}.png"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()

            if response.status == 404:
                logger.critical(f"Error: 404 response from {url}")
                return False

            async with async_open(os.path.join(path, filename), "wb") as f:
                logger.info(f"Download full timetable from {url} complete")
                await f.write(data)
                return True
