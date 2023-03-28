from datetime import datetime, timedelta

from config import labeler, api
from loguru import logger
from utils.img import ImageCl, download_timetable
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import PayloadRule
from vkbottle.tools import PhotoMessageUploader


@labeler.message(PayloadRule({"action": "timetable"}))
@labeler.message(text="Расписание")
@labeler.message(text="расписание")
async def timetables_all_labeler(message: Message):
    # Get current date
    date = datetime.now()
    if datetime.today().weekday() == 5:
        date += timedelta(days=1)
    date += timedelta(days=1)

    temp_date = date.strftime("%d.%m.20%y")
    filename_timetable = f"img/rasp-{temp_date}.png"
    if await ImageCl.check_download_full_timetable(filename=filename_timetable) is False:
        if await download_timetable(date=temp_date) is False:
            logger.critical(f"Failed to download timetable for {temp_date}")
            await message.answer("Расписание не найдено")
            return False

    uploader = PhotoMessageUploader(api)
    doc = await uploader.upload(peer_id=message.peer_id, file_source=filename_timetable)

    await message.answer(message="Держите", attachment=doc)
