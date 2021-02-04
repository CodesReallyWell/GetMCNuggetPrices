# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tmp = message.content
    msgMinus = tmp.replace('?', '')
    if (tmp.find('?') != -1) and (tmp.find('Liam') == -1):
        response = " " + msgMinus
        await message.channel.send(response)
    elif (tmp.find('Liam') != -1) or (tmp.find('liam') != -1):
        response = "Love you Liam <3"
        await message.channel.send(response)
        
client.run(TOKEN)
