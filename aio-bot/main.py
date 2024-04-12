import asyncio

from aiogram import Bot, Dispatcher, types

from app.handlers import router


# бот - это сервер который будет взаимодействовать с API телеграмма


async def main():
    # создаем бота
    bot = Bot(token='')
    dp = Dispatcher()  # диспатчер инициализирует все входящие апдейты.
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен!')
