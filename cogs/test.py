import discord
import random
import pickledb
from datetime import datetime
from discord.ext import commands
import math
from main import bot, myID
from thispersondoesnotexist import get_online_person, save_picture

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

            picture = await get_online_person()

            filename = "person.jpeg"
            await save_picture(picture, f"{filename}")

            file = discord.File(fp=filename, filename=filename)

            await ctx.send(file=file)

        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in test: ```" + str(e) + "```")


async def setup(bot):
    await bot.add_cog(Test(bot))