# test.py
from discord import Embed
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx):
        """Simple test command."""
        await ctx.send('It worked! 👌')
