import discord
from discord.ext import commands
from main import bot, myID, prefix, defaultPrefix
import asyncio
import pickledb
import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import urllib.parse


# load_dotenv()
# mongouser = os.getenv('mongouser')
# mongopass = os.getenv('mongopass')

# username = urllib.parse.quote_plus(mongouser)
# password = urllib.parse.quote_plus(mongopass)

# uri = f"mongodb+srv://{username}:{password}@branbot.lkbyedj.mongodb.net/?retryWrites=true&w=majority&appName=branbot"

# # Create a new client and connect to the server
# cluster = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     cluster.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# bot_channels = [1251256423711772732]

# level = ["level 5", "level 10", "level 15"]
# levelnum = [5,10,15]

# levelling = cluster["discord"]["levelling"]

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")


    # @commands.command()
    # async def addxp(self, ctx, amt, id = None):
    #     try:
    #         if ctx.author.id == myID:
    #             if id == None:
    #                 id = myID
    #             stats = levelling.find_one({"id" : id})
    #             if stats is None:
    #                     newuser = {"id" : id, "xp": 100}
    #                     levelling.insert_one(newuser)
    #             if float(amt) % 5 == 0:    
    #                 xp = int(stats["xp"])
    #                 xp = xp+int(amt)
    #             else:
    #                 xp = stats["xp"]
    #                 await ctx.send("Number must be a multiple of 5!")
    #             levelling.update_one({"id":id}, {"$set":{"xp":xp}})
    #             await ctx.send(f"added {amt}xp to <@{id}>")
    #         else:
    #             pass
    #     except Exception as e:
    #         user = await self.bot.fetch_user(myID)
    #         await user.send("Exception in addxp: ```" + str(e) + "```")
    
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.content.startswith("<@1242563143910035546>"):
    #         if prefix == None:
    #             pfx = defaultPrefix
    #         else:
    #             pfx = prefix
    #         e = discord.Embed(title="Prefix", description=f"Current prefix is {pfx}")
    #         await message.channel.send(embed=e)
    #     else:
    #         if message.channel.id not in bot_channels:
    #             stats = levelling.find_one({"id" : message.author.id})
    #             if not message.author.bot:
    #                 if stats is None:
    #                     newuser = {"id" : message.author.id, "xp": 100}
    #                     levelling.insert_one(newuser)
    #                 else:
    #                     xp = stats["xp"] + 5
    #                     levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
    #                     lvl = 0
    #                     while True:
    #                         if xp < ((50*(lvl**2))+(50*(lvl))):
    #                             break
    #                         lvl += 1
    #                     xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
    #                     if xp == 0:
    #                         await message.channel.send(f"{message.author.mention}'s dick grew to {lvl} inches!")
    #                         for i in range(len(level)):
    #                             if lvl == levelnum[i]:
    #                                 await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
    # @commands.command(aliases=["level", "r", "lvl"], description="Shows your level and your progress to the next level")
    # async def rank(self, ctx):
    #     try:
    #         stats = levelling.find_one({"id" : ctx.author.id})
    #         if stats is None:
    #             embed = discord.Embed(description="You have no rank")
    #             await ctx.send(embed=embed)
    #         else:
    #             xp = stats["xp"]
    #             lvl = 0
    #             rank = 0
    #             while True:
    #                 if xp < ((50*(lvl**2))+(50*(lvl))):
    #                     break
    #                 lvl += 1
    #             xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
    #             boxes = int((xp/(200*((1/2) * lvl)))*20)
    #             rankings = levelling.find().sort("xp",-1)
    #             for x in rankings:
    #                 rank += 1
    #                 if stats["id"] == x["id"]:
    #                     break
    #             embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
    #             embed.add_field(name="Name", value=ctx.author.mention, inline=True)
    #             embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
    #             embed.add_field(name='Level', value=f'{lvl}', inline=True)
    #             embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
    #             embed.add_field(name="Progress Bar", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
    #             embed.set_thumbnail(url=ctx.author.avatar)
    #             await ctx.send(embed=embed)
    #     except Exception as e:
    #         user = await self.bot.fetch_user(myID)
    #         await user.send("Exception in rank: ```" + str(e) + "```")
    #@commands.command(aliases=["lb"])
    # async def leaderboard(self, ctx):
    #     try:
    #         rankings = levelling.find({}).sort({ 'xp' : -1 })
    #         print(f"rankings = {rankings}")
    #         i = 1
    #         embed = discord.Embed(title="Rankings:")
    #         for x in rankings:
    #             try:
    #                 temp = ctx.guild.get_member(x["id"])
    #                 print(f"temp = {temp}")
    #                 tempxp = x["xp"]
    #                 print(f"tempxp = {tempxp}")
    #                 embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
    #                 i+= 1
    #             except:
    #                 pass
    #             if i == 11:
    #                 break
    #         print(f"embed = {embed}")
    #         await ctx.send(embed=embed)
    #     except Exception as e:
    #         user = await self.bot.fetch_user(myID)
    #         await user.send("Exception in leaderboard: ```" + str(e) + "```")
async def setup(bot):
    await bot.add_cog(Levels(bot))