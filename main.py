import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive
from replit import db

'''lst=db["key"]["optional"]
list_add=[]
for i in list_add:
  lst.append(i)'''

client = discord.Client()
token = os.environ['token']


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("y.help"))
  print("Bot online as {0.user}".format(client))


@client.event
async def on_message(message):
    msg=message.content.lower()
    if message.author.bot:
        return

    elif msg == "y.ping":
        await message.reply("Pong")

    elif msg == "hello there":
        await message.reply("https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326")

    elif msg == 'f':
        await message.reply(random.choice(db['f_gifs']))

    elif msg in db["salam_i"]:
        await message.reply(random.choice(db["salam_o"]))
    
    elif msg == "mukund.db":
      for i in db.keys():
        await message.reply(f"{i}={db[i]}")
    
    elif msg=='y.help':
        embedVar = discord.Embed(title="Yemmerald Features", description="Bot made by @Zeus_1347#0765. DM him if the bot is offline or if you have any suggestions or feedback. \n PS: If you are a Mod, change the @Yemmerald role's color to #00FF00 for *aesthetics*.", color=0x00ff00)
        embedVar.add_field(name="Useless Unit Convertor", value="Compares your numbers and values to useless random objects\n(Still working on it. Will be adding more to it. Right now only length values will be compared)", inline=False)
        embedVar.add_field(name="Hello There", value="Replies with General Kenobi", inline=False)
        embedVar.add_field(name="F", value="Replies with F to pay  respects", inline=False)
        embedVar.add_field(name="Salam", value="Replies with Alaikum Assalam", inline=False)
        await message.channel.send(embed=embedVar)

        


    else:
      words = msg.split()
      for j in range(len(words)-1):
          if words[j].isdigit() or ("." in words[j]):
              unit=words[j+ 1]
              amount=float(words[j])
              if amount==int(amount):
                amount=int(amount)  
              amount_c=amount
              if unit in ["m","metre","meter","meters","metres"]:
                  unit_type_choice=random.choice(db["units_dict"]["length"])
              elif unit in ["cm",'centimeter','centimetre','centimeters','centimetres']:
                  amount_c/=100
                  unit_type_choice=random.choice(db["units_dict"]["length"])
              elif unit in ["in",'inches','inch']:
                  amount_c/=39.37
                  unit_type_choice=random.choice(db["units_dict"]["length"])
              elif unit in ['feet','foot','ft']:
                  amount_c/=3.281
                  unit_type_choice=random.choice(db["units_dict"]["length"])
              else:
                continue
              
              converted=int(unit_type_choice[0] * amount_c)
              response=""
              for i in unit_type_choice[1:]:
                if i=="a":
                  i=amount
                elif i=='u':
                  i=unit
                elif i=='c':
                  i=converted          
                response=response+str(i)+" "
              
              await message.reply(response)

                


keep_alive()
client.run(token)
