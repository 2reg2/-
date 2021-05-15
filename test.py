import discord
from discord import client
from discord import member
from discord import role
from discord.colour import Color
from time import time


from discord.ext import commands

from discord.ext.commands import Bot

TOKEN = "ODQwOTMxOTM5NTIyMTgzMjA4.YJfY5g.dXeSiurbG_B9D2CHG-8BtQ3iSlU"

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )




#запуск
@bot.event
async def on_ready():
    print("Я запущен!")


@bot.command()
async def hi(ctx):
    embed = discord.Embed(
        title="Привет всем!",)
    await ctx.send(embed=embed)

@bot.command()
async def t12(ctx):
    embed = discord.Embed(
        title="если готов поставь :white_check_mark:",)
    await ctx.send(embed=embed)



@bot.command(pass_context = True)
async def rit(ctx):
    
    for i in range(3) :
     await ctx.send(l = range(1, 6) )


@bot.command(pass_context = True)
async def start(ctx):
  await ctx.send("если готов то напиши (+ready)!",)

    

@bot.command()
async def ready(ctx):
    world = []
    world.append (input({member.name}))
    i = len(world) 
    if (i % 2) == 0:
            n = 0
            time_user = int(10)
            comment = str ("время вышло")
            for q in range (time_user):
                time.sleep(1)
                n += 1

            await ctx.send("время вышло",)
    else:
          await ctx.send("недостаточно играков")
         


bot.run(TOKEN)
