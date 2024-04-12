from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

import app.keyboards as kb

router = Router()

moderator_chat_id = -1002027252561
news_proofs_chat_id = -1002062916210
iqonomy_chat_id = -1002108569989
mens_shelter_chat_id = -1002016217690


@router.message()
async def catalog(message: Message):
    # if message.caption:
    #     if len(message.caption) < 20 and 'instagram' not in message.caption:
    #         await message.copy_to(chat_id=mens_shelter_chat_id)
    #         await message.delete()
    #         return
    await message.copy_to(chat_id=moderator_chat_id, reply_markup=kb.catalog)
    await message.delete()


@router.callback_query(F.data == 'aprove')
async def aprove(callback: CallbackQuery):
    try:
        # if "Men's shelter" in callback.message.caption:
        #     await callback.message.copy_to(chat_id=mens_shelter_chat_id)
        #     await callback.message.delete()
        if 'IQonomy' in callback.message.caption:
            await callback.message.copy_to(chat_id=iqonomy_chat_id)
            await callback.message.delete()
        if 'News & Proofs' in callback.message.caption:
            await callback.message.copy_to(chat_id=news_proofs_chat_id)
            await callback.message.delete()
    except:
        # if "Men's shelter" in callback.message.text:
        #     await callback.message.copy_to(chat_id=mens_shelter_chat_id)
        #     await callback.message.delete()
        if 'IQonomy' in callback.message.text:
            await callback.message.copy_to(chat_id=iqonomy_chat_id)
            await callback.message.delete()
        if 'News & Proofs' in callback.message.text:
            await callback.message.copy_to(chat_id=news_proofs_chat_id)
            await callback.message.delete()


@router.callback_query(F.data == 'reject')
async def reject(callback: CallbackQuery):
    await callback.message.delete()


# @router.callback_query(F.data == 'rewrite')
# async def rewrite(callback: CallbackQuery):
#     if callback.message.photo:
#         for word in image_dicts_crypto:
#             for words in word['words']:
#                 try:
#                     if words.lower() in callback.message.caotion.lower():
#                         await callback.message.copy_to(chat_id=moderator_chat_id, photo=random.choice(word['images']), reply_markup=kb.catalog)
#                         await callback.message.delete()
#                         return
#                 except Exception as e:
#                     print(e)
#                     await callback.message.copy_to(chat_id=moderator_chat_id, photo=callback.message.photo, reply_markup=kb.catalog)
#                     await callback.message.delete()
#                     return
    # await callback.message.copy_to(chat_id=moderator_chat_id, reply_markup=kb.catalog)
    # await callback.message.delete()
    # return
