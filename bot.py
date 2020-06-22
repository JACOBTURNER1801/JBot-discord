import discord
from discord.ext import commands
import Python.JBot.quotes
from Python.JBot.quotes import Quotes
import asyncio

client = discord.Client()

# GLOBAL VARIABLES
TOKEN = open("C:/Users/FiercePC/Desktop/projects/token.txt", "a").read()
SERVER_ID = 394868206545797130

commands_usable = """```py
def commands():
    return {
        jbot.commands(): 'returns the commands'
        jbot.hello(): 'says hello'
        jbot.logout(): 'disconnects the bot'
        jbot.add_quote() "quote": 'adds quote into quotes list'
        jbot.display_quotes(): 'displays the quotes'
        jbot.get_quote(): 'randomly gets a quote from the list'
        jbot.bug_report(): 'tells you how to report a bug'
    }
```"""

list_quotes = [
    "Hello there from the bot, this is an example of an inspirational message",
    "To dare is to do - Tottenham Hotspur FC who continuesly bottle things lmao"
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

    elif "jbot.logout()" == message.content.lower() and str(message.author) != "Jacob#3584":
        await message.channel.send("Only Jacob can close me down!")

    elif "jbot.logout()" == message.content.lower() and str(message.author) == "Jacob#3584":
        await message.channel.send("logging out")
        await client.close()

    elif "jbot.display_quotes()" == message.content.lower():
        output = Quotes_obj.print_quotes()
        await message.channel.send("here are the quotes: ")
        await message.channel.send(str(output))

    elif "jbot.add_quote()" == message.content.lower():
        # the [15:] is because of the jbot.add_quote() command being 15
        # characters and we don't want to add that to the quotes list
        await message.channel.send(f"adding {message.content[15:]} to the quotes list")
        Quotes_obj.modify_quotes(str(message.content[15:]))
        await message.channel.send("should be done, now displaying the quotes again")
        await message.channel.send(str(Quotes_obj.print_quotes()))

    elif "jbot.get_quote()" == message.content.lower():
        # get a quote
        randomly_generated_quote: str = Quotes.get_quote(list_quotes)
        # send the quote @'ing the user
        message.channel.send(
            f" '{randomly_generated_quote}' @{message.author.name} ")

    elif "jbot.bug_report()" == message.content.lower():
        link = "https://github.com/JACOBTURNER1801/JBot-discord/issues"
        await message.channel.send(f"In order to report a bug you need to follow {link}")


client.run(TOKEN)
