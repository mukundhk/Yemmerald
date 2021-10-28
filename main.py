import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive
from replit import db

client = commands.Bot(command_prefix='y.',help_command=None)
token = os.environ['token']

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game("y.help"))
  print("Bot online as {0.user}".format(client))

@client.event
async def on_message(ctx):
  msg = ctx.content.lower()
  if ctx.author.bot:
    return
  elif msg == "hello there":
    await ctx.reply("https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326")
    await ctx.channel.send("https://tenor.com/view/star-wars-general-grevious-bold-one-gif-12332693")
    await ctx.channel.send("https://tenor.com/view/hello-there-kenobi-greivous-lightsaber-gif-16652462")

  elif msg == 'f':
    await ctx.reply(random.choice(db['f_gifs']))

  elif msg in db["salam_i"]:
    await ctx.reply(random.choice(db["salam_o"]))
  await client.process_commands(ctx)

@client.command(name="fulldb")
async def fulldb(ctx):
   for i in db.keys():
      await ctx.reply(f"{i}={db[i]}")

@client.command(name="help")
async def help(ctx):
  embedVar = discord.Embed(title="Yemmerald v2.3.2",description="Bot made by **@Zeus_1347#0765**. Please DM if the bot is offline or if you have any suggestions or feedback. \n ",color=0x26a43b)
  embedVar.set_thumbnail(url="https://i.imgur.com/iJn5Kgn.png")
  embedVar.add_field(name="Useless Unit Convertor",value="Use `y.convert <amount> <unit>` \nConverts your lengths, weights and time to random useless units",inline=False)
  embedVar.add_field(name="Spam",value="Use `y.spam <user> <message> <number>` \nSpams a mentioned user the specified number of times. \n<number> is an optional parameter\nIf you want the message to have more than one word, use quotes")
  embedVar.add_field(name="Spam DM",value="Use `y.spamdm <user> <message> <number>` \nSpams a mentioned user in their DM the specified number of times. Use this when you dont want to spam on the server \n<number> is an optional parameter\nIf you want the message to have more than one word, use quotes")
  embedVar.add_field(name="Hello There",value="Replies with General Kenobi",inline=False)
  embedVar.add_field(name="Salam",value="Replies with Alaikum Assalam",inline=False)
  embedVar.add_field(name="F",value="Replies with F to pay  respects",inline=False)
  embedVar.set_footer(text="PS: If you are a Mod, change the **@Yemmerald** role's color to `#26a43b` for __*~aEsThEtIcS~*__.")
  await ctx.reply(embed=embedVar)

@client.command(name='poll')
async def poll(ctx,*args):
  response=f'<@everyone>'
  for i in args:
    response+=f"\n{i}"
  await ctx.send(response)
  
@client.command(name='spam')
async def spam(ctx,user:discord.User,message, num=1):
  if num>0:
    num=20
  for i in range(int(num)):
    await ctx.send(f"{user.mention} {message}")

@client.command(name='spamdm')
async def spamdm(ctx,user: discord.User, message, num=1):
  if num>20:
    num=20
  for i in range(int(num)):
    await user.send(f"{user.mention} {message}")

@client.command(name="convert")
async def convert(ctx,amount:float,unit):
  if amount == int(amount): 
    amount = int(amount)
  amount_c = amount
  if unit in ["m", "metre", "meter", "meters", "metres"]:
    unit_type_choice=random.choice(db['length'])
  elif unit in ["cm", 'centimeter', 'centimetre', 'centimeters','centimetres','cms']:
    amount_c /= 100
    unit_type_choice=random.choice(db['length'])
  elif unit in ['in','inches', 'inch']:
    amount_c /= 39.37
    unit_type_choice=random.choice(db['length'])
  elif unit in ['feet', 'foot', 'ft']:
    amount_c /= 3.281
    unit_type_choice=random.choice(db['length'])
  elif unit in ['kilometers','kilometres','kilometer','kilometre','km','kms']:
    amount_c*=1000
    unit_type_choice=random.choice(db['length'])
  elif unit in ['kg','kilogram','kgs','kilograms','kilo','kilos']:
    unit_type_choice=random.choice(db['weight'])
  elif unit in ['g','gs','gram','grams']:
    amount_c*=1000
    unit_type_choice=random.choice(db['weight'])
  elif unit in ['lb','lbs','pound','pounds']:
    amount_c/=2.205
    unit_type_choice=random.choice(db['weight'])
  elif unit in ['ounce','ounces','oz']:
    amount_c/=35.274
    unit_type_choice=random.choice(db['weight'])
  elif unit in ['ton','tons','tonne','tonnes']:
    amount_c/=1000
    unit_type_choice=random.choice(db['weight'])
  elif unit in ['hours','hour','hrs']:
    unit_type_choice=random.choice(db['time'])
  elif unit in ['minutes','minute','min','mins']:
    amount_c/=60
    unit_type_choice=random.choice(db['time'])
  elif unit in ['seconds','second','sec','secs']:
    amount_c/=3600
    unit_type_choice=random.choice(db['time'])
  elif unit in ['days','day']:
    amount_c*=24
    unit_type_choice=random.choice(db['time'])
  elif unit in ['weeks','week']:
    amount_c*=168
    unit_type_choice=random.choice(db['time'])
  elif unit in ['months','month']:
    amount_c*=730.001
    unit_type_choice=random.choice(db['time'])
  elif unit in ['years','year','yrs','yr']:
    amount_c*=8760.00240024
    unit_type_choice=random.choice(db['time'])
  elif unit in ['decades','decade']:
    amount_c*=87600.0240024
    unit_type_choice=random.choice(db['time'])
  elif unit in ['centuries','century']:
    amount_c*=876000.240024
    unit_type_choice=random.choice(db['time'])
  elif unit in ['millenium','millenia']:
    amount_c=8760002.40024
    unit_type_choice=random.choice(db['time'])             
  else:
    await ctx.reply("Unit not supported. Try again with another unit")

  converted = unit_type_choice[0] * amount_c
  if not converted < 1:
    converted = int(converted)
  response = ""
  for i in unit_type_choice[1:]:
    if i == "a":
      i = amount
    elif i == 'u':
      i = unit
    elif i == 'c':
      i = converted
    response = response + str(i) + " "
  await ctx.reply(response)








  

keep_alive()
client.run(token)
