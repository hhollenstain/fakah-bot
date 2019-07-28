import discord
import logging
import random
from discord import Game
from discord.ext import commands
from fakah import VERSION
from fakah.lib import utils

LOG = logging.getLogger(__name__)



class Server(commands.Cog):
    def __init__(self, fakah):
        self.fakah = fakah

    @commands.Cog.listener()
    async def on_ready(self):
        await self.fakah.change_presence(status=discord.Status.idle, activity=Game('Waking up, making coffee...'))
        LOG.info('Logged in as {}'.format(self.fakah.user.name))
        self.fakah.loop.create_task(utils.change_status(self.fakah))
        self.fakah.loop.create_task(utils.list_servers(self.fakah))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            LOG.error(error)
            msg = '{} Error running the command'.format(ctx.message.author.mention)
        if isinstance(error, commands.CommandNotFound):
            msg = '{} the command you ran does not exist please use !help for assistance'.format(ctx.message.author.mention)
        if isinstance(error, commands.CheckFailure):
            msg = ':octagonal_sign: you do not have permission to run this command, {}'.format(ctx.message.author.mention)
        if isinstance(error, commands.MissingRequiredArgument):
            msg = 'Missing required argument: ```{}```'.format(error)

        if not msg:
            msg = 'Oh no, I have no idea what I am doing! {}'.format(error)


        await ctx.send('{}'.format(msg))

    @commands.command()
    async def fakah(self, ctx):
        embed = discord.Embed(
            title = 'fakah Bot',
            description = 'fakah Bot information',
            colour = discord.Colour.green()
        )

        fakah_avatar = [
                         'https://cdn.discordapp.com/attachments/295256054260826112/604752148227424286/44118538_10217585300408223_1134323183818637312_n.png',
                        ]

        embed.set_author(name='Fakahuman')
        embed.set_thumbnail(url=random.choice(fakah_avatar))
        embed.add_field(name='description', value=f'fakah is a WIP, add Fakahuman to your server! [add me]( https://discordapp.com/oauth2/authorize?client_id={self.fakah.app_id}&scope=bot)', inline=True)
        embed.add_field(name='Version', value=VERSION, inline=True)

        await ctx.send(embed=embed)

def setup(fakah):
    fakah.add_cog(Server(fakah))
