from discord.ext import commands


class Smarts(commands.Cog):
    """Comandos inteligentes"""
    def __init__(self, bot):
      self.bot = bot

    @commands.command(name="calcular", help="Calcula uma expressão")
    async def calculate_expression(self, ctx, *expression):
      expression = "".join(expression)
      print(expression)
      response = eval(expression)
      await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Smarts(bot))