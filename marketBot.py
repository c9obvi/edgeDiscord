# market price bot needs its own bot + auth

import os
import requests
import discord
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


#connects to discord + guild then prints the status
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$btc'):
        quote = get_btc()
        await message.channel.send(quote)
    if message.content.startswith('$eth'):
        quote = get_eth()
        await message.channel.send(quote)
    if message.content.startswith('$ada'):
        quote = get_ada()
        await message.channel.send(quote)

def get_btc():
    response1 = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current BTC price is: $"+amount+" " +currency
    return(quote)

def get_eth():
    response1 = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current ETH price is: $"+amount+" " +currency
    return(quote)

def get_ada():
    response1 = requests.get('https://api.coinbase.com/v2/prices/ADA-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current ADA price is: $"+amount+" " +currency
    return(quote)



client.run(TOKEN)