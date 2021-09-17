import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive
from replit import db

lst1 = [
    [2070000, 'a', 'u', "would need about", 'c', "human hairs to lift."],
    [
        3.359424866, 'a', 'u', "is about the weight of", 'c',
        "'Velener Mini Potted Plastic Fake Green Plants'."
    ],
    [
        2.873563218, 'a', 'u', "is about the weight of", 'c',
        "Minecraft: Redstone Handbook: An Official Mojang Book (Hardcover)."
    ],
    [
        1.218023533, 'a', 'u', "is about the same weight as", 'c',
        "'Double sided 60 inch Mermaker Pepperoni Pizza Blankets'."
    ],
    [
        8.86280467, 'a', 'u', "is about the weight of", 'c',
        "'6pack TWOHANDS Assorted Pastel Color Highlighters'."
    ],
    [
        19471.42, 'a', 'u', "of vegan poop being burned provides about", 'c',
        "BTU(British Thermal Unit)."
    ],
    [
        361.8730093, 'a', 'u', "is about the weight of $", 'c',
        "worth of Premium Glass Nail Files."
    ],
    [
        24.32686944, 'a', 'u', "is the weight of about", 'c',
        "'Kingston 120GB Q500 SATA3 2.5 Solid State Drives'."
    ],
    [
        1.851851852, 'a', 'u',
        "of double AA batteries could start a medium sized car about", 'c',
        "times."
    ]
]
lst2=[[39.37007874, 'a', 'u', 'is the length of approximately', 'c', "'Wooden Rice Paddle Versatile Serving Spoons' laid lengthwise."],
[2.021, 'a', 'u', 'is about the same as', 'c', "'Logitech Wireless Keyboard K350s' laid widthwise by each other."]
, [9.842519685, 'a', 'u', 'is about the length of', 'c', "'Bug Bite Thing Suction Tool - Poison Remover For Bug Bites's stacked on top of each other."]
, [4.921259843, 'a', 'u', 'is about the length of', 'c', "'EuroGraphics Knittin Kittens 500-Piece Puzzle's next to each other."]
, [2.04095794402, 'a', 'u', 'is the length of about', 'c', "'Ford F-150 Custom Fit Front FloorLiners' lined up next to each other."]
, [9.803921569, 'a', 'u', 'is the length of about', 'c', "'Standard Diatonic Key of C, Blues Silver grey Harmonicas' lined up next to each other."]
, [3.402772579, 'a', 'u', 'is about', 'c', 'RTX 3090 graphics cards lined up.']
, [0.4921259843, 'a', 'u', 'is about the same as', 'c', 'times the average door frame height']
, [1814.8820326, 'a', 'u', 'is about the same as', 'c', 'sperm cells lined up head to tail']
, [0.5734063318, 'a', 'u', 'is the height of', 'c', "'Samsung Side by Side; Fingerprint Resistant Stainless Steel Refrigerators' stacked on top of each other."]
, [0.00490677134, 'a', 'u', 'is about', 'c', "times the Guinness World Record for 'Longest Hot Dog'"]
, [4.525296407, 'a', 'u', 'is the length of like', 'c', "'Zulay Premium Quality Metal Lemon Squeezers' laid next to each other."],
[1.789549034, 'a', 'u', 'is about the same distance as', 'c', "'Replica Bilbo's from The Lord of the Rings Sting Swords'"]]
db['length']=lst2
db['weight'] = lst1

client = discord.Client()
token = os.environ['token']


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("y.help"))
    print("Bot online as {0.user}".format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author.bot:
        return

    elif "yemmeraald" in msg:
        await message.reply("Yes?\nUse y.help if you need it.")

    elif msg == "y.ping":
        await message.reply("Pong")

    elif msg == "hello there":
        await message.reply(
            "https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326"
        )

    elif msg == 'f':
        await message.reply(random.choice(db['f_gifs']))

    elif msg in db["salam_i"]:
        await message.reply(random.choice(db["salam_o"]))

    elif msg == "y.fulldb":
        for i in db.keys():
            await message.reply(f"{i}={db[i]}")

    elif msg == 'y.help':
        embedVar = discord.Embed(
            title="Yemmerald Features",
            description=
            "Bot made by **@Zeus_1347#0765**. Please DM if the bot is offline or if you have any suggestions or feedback. \n PS: If you are a Mod, change the **@Yemmerald** role's color to `#26a43b` for __*~aEsThEtIcS~*__.",
            color=0x26a43b)
        embedVar.add_field(
            name="Useless Unit Convertor",
            value=
            "Compares your numbers and values to useless random objects\n(Still working on it. Will be adding more to it. Right now only length values will be compared)",
            inline=False)
        embedVar.add_field(name="Hello There",
                           value="Replies with General Kenobi",
                           inline=False)
        embedVar.add_field(name="F",
                           value="Replies with F to pay  respects",
                           inline=False)
        embedVar.add_field(name="Salam",
                           value="Replies with Alaikum Assalam",
                           inline=False)
        await message.reply(embed=embedVar)

    else:
        words = msg.split()
        for j in range(len(words) - 1):
            if words[j].isdigit() or ("." in words[j]):
                try:
                    amount = float(words[j])
                except ValueError:
                    continue
                if amount == int(amount):
                    amount = int(amount)
                unit = words[j + 1]
                amount_c = amount
                if unit in ["m", "metre", "meter", "meters", "metres"]:
                    unit_type_choice = random.choice(
                        db["units_dict"]["length"])
                elif unit in [
                        "cm", 'centimeter', 'centimetre', 'centimeters',
                        'centimetres'
                ]:
                    amount_c /= 100
                    unit_type_choice = random.choice(
                        db["units_dict"]["length"])
                elif unit in ["in", 'inches', 'inch']:
                    amount_c /= 39.37
                    unit_type_choice = random.choice(
                        db["units_dict"]["length"])
                elif unit in ['feet', 'foot', 'ft']:
                    amount_c /= 3.281
                    unit_type_choice = random.choice(
                        db["units_dict"]["length"])
                else:
                    continue

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


keep_alive()
client.run(token)
