# bot.py
import os
from getNugPrices import getNugPrices

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.content == '!nuggs'):
        nugPrices = getNugPrices()
        await message.channel.send(nugPrices)


client.run(TOKEN)
