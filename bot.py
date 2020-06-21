import discord
from discord.ext import commands
import re
import time
import asyncio
import random
import Python.JBot.quotes
from Python.JBot.quotes import Quotes

client = discord.Client()

# GLOBAL VARIABLES
TOKEN = open("token.txt", "a").read()
SERVER_ID = 394868206545797130

commands_usable = """```py
def commands():
    return {
        jbot.hello(): 'says hello'
        jbot.logout(): 'disconnects the bot'
        jbot.commands(): 'returns the commands'
        jbot.add_quote() <quote>: 'adds quote into quotes list'
        jbot.display_quotes(): 'displays the quotes'
    }
```"""

list_quotes = [
    "Hello there from the bot, this is an example of an inspirational message",
]

# create Quotes object
Quotes_obj = Quotes(list_quotes)

# Bot logging in


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(status=discord.Status.online)

# Message received from the server


@client.event
async def on_message(message):
    print(f"{message.channel}, {message.author}, {message.author.name}, {message.content}")
    guild = client.get_guild(SERVER_ID)
    author_roles = message.author.roles

    # go through commands and perform action based on the command

    if "jbot.commands()" == message.content.lower():
        await message.channel.send(commands_usable)

    elif "jbot.hello()" == message.content.lower():
        await message.channel.send(f"hello there {message.author.name}")

    elif "jbot.logout()" == message.content.lower():
        await message.channel.send("Logging out")
        await client.logout()

    elif "jbot.display_quotes()" == message.content.lower():
        output = Quotes_obj.print_quotes()
        await message.channel.send("here are the quotes: ")
        await message.channel.send(str(output))

    elif "jbot.add_quote()" == message.content.lower():
        # the [14:] is because of the jbot.add_quote() command being 15
        # characters and we don't want to add that to the quotes list
        await message.channel.send(f"adding {message.content[15:]} to the quotes list")
        Quotes_obj.modify_quotes(str(message.content[15:]))
        await message.channel.send("should be done, now displaying the quotes again")
        await message.channel.send(str(Quotes_obj.print_quotes()))
