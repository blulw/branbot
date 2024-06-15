import discord
import random
import pickledb
from datetime import datetime
from discord.ext import commands
import math

db = pickledb.load('discord.db', True)

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command()
    async def test(self, ctx):
        try:
            author = str(ctx.author)
            if not db.exists(author):
                db.set(author, 0)
            db.append(author, 1)
            await ctx.reply(f'you have run this command {db.get(author)} times.')
        except Exception as e:
            user = await self.bot.fetch_user('817475032112037888')
            await user.send("Exception in test: ```" + str(e) + "```")

async def setup(bot):
    await bot.add_cog(Test(bot))