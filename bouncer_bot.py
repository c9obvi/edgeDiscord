# Bouncer and head security at Edge Discord 

import os
import requests
import discord
from dotenv import load_dotenv
import json
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#define flaggable words dictionary?
flag_words = ["private keys", "private key", "Private Keys", "Private keys", "PRIVATE KEYS", "private Keys"]
#response to flagged private key talk -- add @TheUserinQuestion + keep tabs on users
flag_response = [
    "Please refrain from sharing or rquesting any private keys, violators will be banned!",
    "Reminder, asking for or revealing private keys will get you banned!",
    "Asking for or giving private keys is a bannable offense on this server!",
    "Disclosing or requesting private keys on this server is bannable and your account will be marked!"
]

#user unique ID to keep tabs before banning OR for promoting -- user IDs will be key to tracking
# our users and their behavior (on our server) int

#connects to discord + guild then prints the status
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm('Welcome to the channel, please keep it clean and scam free in here or I will have to through you out')
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#had to variablize message.content to work with itteration (looping/sifting)
    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Welcome to Edge Community Discord! Keep it friendly in here will ya. Or I may have to throw you out.')

    if msg.startswith('$help'):
        await message.channel.send('Sure thing! I will get you the link to support ASAP! \n\n https://support.edge.app')

#Monitor users messages for filtering
    if any(word in msg for word in flag_words):
        await message.channel.send(random.choice(flag_response))
    





client.run(TOKEN)