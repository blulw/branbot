import discord
from discord.ext import commands
from main import bot, myID

class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    logchannel="1304264659569741904"

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.channel.type is discord.ChannelType.private:
                channel = await self.bot.fetch_channel(1304264659569741904)
                embedded_msg = discord.Embed(title="New DM!")
                embedded_msg.add_field(name="",value=message.content)
                embedded_msg.set_footer(text=message.author.name, icon_url=message.author.avatar)
                await channel.send(embed=embedded_msg)
        except Exception as e:
                    user = await self.bot.fetch_user(myID)
                    await user.send("Exception in dmlog: ```" + str(e) + "```")

async def setup(bot):
    await bot.add_cog(Dm(bot))
