import discord
from discord.ext import commands

client = discord.Client()

# GLOBAL VARIABLES
TOKEN = open("token.txt", "a").read()
