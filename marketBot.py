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
    if message.content.startswith('$xmr'):
        quote = get_xmr()
        await message.channel.send(quote)
    if message.content.startswith('$ltc'):
        quote = get_ltc()
        await message.channel.send(quote)        
    if message.content.startswith('$sol'):
        quote = get_sol()
        await message.channel.send(quote)
    if message.content.startswith('$doge'):
        quote = get_doge()
        await message.channel.send(quote)


def get_btc():
    response1 = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Bitcoin (BTC) price is:  $"+amount+" " +currency
    return(quote)

def get_eth():
    response1 = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Ethereum (ETH) price is:  $"+amount+" " +currency
    return(quote)

def get_ada():
    response1 = requests.get('https://api.coinbase.com/v2/prices/ADA-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Cardano (ADA) price is:  $"+amount+" " +currency
    return(quote)

def get_xmr():
    response1 = requests.get('https://api.coinbase.com/v2/prices/XMR-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Monero (XMR) price is:  $"+amount+" " +currency
    return(quote)

def get_ltc():
    response1 = requests.get('https://api.coinbase.com/v2/prices/LTC-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Litecoin (LTC) price is:  $"+amount+" " +currency
    return(quote)

def get_sol():
    response1 = requests.get('https://api.coinbase.com/v2/prices/SOL-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Solana (SOL) price is:  $"+amount+" " +currency
    return(quote)

def get_doge():
    response1 = requests.get('https://api.coinbase.com/v2/prices/DOGE-USD/buy')
    json_data = json.loads(response1.text)
    prequote = json_data['data']
    currency = prequote['currency']
    amount = prequote['amount']
    quote = "current Doge (DOGE) price is:  $"+amount+" " +currency
    return(quote)

    

client.run(TOKEN)