import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
token = os.environ['token']

f_gifs = [
    "https://tenor.com/view/f-press-f-shaking-gif-14143393",
    "https://tenor.com/view/f-letter-f-burts-rip-pipec-f-throw-gif-17537831",
    "https://tenor.com/view/salute-letter-f-respect-crying-gif-17677784",
    "https://tenor.com/view/press-f-pay-respect-keyboard-gif-12855017",
    "https://tenor.com/view/pay-respects-press-f-call-of-duty-respect-press-x-gif-22309724","https://tenor.com/view/efemann-efe-ff-f-in-the-chat-f-in-chat-gif-17919585","https://tenor.com/view/press-f-pay-respect-coffin-burial-gif-12855021"
]
salam_i=["salamalaikum","salam","assalam alaikum","assalam","assalamualaikum","assalamualikum","salamalekum","salamualaikum","salamualekum","assalamalekum"]
salam_o=["Walaikum Salam Kenobi Al Habibi","Walaikum Assalam Al Obi Wan Al Kenobi"]


@client.event
async def on_ready():
    print("Bot online as {0.user}".format(client))


@client.event
async def on_message(msg):
    if msg.author.bot: 
        return 

    if msg.content.lower()=="y.ping":
      await msg.channel.send("Pong")
      
    if msg.content.lower() == "hello there":
        await msg.channel.send("https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326")

    if msg.content.lower() == 'f':
        await msg.channel.send(random.choice(f_gifs))

    if msg.content.lower() in salam_i:
        await msg.channel.send(random.choice(salam_o))



keep_alive()
client.run(token)
