import discord
import os
import random
from keep_alive import keep_alive
from replit import db

'''lst=db["key"]["optional"]
list_add=[]
for i in list_add:
  lst.append(i)'''

client = discord.Client()
token = os.environ['token']


def UUC(amount,unit,lst,amount_c):
    converted=lst[0] * amount_c
    response=""
    for i in lst[1:]:
      if i=="a":
        i=amount
      elif i=='u':
        i=unit
      elif i=='c':
        i=converted          
      response=response+str(i)+" "
    return response



@client.event
async def on_ready():
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


    else:
      words = msg.split()
      for j in range(len(words)-1):
          if words[j].isdigit() or ("." in words[j]):
              unit=words[j+ 1]
              try:
                amount=float(words[j])
              except:
                continue
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

              await message.reply(UUC(amount,unit,unit_type_choice,amount_c))

                


keep_alive()
client.run(token)
