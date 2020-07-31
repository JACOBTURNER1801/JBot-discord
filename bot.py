import discord
from discord.ext import commands
# doesn't find the file for some reason (it's literally in the same folder)
# import Python.JBot.quotes
# from Python.JBot.quotes import Quotes
import asyncio
from google import google

client = discord.Client()

# GLOBAL VARIABLES
TOKEN = open("C:/Users/FiercePC/Desktop/projects/token.txt", "a").read()
SERVER_ID = 394868206545797130
# for the search feature
NUM_PAGES = 1  # searches 1 page


commands_usable = """```py
def commands():
    return {
        jbot.commands(): 'returns the commands'
        jbot.hello(): 'says hello'
        jbot.logout(): 'disconnects the bot'
        jbot.bug_report(): 'tells you how to report a bug'
        jbot.search(): 'googles what you put after'
    }
    DEPRECATED:
        jbot.add_quote() "quote": 'adds quote into quotes list'
        jbot.display_quotes(): 'displays the quotes'
        jbot.get_quote(): 'randomly gets a quote from the list'
        
```"""

'''
list_quotes = [
    "Hello there from the bot, this is an example of an inspirational message",
    "To dare is to do - Tottenham Hotspur FC who continuesly bottle things lmao"
]

# create Quotes object
Quotes_obj = Quotes(list_quotes)
'''
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

    elif "jbot.logout()" == message.content.lower() and str(message.author) != "Jacob#3584":
        await message.channel.send("Only Jacob can close me down!")

    elif "jbot.logout()" == message.content.lower() and str(message.author) == "Jacob#3584":
        await message.channel.send("logging out")
        await client.close()
    # see quotes conditional statements in a separate text file

    elif "jbot.bug_report()" == message.content.lower():
        link = "https://github.com/JACOBTURNER1801/JBot-discord/issues"
        await message.channel.send(f"In order to report a bug you need to follow {link}")
    elif "jbot.search()" == message.content.lower():
        # search for the phrase after the 13th character
        phrase: str = message.content[12:]
        search_result = google.search(phrase, NUM_PAGES)
        search_link = search_result.link
        search_name = search_result.name
        await message.channel.send(f"Name : {search_name}, Link: {search_link}")


client.run(TOKEN)
