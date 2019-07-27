import asyncio
import discord
import logging
import random
from discord import Game
from discord.ext import commands
from fakah.lib import utils

LOG = logging.getLogger(__name__)


async def purge_unused_vc(fakah):
    while not fakah.is_closed():
        purged_channel_count = 0
        for server in fakah.guilds:
            fakah_channels = [vc for vc in server.voice_channels if  vc.name.startswith(fakah.voice_channel_prefix)]
            for vc in fakah_channels:
                if len(vc.members) < 1:
                    purged_channel_count += 1
                    LOG.info(f'Deleting Voice Channel: {vc.name} from GUILD: {server.name}')
                    await vc.delete(reason='fakah does not like unused channels cluttering up his 720 display')
        LOG.info(f'Purged {purged_channel_count} Channels this loop')
        await asyncio.sleep(60)


class FakahUnknownCategory(commands.CommandError):
    """Custom Exception class for unknown category errors."""

class FakahChannels(commands.Cog):
    def __init__(self, fakah):
        self.fakah = fakah

    @commands.Cog.listener()
    async def on_ready(self):
        LOG.info('Starting Voice Channel purger loop')
        self.fakah.loop.create_task(purge_unused_vc(self.fakah))


    @commands.command()
    async def gc(self, ctx, *, gcrequest: str=''):

        #await ctx.send(discord.utils.find(lambda m: m.name == 'HANK-test', ctx.guild.categories))
        #await ctx.send(discord.utils.get(ctx.guild.categories, name='test-cat'))
        #await ctx.send(discord.utils.get(ctx.guild.categories, name="HANK-test"))
        #await ctx.send('looking for {}'.format(discord.utils.get(ctx.guild.categories, name="test-cat")))
        #await ctx.send(dir(ctx.guild))
        # fakah_cat = discord.utils.get(ctx.guild.categories, name="test-cat")
        #await ctx.send(discord.utils.get(ctx.guild.categories, name="test-cat"))
        #await ctx.send(fakah_cat.fetch_channels())
        #await ctx.send(dir(fakah_cat))
        # for vchannel in fakah_cat.voice_channels:
        #     msg = dir(vchannel)
        #     break
        #await ctx.send(fakah_cat.voice_channels.count())
        #await ctx.send(len(vchannel.members))
        #await ctx.send(ctx.guild.voice_channels)
        # vcs = [vc for vc in ctx.guild.voice_channels if  vc.name.startswith('24/7 -')]
        # await ctx.send(vcs)
        #await ctx.send(discord.utils.find(lambda m: m.name == 'test-', ctx.guild.voice_channels))


        data =  await self.parse(ctx, gcrequest )
        if data['category'] is None:
            raise FakahUnknownCategory(f'Unknown Discord category')
        cat_name = [cat for cat in ctx.guild.categories if cat.name.lower() in data['category']][0]
        fakah_number = self.channel_number(ctx, data)
        created_channel = await ctx.guild.create_voice_channel(f'{self.fakah.voice_channel_prefix}{data["category"]} {fakah_number}', overwrites=None, category=cat_name, reason='Fakah bot automation')

        await ctx.send(created_channel)

        #await ctx.send(dir(discord.utils.get(ctx.guild.categories, name="HANK-test").name))

    def channel_number(self, ctx, data):
        fakah_channels = [vc for vc in ctx.guild.voice_channels if vc.name.startswith(f'{self.fakah.voice_channel_prefix}{data["category"]}')]
        return (len(fakah_channels) + 1)

    async def parse(self, ctx, gcrequest):
        server_cats = self.cat_names(ctx)
        category = None
        number_of_users = 10
        gcrequest = gcrequest.lower().split()
        data = {}
        for info in gcrequest:
            if info in server_cats:
                category = info
        data['category'] = category
        data['number_of_users'] = number_of_users
        return data

    def cat_names(self, ctx):
        cat_list = []
        for cat in ctx.guild.categories:
            cat_list.append(cat.name.lower())
        return cat_list

    @gc.error
    async def fakah_handler(self, ctx, error):
        embed = discord.Embed(
            title = 'Fakah error',
            colour = discord.Colour.red()
        )
        if isinstance(error, FakahUnknownCategory):
            msg = 'Unkonwn category, please type in an existing category in this Server'
        else:
            msg = error
        embed.add_field(name='Error', value=msg)
        await ctx.send(embed=embed)


def setup(fakah):
    fakah.add_cog(FakahChannels(fakah))
