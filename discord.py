import discord
from discord.ext import commands

#creacion y configuracion de los permisos
permisos=discord.Intents.default()
permisos.message_content=True

#creacion del bot
coco = commands.bot(command_prefix="/" ,intents= permisos)

# eventos
@coco.event
async def on_ready():
    print("El bot esta en linea")

@coco.command()
async def hola(ctx):
    await ctx.send(f" Hola mi nombre es{coco.user.name}")

coco.run("TOKEN")

@coco.command()
async def como (ctx):
    await ctx.send(f" Como puedo ayudar? {user.question}")

@coco.command()
async def como (ctx):
    await ctx.send(f"Analyzing question")

import datetime
from discord.ext import commands, tasks

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=8, minute=30, tzinfo=utc)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        print("My task is running!")
        
@bot.command()
async def algo(ctx):
    await ctx.send(f"Algo mas que puedo aser por ti? {user.respond}")
    
@coco.command()
async def adios(ctx):
    await ctx.send(f"Adios {user.respond}")

    bot.run("token")
