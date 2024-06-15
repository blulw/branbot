import discord
from discord.ext import commands
import requests 
from main import bot, myID


class Dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command(aliases=["woof", "bark", "puppy"])
    async def dog(self, ctx):
        try:
            url = 'https://random.dog/woof'

            r = requests.get(url)

            extension = str(r.content)

            extension = extension[1:].replace("'", "")

            
            url = f'https://random.dog/{extension}'
            filename = 'dog.jpg'

            r = requests.get(url)

            with open(filename,'wb') as f:
                f.write(r.content)
            
            file = discord.File("dog.jpg", filename="dog.jpg")
            embedded_msg = discord.Embed(title="dog.")
            embedded_msg.set_image(url="attachment://dog.jpg")
            embedded_msg.set_footer(text="Provided by random.dog", icon_url=ctx.message.author.avatar)
            await ctx.send(file=file, embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in dog: ```" + str(e) + "```")

    @bot.tree.command(name="dog", description="shows a random dog image")
    async def woof(self, interaction: discord.Interaction):
        try:
            url = 'https://random.dog/woof'

            r = requests.get(url)

            extension = str(r.content)

            extension = extension[1:].replace("'", "")

            
            url = f'https://random.dog/{extension}'
            filename = 'dog.jpg'

            r = requests.get(url)

            with open(filename,'wb') as f:
                f.write(r.content)
            
            file = discord.File("dog.jpg", filename="dog.jpg")
            embedded_msg = discord.Embed(title="dog.")
            embedded_msg.set_image(url="attachment://dog.jpg")
            embedded_msg.set_footer(text="Provided by random.dog", icon_url=interaction.user.avatar)
            await interaction.response.send_message(file=file, embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in dog: ```" + str(e) + "```")
async def setup(bot):
    await bot.add_cog(Dog(bot))
