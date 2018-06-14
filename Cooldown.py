# this file is specialy maded for commands that have cooldowns
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Cooldowns():
    def __init__(self, bot):
        self.bot = bot

  @commands.cooldown(1, 86400, commands.BucketType.user)
  @commands.command(aliases=[dCafe])
  async def DailyCafe(ctx):
      Cafe = discord.Embed(title="Your daily Cafe", color=0xff8080)
      Cafe.add_field(name="You didin't get you daily cafe? Here it is ☕", value="Everyone Loves coffee no?", inline=False)
      Cafe.set_footer(text="Note : Here is a cooldown for this command.")
      await ctx.send(embed=Cafe)
     
   @commands.cooldown(1, 10, commands.BucketType.user)
   @commands.command()
   async def coinflip(self, ctx):
       choice = random.randint(1,2)
       if choice == 1:
           embed=discord.Embed(title="you flipped tails", color=0xff0000)
           embed.set_image(url="https://image.prntscr.com/image/XIhcumqjRB_FjHzPCz-jOQ.png")
           await ctx.send(embed=embed)
       if choice == 2:
           embed=discord.Embed(title="You flipped heads", color=0xff0000)
           embed.set_image(url="https://image.prntscr.com/image/rco6mQybS7aJcqfW7RK59Q.png")
           await ctx.send(embed=embed)
           
def setup(bot):
    bot.add_cog(Cooldowns(bot))
