import random
from aiogram import Router
from aiogram.types import Message
from services.file_handling import book
from database.database import users_db
from keyboards.pagination_kb import create_pagination_keyboard
import logging

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message()
async def send_echo(message: Message):
    pages = ['/page_1', '/page_2', '/page_3', '/page_4', '/page_5', '/page_6', '/page_7', '/page_8', '/page_9',
             '/page_10', '/page_11', '/page_12', '/page_13', '/page_14', '/page_15', '/page_16', '/page_17', '/page_18',
             '/page_19', '/page_20', '/page_21', '/page_22', '/page_23', '/page_24', '/page_25', '/page_26', '/page_27',
             '/page_28', '/page_29', '/page_30', '/page_31', '/page_32', '/page_33', '/page_34', '/page_35', '/page_36',
             '/page_37', '/page_38', '/page_39', '/page_40', '/page_41', '/page_42', '/page_43', '/page_44', '/page_45',
             '/page_46', '/page_47', '/page_48', '/page_49', '/page_50', '/page_51', '/page_52', '/page_53', '/page_54',
             '/page_55', '/page_56', '/page_57', '/page_58', '/page_59', '/page_60', '/page_61', '/page_62', '/page_63',
             '/page_64', '/page_65', '/page_66']
    random_index = random.randint(1, len(pages))

    if message.text not in pages:
        await message.answer(f'Рандомный текст \n* * *\n')
        users_db[message.from_user.id]['page'] = random_index
        text = book[users_db[message.from_user.id]['page']]
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                'forward'))
    else:
        users_db[message.from_user.id]['page'] = int(message.text[6:])
        text = book[users_db[message.from_user.id]['page']]
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[message.from_user.id]["page"]}/{len(book)}',
                'forward'))
