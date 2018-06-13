import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='c.', description='With the cats')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Prefix -> c.'), status='dnd')
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    
@bot.command()
async def ping(self, ctx):
    """Pong!"""
    em = discord.Embed(title="Pong!", description="Your ping: {} ms".format(round(self.bot.latency*1000, 1)), colour=discord.Colour.orange())
    await ctx.send(embed=em)
    
@bot.command()
async def userinfo(self, ctx):
    embed = discord.Embed(title="User Info", colour=0xff8080)
    embed.add_field(name="ID", value="{}".format(ctx.author.id), inline=False)
    embed.add_field(name="UserName", value="{}".format(ctx.author.name), inline=False)
    embed.add_field(name="Status", value="{}".format(ctx.author.status), inline=False)
    await ctx.send(embed=embed)
    
    
bot.run('your_token_here')
