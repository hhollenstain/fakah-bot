#!/usr/bin/env python3
"""
Tamago BOT LIVES!
"""
import asyncio
import random
import os
import discord
import importlib
import logging
import coloredlogs
import sys
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from fakah.lib import plugin, utils
from fakah.fakah import Fakah

EXTENSIONS = [
    'fakahchannels',
    'server',
    ]

LOG = logging.getLogger(__name__)

APP_ID = os.getenv('APP_ID') or 'fakeid'
BOT_PREFIX = ("?", "!")
SHARD = os.getenv('SHARD') or 0
SHARD_COUNT = os.getenv('SHARD_COUNT') or 1
TOKEN = os.getenv('TOKEN')
VOICE_CHANNEL_PREFIX = os.getenv('VOICE_CHANNEL_PREFIX') or 'GAME-ROOMS'

def main():
    """Entrypoint if called as an executable."""
    args = utils.parse_arguments()
    logging.basicConfig(level=logging.INFO)
    coloredlogs.install(level=0,
                        fmt="[%(asctime)s][%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                        isatty=True)
    if args.debug:
        l_level = logging.DEBUG
    else:
        l_level = logging.INFO

    logging.getLogger(__package__).setLevel(l_level)
    logging.getLogger('discord').setLevel(l_level)
    logging.getLogger('websockets.protocol').setLevel(l_level)
    logging.getLogger('urllib3').setLevel(l_level)

    LOG.info("LONG LIVE Fakah")
    fakah = Fakah(shard_id=int(SHARD), shard_count=int(SHARD_COUNT),
                    command_prefix=BOT_PREFIX, app_id=APP_ID, voice_channel_prefix=VOICE_CHANNEL_PREFIX)

    for extension in EXTENSIONS:
        plugin.load('fakah.lib.plugins.{}'.format(extension), fakah)

    fakah.run(TOKEN)

if __name__ == '__main__':
    main()
