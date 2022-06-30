from discord.ext import commands, tasks
import datetime 


class Dates(commands.Cog):
    """Trabalhar com Datas"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(hours=12)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%y às %H:%M:%S")
        channel = self.bot.get_channel(476216220610330653)
        await channel.send("BOT criado para o grupo The emissaries of death. Data atual: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))