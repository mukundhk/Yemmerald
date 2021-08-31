import discord
import os
import random
from keep_alive import keep_alive


#units_file=open("units.dat","rb")
#units_fh=pickle.load(units_file)
amount=0
unit=""
converted=0
units_dict={"length":[[39.37007874,amount,unit,"is the length of approximately",converted,"'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise."], [2.021,amount,unit,"is the same as", converted,"'Logitech Wireless Keyboard K350s' laid widthwise by each other."]], "weight":[[]]}




client = discord.Client()
token = os.environ['token']

f_gifs = [
    "https://tenor.com/view/f-press-f-shaking-gif-14143393",
    "https://tenor.com/view/f-letter-f-burts-rip-pipec-f-throw-gif-17537831",
    "https://tenor.com/view/salute-letter-f-respect-crying-gif-17677784",
    "https://tenor.com/view/press-f-pay-respect-keyboard-gif-12855017",
    "https://tenor.com/view/pay-respects-press-f-call-of-duty-respect-press-x-gif-22309724",
    "https://tenor.com/view/efemann-efe-ff-f-in-the-chat-f-in-chat-gif-17919585",
    "https://tenor.com/view/press-f-pay-respect-coffin-burial-gif-12855021"
]
salam_i = [
    "salamalaikum", "salam", "assalam alaikum", "assalam", "assalamualaikum",
    "assalamualikum", "salamalekum", "salamualaikum", "salamualekum",
    "assalamalekum"
]
salam_o = [
    "Walaikum Salam Kenobi Al Habibi", "Walaikum Assalam Al Obi Wan Al Kenobi"
]

def UUC(amount,unit,converted,lst):
  response=""
  for i in lst:
    response=response+str(i)+" "
  return response



@client.event
async def on_ready():
    print("Bot online as {0.user}".format(client))


@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    if msg.content.lower() == "y.ping":
        await msg.channel.send("Pong")

    if msg.content.lower() == "hello there":
        await msg.channel.send(
            "https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326"
        )

    if msg.content.lower() == 'f':
        await msg.channel.send(random.choice(f_gifs))

    if msg.content.lower() in salam_i:
        await msg.channel.send(random.choice(salam_o))

    
    words = msg.content.lower().split()
    for j in range(len(words)):
        if words[j].isdigit():
            unit=words[j+ 1]
            if unit=="m" or "metre" or "meter" or "meters" or "metres":
                amount=words[j]
                length_choice=random.choice(units_dict["length"])
                converted=length_choice[0] * float(amount)
                await msg.channel.send(UUC(amount,unit,converted,length_choice))
    
    
keep_alive()
client.run(token)
