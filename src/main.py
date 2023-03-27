import requests
import random
import discord
from discord.ext.commands import Bot, check, Context

TOKEN = open("TOKEN", "r")


intents = discord.Intents().all()
intents.message_content = True

def get_random_image_with_tag(tag):
    url = f"https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1&tags={tag}"
    try:
        response = requests.get(url)
        data = response.json()
    except:
        return None
    if data:
        post = random.choice(data)
        image_url = f"https://safebooru.org/images/{post['directory']}/{post['image']}"
        return image_url
    else:
        return None
    
f=[
    "hello * I hate you" 
]
    
client = Bot(intents=intents, command_prefix="*")


@client.event
async def on_ready():
    await client.get_channel(1054730196072271893).send(f"im extremely gay")

@client.event
async def on_member_join(member):
    await client.get_channel(1054730196072271893).send(f"{member} is also gay")

@client.event
async def on_message(context: discord.Message):
    if context.author.id==1084800671112507422:
        return
    if not context.content.startswith("*"):
        if "727" in context.content:
            await context.reply("osu")
    await client.process_commands(context)
    

@client.command()
async def howgay(context: Context, arg: discord.Member=None):
    if arg==None:
        arg = context.author
    random.seed(arg.id)
    if arg.id==896405937642942486:
        await context.reply(f"{arg.mention} is 100% gay")
        return
    elif arg.id==721655391481495583:
        await context.reply(f"{arg.mention} is 0% gay")
        return
    await context.reply(f"{arg.mention} is {random.randint(1,100)}% gay")

@client.command()
async def getpic(context: Context, arg: str ):
    pic=get_random_image_with_tag(arg)
    if pic== None:
        pic="pedaret"
    await context.reply(pic)

@client.command()
async def couple(context: Context, per1:discord.Member=None, per2:discord.Member=None):
    if per1==None or per2==None:
        await context.reply("pls tag two people")
        return
    elif per1.id == 896405937642942486 and per2.id == 837648762041401384:
        await context.reply(f"{per1.mention} and {per2.mention} are 100% compatible.")
        return
    elif per1.id == 837648762041401384 and per2.id == 896405937642942486:
        await context.reply(f"{per1.mention} and {per2.mention} are 100% compatible.")
        return
    elif per1.id == 841667295075106856 and per2.id == 721655391481495583:
        await context.reply(f"{per1.mention} and {per2.mention} are 100% compatible.")
        return
    elif per1.id == 721655391481495583 and per2.id == 841667295075106856:
        await context.reply(f"{per1.mention} and {per2.mention} are 100% compatible.")
        return
    random.seed(per1.id+per2.id)
    await context.reply(f"{per1.mention} and {per2.mention} are {random.randint(1,100)}% compatible.")
     
@client.command()
async def flirt(context: Context, arg:discord.Member=None):
    if arg==None:
        arg = context.author
    
    await context.send(random.choice(f).replace("*",arg.mention))

@client.command()
async def ban(context: Context, arg:discord.Member, re:str=None):
    try:
        await arg.ban(reason=re)
        await context.reply("ban was successful.")
    except:
        await context.reply("ban wasn't successful.")


@client.command()
async def rps(context: Context, arg:str=None ):
    if arg==None:
        await context.reply("you didn't choose anything")
        return
    L=["rock", "paper", "scissors"]
    chosenmove=random.choice(L)
    if chosenmove=="rock" and arg=="paper":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, you win!")
        return
    elif chosenmove=="rock" and arg=="scissors":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, I win!")
        return
    elif chosenmove=="rock" and arg=="rock":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, tied!")
        return
    elif chosenmove=="paper" and arg=="paper":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, tied!")
        return
    elif chosenmove=="paper" and arg=="rock":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, I win!")
        return
    elif chosenmove=="paper" and arg=="scissors":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, you win!")
        return
    elif chosenmove=="scissors" and arg=="paper":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, I win!")
        return
    elif chosenmove=="scissors" and arg=="rock":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, you win!")
        return
    elif chosenmove=="scissors" and arg=="scissors":
        await context.reply(f"you chose {arg}, I chose {chosenmove}, tied!")
        return
    else:
        await context.reply("BILAKH!!")
        

 


client.run(TOKEN.read())