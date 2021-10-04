import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive
from replit import db

client = discord.Client()
token = os.environ['token']

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game("y.help"))
  print("Bot online as {0.user}".format(client))


@client.event
async def on_message(message):
  msg = message.content.lower()
  if message.author.bot:
    return

  elif msg == "hello there":
    await message.reply("https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326")

  elif msg == 'f':
    await message.reply(random.choice(db['f_gifs']))

  elif msg in db["salam_i"]:
    await message.reply(random.choice(db["salam_o"]))

  elif msg == "y.fulldb":  
    for i in db.keys():
      await message.reply(f"{i}={db[i]}")

  elif msg == 'y.help':
    embedVar = discord.Embed(title="Yemmerald v2.2.1",description="Bot made by **@Zeus_1347#0765**. Please DM if the bot is offline or if you have any suggestions or feedback. \n ",color=0x26a43b)
    embedVar.set_thumbnail(url="https://i.imgur.com/3VJ5njN.jpg")
    embedVar.add_field(name="Useless Unit Convertor",value="Use `y.convert <amount> <unit>` \nConverts your lengths, weights and time to random useless units",inline=False)
    embedVar.add_field(name="Hello There",value="Replies with General Kenobi",inline=False)
    embedVar.add_field(name="Salam",value="Replies with Alaikum Assalam",inline=False)
    embedVar.add_field(name="F",value="Replies with F to pay  respects",inline=False)
    embedVar.set_footer(text="PS: If you are a Mod, change the **@Yemmerald** role's color to `#26a43b` for __*~aEsThEtIcS~*__.")
    await message.reply(embed=embedVar)

  elif msg.startswith("y.convert"):
    words = msg.split()
    for j in range(1,len(words) - 1):
      if words[j].isdigit() or ("." in words[j]) or (words[j]=='a') or (words[j]=='an'):
        if words[j]=='a' or words[j]=='an':
          amount=1
        try:
          amount = float(words[j])
        except ValueError:
          continue
        if amount == int(amount):
          amount = int(amount)
        unit = words[j + 1]
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
          await message.reply("Unit not supported. Try again with another unit")
          break
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

        await message.reply(response)
        break
    else:
        await message.reply("Wrong format. Use `y.convert <amount> <unit>`")

keep_alive()
client.run(token)
