import logging
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('BOT-MAIN')

bot = commands.Bot(
    command_prefix=None,
    intents=discord.Intents.default(),
    activity=discord.Activity(type=discord.ActivityType.listening, name='Rocket League Music'),
    status=discord.Status.online,
    sync_commands=False,
    delete_not_existing_commands=False,
)

if __name__ == '__main__':
    log.info('Starting Bot....'),
    bot.run(os.getenv('BOT_TOKEN')),

