# bot.py
import os

import discord
from discord.ext import commands

# Environment variables.
from dotenv import load_dotenv
load_dotenv()
CHANNEL = int(os.getenv('DISCORD_CHANNEL')) # ⚠ Must be an integer.
GUILD = os.getenv('DISCORD_GUILD')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    """Runs on startup and verifies everything is ok."""
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'\033[94m{bot.user} successfully connected to {guild.name}!\033[0m 😎')
    activity = discord.Activity(name='the world end ☣', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    channel = bot.get_channel(CHANNEL)
    try:
        print('\033[94mTrying to send message to channel...\033[0m 🤞')
        await channel.send('I\'m alive! 😀')
        print(f'\033[92mMessage sent to {channel.name}!\033[0m 😀')
    except:
        print(f'\033[91mInvalid channel id!\033[0m 😭')

@bot.command(name='test')
async def test(ctx):
    """Simple test command."""
    await ctx.send('It worked! 👌')

bot.run(TOKEN)
