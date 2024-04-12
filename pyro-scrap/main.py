from typing import List
import logging
import re
import g4f
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
import asyncio
import random

from prompts import prompt_no_link_with_media, prompt_no_link_no_media, prompt_with_link_with_media, prompt_with_link_no_media
from donor_channels import crypto_channels, finance_channels
from images import image_dicts_crypto


from api import api_hash_key, api_id_key


# ID channels

donor_lists: List = crypto_channels + finance_channels # + mens_shelter_channels


moderator_channel: int = 7131490029  # bot -1002027252561

# На какой канал оставлять ссылку:


def to_whats_channel(message):
    if message.chat.id in crypto_channels:
        return "🔥 [News & Proofs](https://t.me/proofs_news) 🔥"
    if message.chat.id in finance_channels:
        return "🏦 [IQonomy](https://t.me/iqonomy) 🏦"
    #if message.chat.id in mens_shelter_channels:
     #   return "🖤 [Men's shelter](https://t.me/mens_shelter_01) 🖤"


async def photo_for_post(client, message, new_message, list_words, list_image):
    for words in list_words:
        if words.lower() in message.text.lower():
            await client.send_photo(chat_id=moderator_channel, photo=random.choice(list_image), caption=new_message)
            return
# Проверка на слова и ссылки
link_pattern = r'https?://\S+'


def has_links(text: str) -> bool:
    return bool(re.search(link_pattern, text))


def result_text(message):
    text_array = message.text.split('\n')
    text_array.pop()
    return '\n'.join(text_array)


async def new_post(client: Client, message: Message):
    if message.audio:
        return
    try:
        if message.chat.id == -1001354602307:
            if 'ставк' not in message.text.lower():
                return
            if 'КАЛЕНДАРЬ'.lower() in message.text.lower():
                return
            try:
                text_array = message.text.split('\n')
                text_array.pop()
                new_message_text = '\n'.join(text_array)
                await client.send_message(chat_id=moderator_channel,  text=f"{new_message_text} \n \n {to_whats_channel(message)}   [🔗Источник](https://t.me/market_macro)")
                return
            except Exception as e:
                print(e)
                return

        # if message.chat.id in mens_shelter_channels:
        #     if message.photo or message.video or message.animation:
        #         if message.caption:
        #             if 'instagram' in message.caption:
        #                 insta = message.caption.split(' ')[0]
        #                 message_instagram = f"{insta} \n \n {
        #                     to_whats_channel(message)} "
        #                 await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption=message_instagram)
        #                 return
        #             await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption=f"{message.caption} 🖤 [Men's shelter](https://t.me/mens_shelter_01) 🖤")
        #             return
        #         await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption="🖤 [Men's shelter](https://t.me/mens_shelter_01) 🖤")
        #         return

        # проверка на ссылки
        if not has_links(str(message)):
            # проверка на медиа
            if message.photo or message.video or message.animation:
                if message.caption:
                    try:
                        prompt = prompt_no_link_with_media(
                            message)
                        # Делаем запрос к chat gpt и получаем ответ

                        new_message_text = await g4f.ChatCompletion.create_async(
                            model='gpt-3.5-turbo',
                            messages=[{"role": "user", "content": prompt}],
                        )
                        await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption=f"{new_message_text} \n \n {to_whats_channel(message)}")
                        return
                    except:
                        return
                else:
                    try:
                        prompt = f"""напиши "{to_whats_channel(message)}" """
                        new_message_text = await g4f.ChatCompletion.create_async(
                            model='gpt-3.5-turbo',
                            messages=[{"role": "user", "content": prompt}],
                        )
                        await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption=f"{new_message_text} \n \n {to_whats_channel(message)}")
                        return
                    except:
                        return
            else:
                prompt = prompt_no_link_no_media(message)
                # Делаем запрос к chat gpt и получаем ответ
                new_message_text = await g4f.ChatCompletion.create_async(
                    model='gpt-3.5-turbo',
                    messages=[{"role": "user", "content": prompt}],
                )
                for word in image_dicts_crypto:
                    for words in word['words']:
                        try:
                            if words.lower() in message.text.lower():
                                await client.send_photo(chat_id=moderator_channel, photo=random.choice(word['images']), caption=f"{new_message_text} \n \n {to_whats_channel(message)}")
                                return
                        except:
                            await client.send_message(chat_id=moderator_channel, text=f"{new_message_text} \n \n {to_whats_channel(message)}")
                            return
                await client.send_message(chat_id=moderator_channel, text=f"{new_message_text} \n \n {to_whats_channel(message)}")
                return
        else:
            # проверка на медиа
            if message.photo or message.video or message.animation:
                try:
                    prompt = prompt_with_link_with_media(
                        message)
                    # Делаем запрос к chat gpt и получаем ответ

                    new_message_text = await g4f.ChatCompletion.create_async(
                        model='gpt-3.5-turbo',
                        messages=[{"role": "user", "content": prompt}],
                    )
                    await client.copy_message(chat_id=moderator_channel, from_chat_id=message.chat.id, message_id=message.id, caption=f"{new_message_text} \n \n {to_whats_channel(message)}")
                    return
                except:
                    return
            else:
                try:
                    prompt = prompt_with_link_no_media(
                        message)
                    # Делаем запрос к chat gpt и получаем ответ
                    new_message_text = await g4f.ChatCompletion.create_async(
                        model='gpt-3.5-turbo',
                        messages=[{"role": "user", "content": prompt}],
                    )
                except:
                    return

                for word in image_dicts_crypto:
                    for words in word['words']:
                        try:
                            if words.lower() in message.text.lower():
                                await client.send_photo(chat_id=moderator_channel, photo=random.choice(word['images']), caption=f"{new_message_text} \n \n {to_whats_channel(message)}")
                                return
                        except:
                            await client.send_message(chat_id=moderator_channel, text=f"{new_message_text} \n \n {to_whats_channel(message)}")
                            return
                await client.send_message(chat_id=moderator_channel, text=f"{new_message_text} \n \n {to_whats_channel(message)}")
                return
    except Exception as e:
        print(e)
        return


async def start():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    user_bot = Client(name='user_bot', api_id=api_id_key,
                      api_hash=api_hash_key)
    user_bot.add_handler(MessageHandler(
        new_post, filters.chat(chats=donor_lists)))

    await user_bot.start()
    await idle()
    await user_bot.stop()


if __name__ == '__main__':
    asyncio.run(start())
