import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='g!', help_command=None)


@bot.command(name="help", description="ve la lista de comandos")
async def help(ctx):
    embed = discord.Embed(title= "help", description=f"lista de comandos", color=discord.Color.blue())
    embed.add_field(name='administracion', value='`say`, `anuncio`, `info`, `user`')

    embed.add_field(name='moderacion', value='`mute` ,`unmute` , `tempmute`, `kick`, `ban`')

    embed.add_field(name='diversion', value='`_8ball`, `avatar`, `kiss`, `mimir`, `cry`, `hug`, `punch`, `sabias`, `poli`, `pat`, `blush`, `nivel`, `l`, `scared`, `drog`', inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    game = discord.Game('Beta v 0.0.4')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Bot cargado')




bot.load_extension("cogs.Misc")
bot.load_extension("cogs.Funny")
bot.load_extension("cogs.Admin")
bot.run(TOKEN)
