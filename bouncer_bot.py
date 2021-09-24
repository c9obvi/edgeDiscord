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

#pre-flags
pre_flags = [
    "send me", "dm me", "DM me", "message me", "whats you",
    "What is your", "what's your", "What is your", "What's your",
#cross check words below:
    "private keys", "private key", 
    "Private Keys", "Private keys", "PRIVATE KEYS", "private Keys",
    "phrase", "Mnemonic Phrase", "mnemonic phrase", "nemonic Phrase"
]

flag_checker = False

#define flaggable words dictionary?
flag_words = ["private keys", "private key", 
"Private Keys", "Private keys", "PRIVATE KEYS", "private Keys",
 "phrase", "Mnemonic Phrase", "mnemonic phrase", "nemonic Phrase"
]
#response to flagged private key talk -- add @TheUserinQuestion + keep tabs on users
flag_response = [
    "Please refrain from sharing or rquesting any private keys, violators will be banned!",
    "Reminder, asking for or revealing private keys will get you banned!",
    "Asking for or giving private keys is a bannable offense on this server!",
    "Disclosing or requesting private keys on this server is bannable and your account will be marked!"
]

# user unique ID to keep tabs before banning OR for promoting -- user IDs will be key to tracking
# IF message.content == "flaged" THEN get USERID - add tally to strikes DB on AirTable.

# our users and their behavior (on our server) int

# connects to discord + guild then prints the status
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
#  prevents the bot's own text from triggering itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return

#had to variablize message.content to work with itteration (looping/sifting)
    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Welcome to Edge Community Discord! Keep it friendly in here will ya. Or I may have to throw you out.')

    if msg.startswith('$help'):
        await message.channel.send('Sure thing! Here is the link to support!! \n\n https://support.edge.app')
    
    if msg.startswith('$app'):
        await message.channel.send('Sure thing! Here is the link to download our app!! \n\n https://edge.app')


# Monitor users messages for filtering
    #this one is attempting to combine words to meet both conditions (testing)
    if any(word in msg for word in pre_flags):
        flagCheck(msg, flag_words)
        if flag_checker(True):
            await message.channel.send(random.choice(flag_response))
    

#  if word in pre flag = True
#  then we check if user "msg" contains "flag_words" 
#  if True then bot sends a random selection from "flag_response"

def flagCheck(msg, flag_words): 
  
    set1 = set(flag_words) 
    set2 = set(msg) 
    if set1.intersection(set2): 
        flag_checker = true
        return flag_checker
    else: 
        return False



#if true  await message.channel.send(random.choice(flag_response))

#def preFlagTrigger():


    #this is current working and live catch for words related to keys
    #if any(word in msg for word in flag_words):
    #    await message.channel.send(random.choice(flag_response))
    
    



client.run(TOKEN)