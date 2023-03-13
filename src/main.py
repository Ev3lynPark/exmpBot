import random
import discord
from discord.ext.commands import Bot, check, Context

TOKEN = open("TOKEN", "r")


intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents, command_prefix="*")


@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.command(pass_context=True, invoke_without_command=True)
async def doxx(context: Context, arg):
    await context.reply(f"{arg}'s ip is {random.randint(10,255)}.{random.randint(10,255)}.{random.randint(10,255)}.{random.randint(10,255)}")



client.run(TOKEN.read())