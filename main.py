import os
import discord
from discord.ext import commands
import logging

##setting up logging 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='birdy.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

#load extension
bot.load_extension('voice')



my_secret = os.environ['TOKEN']
bot.run(my_secret)
