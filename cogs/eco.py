import discord
import random
import pickledb
from datetime import datetime
from discord.ext import commands
import math
from main import bot, myID

money = pickledb.load('money.db', True)

class Eco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")
    
    @commands.command(aliases=["w"])
    @commands.cooldown(1,300,commands.BucketType.user)
    async def work(self, ctx):
        try:
            author = str(ctx.author)
            jobs = ['You worked as a barber and earned',
                    'You mowed some lawns and earned',
                    'You worked as a full-stack developer and earned',
                    'You picked up some rubbish and found']
            if not money.exists(author):
                money.set(author, 0)
            earnings = random.randint(5,75)
            job = random.choice(jobs)
            money.append(author, earnings)
            await ctx.send(f'{job} ${earnings}')
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in work: ```" + str(e) + "```")

    @commands.command(aliases=["money", "b", "bal"], description="Displays your balance")
    async def balance(self, ctx):
        try:
            author = str(ctx.author)
            if not money.exists(author):
                money.set(author, 0)
            await ctx.send(f"{author}'s balance: ${money.get(author)}")
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in balance: ```" + str(e) + "```")
    
    @commands.command(description="Resets everyone's money")
    @commands.is_owner()
    async def ecoreset(self, ctx):
        with open('money.db', 'w') as f:
            f.write()
async def setup(bot):
    await bot.add_cog(Eco(bot))