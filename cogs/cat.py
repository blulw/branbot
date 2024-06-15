import discord
from discord.ext import commands
import requests 
from main import bot, myID


class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command(aliases=["meow", "kitty"])
    async def cat(self, ctx):
        try:
            url = 'https://cataas.com/cat'
            filename = 'cat.jpg'

            r = requests.get(url)

            with open(filename,'wb') as f:
                f.write(r.content)
            file = discord.File("cat.jpg", filename="cat.jpg")
            embedded_msg = discord.Embed(title="KITTYYYYYY!")
            embedded_msg.set_image(url="attachment://cat.jpg")
            embedded_msg.set_footer(text="Provided by CATAAS", icon_url=ctx.message.author.avatar)
            await ctx.send(file=file, embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in cat: ```" + str(e) + "```")
            

    @bot.tree.command(name="cat", description="shows a random cat image")
    async def cat(self, interaction: discord.Interaction):
        try:
            url = 'https://cataas.com/cat'
            filename = 'cat.jpg'

            r = requests.get(url)

            with open(filename,'wb') as f:
                f.write(r.content)
            file = discord.File("cat.jpg", filename="cat.jpg")
            embedded_msg = discord.Embed(title="KITTYYYYYY!")
            embedded_msg.set_image(url="attachment://cat.jpg")
            embedded_msg.set_footer(text="Provided by CATAAS", icon_url=interaction.user.avatar)
            await interaction.response.send_message(file=file, embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in cat: ```" + str(e) + "```")

async def setup(bot):
    await bot.add_cog(Cat(bot))
