import discord
from discord import app_commands
from discord.ext import commands
import random
import asyncio
from main import bot, myID

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command(aliases=["d", "roll"], description="rolls a random number between 1 and 6")
    async def dice(self, ctx, sides=None):
        try:
            if sides == None:
                await ctx.send("You rolled " + str(random.randint(1,6)))
            elif int(sides) < 1:
                await ctx.send("Number of sides must be above 1!")
            else:
                await ctx.send("You rolled " + str(random.randint(1,int(sides))))
        except Exception as e:
            if "invalid literal for int() with base 10:" in str(e):
                await ctx.send("Number must be an integer!")
            else:
                user = await self.bot.fetch_user(myID)
                await user.send("Exception in dice: ```" + str(e) + "```")

    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @bot.tree.command(name="dice", description="rolls a random number between 1 and 6")
    @app_commands.describe(sides="the upper limit for your roll")
    async def roll(self, interaction: discord.Interaction, sides: int=None):
        try:
            if sides == None:
                await interaction.response.send_message("You rolled " + str(random.randint(1,6)))
            elif int(sides) < 1:
                await interaction.response.send_message("Number of sides must be above 1!")
            else:
                await interaction.response.send_message("You rolled " + str(random.randint(1,int(sides))))
        except Exception as e:
            if "invalid literal for int() with base 10:" in str(e):
                await interaction.response.send_message("Number must be an integer!")
            else:
                user = await self.bot.fetch_user(myID)
                await user.send("Exception in dice: ```" + str(e) + "```")
                    

async def setup(bot):
    await bot.add_cog(Fun(bot))