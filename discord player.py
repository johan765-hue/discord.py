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
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    
@bot.command()
async def algo(ctx):
    await ctx.send(f"Algo mas que puedo aser por ti? {user.respond}")
    
@coco.command()
async def adios(ctx):
    await ctx.send(f"Adios {user.respond}")

    bot.run("token")
