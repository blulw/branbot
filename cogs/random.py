import discord
from discord.ext import commands
import requests 
from main import bot, myID
from thispersondoesnotexist import get_online_person, save_picture

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command(aliases=["meow", "kitty"], description="shows a random cat image")
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
            #await ctx.send("cataas broken, if i keep this working the bot breaks")
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in cat: ```" + str(e) + "```")
            
    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @bot.tree.command(name="cat", description="shows a random cat image")
    async def meow(self, interaction: discord.Interaction):
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
            #await interaction.response.send_message("cataas broken, if i keep this working the bot breaks")
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in cat: ```" + str(e) + "```")

    @commands.command(aliases=["astrid", "ash"], description="shows a random glaive image")
    async def glaive(self, ctx):
        try:
            url = 'https://api.bran.lol/glaive'

            embedded_msg = discord.Embed(title="gaive!")
            embedded_msg.set_image(url=url)
            embedded_msg.set_footer(text="Provided by api.bran.lol", icon_url=ctx.message.author.avatar)
            await ctx.send(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in glaive: ```" + str(e) + "```")

    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @bot.tree.command(name="glaive", description="shows a random glaive image")
    async def astrid(self, interaction: discord.Interaction):
        try:
            url = 'https://api.bran.lol/glaive'

            embedded_msg = discord.Embed(title="gaive!")
            embedded_msg.set_image(url=url)
            embedded_msg.set_footer(text="Provided by api.bran.lol", icon_url=interaction.user.avatar)
            await interaction.response.send_message(embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in glaive: ```" + str(e) + "```")

    @commands.command(aliases=["woof", "bark", "puppy"], description="shows a random dog image")
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

    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
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


    @commands.command(aliases=["human", "tpdni"], description="shows a random human image")
    async def person(self, ctx):
        try:
            picture = await get_online_person()

            filename = "person.jpeg"
            await save_picture(picture, f"{filename}")

            file = discord.File(fp=filename, filename=filename)

            embedded_msg = discord.Embed(title="")
            embedded_msg.set_image(url="attachment://person.jpeg")
            embedded_msg.set_footer(text="Provided by thispersondoesnotexist", icon_url=ctx.message.author.avatar)

            await ctx.send(file=file, embed=embedded_msg)
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in person: ```" + str(e) + "```")
            

    @discord.app_commands.guild_install(func=None)
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @bot.tree.command(name="human", description="shows a random human image")
    async def human(self, interaction: discord.Interaction):
        try:
            picture = await get_online_person()

            filename = "person.jpeg"
            await save_picture(picture, f"{filename}")

            file = discord.File(fp=filename, filename=filename)

            embedded_msg = discord.Embed(title="")
            embedded_msg.set_image(url="attachment://person.jpeg")
            embedded_msg.set_footer(text="Provided by thispersondoesnotexist", icon_url=interaction.user.avatar)

            await interaction.response.send_message(file=file, embed=embedded_msg)
            
        except Exception as e:
            user = await self.bot.fetch_user(myID)
            await user.send("Exception in human: ```" + str(e) + "```")
            
    # @bot.tree.command(name="lol", description="shows a random human image")
    # async def lol(self, interaction: discord.Interaction, search: str=None):
    #     try:
    #         link = "https://kuuichi.xyz"
    #         if search != None:
    #             link = "https://kuuichi.xyz?file=" + search
    #         await interaction.response.send_message(link)
    #         embedded_msg = discord.Embed(title="")
    #         embedded_msg.set_image(url=link)
    #         embedded_msg.set_footer(text="Provided by keiran", icon_url=interaction.user.avatar)

    #         await interaction.response.send_message(embed=embedded_msg)
            
    #     except Exception as e:
    #         user = await self.bot.fetch_user(myID)
    #         await user.send("Exception in lol: ```" + str(e) + "```")
async def setup(bot):
    await bot.add_cog(Random(bot))
