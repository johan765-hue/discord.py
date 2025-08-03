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

@bot.command()
async def algo(ctx):
    await ctx.send(f"Algo mas que puedo aser por ti? {user.respond}")
    
@coco.command()
async def adios(ctx):
    await ctx.send(f"Adios {user.respond}")

    bot.run("token")
