from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать общение'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='wt',
            description='удобный интерфейс с выбором'
        ),
        BotCommand(
            command='weather',
            description='weather <город> для определенного города'
        )
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())