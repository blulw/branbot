import discord
import random
import pickledb
from datetime import datetime
from discord.ext import commands
import math
from main import bot, myID


class EZ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @discord.app_commands.command(name="autoplay", description="How to customise the text on the autoplay fix screen")
    async def click(self, interaction: discord.Interaction):
        try:
            embedded_msg = discord.Embed(title="Autoplay Fix")
            embedded_msg.add_field(name="", value="go [here](https://e-z.gg/dash/bio)\n go to file settings\n turn autoplay fix on\n click the cogwheel", inline=True)
            embedded_msg.set_image(url="https://www.bran.lol/img/ez/click.png")
            await interaction.response.send_message(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in autoplay: ```" + str(e) + "```")
            
    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @discord.app_commands.command(name="border", description="How to make border invisible")
    async def border(self, interaction: discord.Interaction):
        try:
            embedded_msg = discord.Embed(title="Invisible Border")
            embedded_msg.add_field(name="", value="go [here](https://e-z.gg/dash/bio)\n go to cosmetic settings\n adjust values according to image", inline=True)
            embedded_msg.set_image(url="https://www.bran.lol/img/ez/border.png")
            await interaction.response.send_message(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in border: ```" + str(e) + "```")
            
    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @discord.app_commands.command(name="rearrange", description="How to rearrange your page")
    async def rearrange(self, interaction: discord.Interaction):
        try:
            embedded_msg = discord.Embed(title="Rearrange Page")
            embedded_msg.add_field(name="", value="go [here](https://e-z.gg/dash/bio)\n go to general settings\n scroll to layout order and adjust to your liking", inline=True)
            embedded_msg.set_image(url="https://www.bran.lol/img/ez/rearrange.png")
            await interaction.response.send_message(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in rearrange: ```" + str(e) + "```")
            
    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @discord.app_commands.command(name="sparkles", description="How to change sparkles colour")
    async def sparkles(self, interaction: discord.Interaction):
        try:
            embedded_msg = discord.Embed(title="Sparkles Colour")
            embedded_msg.add_field(name="", value="Sparkle colour is determined by primary and secondary colours", inline=True)
            embedded_msg.add_field(name="", value="go [here](https://e-z.gg/dash/bio)\n go to cosmetic settings\n adjust to your liking", inline=True)
            embedded_msg.set_image(url="https://www.bran.lol/img/ez/sparkles.png")
            await interaction.response.send_message(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in sparkles: ```" + str(e) + "```")


async def setup(bot):
    await bot.add_cog(EZ(bot))