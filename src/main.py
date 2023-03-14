import random
import discord
from discord.ext.commands import Bot, check, Context

TOKEN = open("TOKEN", "r")


intents = discord.Intents().all()
intents.message_content = True

client = Bot(intents=intents, command_prefix="*")


@client.event
async def on_ready():
    await client.get_channel(1054730196072271893).send(f"im extremely gay")

@client.event
async def on_member_join(member):
    await client.get_channel(1054730196072271893).send(f"{member} is also gay")


@client.event
async def on_message(message):
    if message.author.id == 1084800671112507422:
        return
    else:
        await message.channel.send("gay")


@client.command(pass_context=True, invoke_without_command=True)
async def doxx(context: Context, arg):
    await context.reply(f"{arg}'s ip is {random.randint(10,255)}.{random.randint(10,255)}.{random.randint(10,255)}.{random.randint(10,255)}")



client.run(TOKEN.read())