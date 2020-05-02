# advise.py
from discord import Embed
from discord.ext import commands

import requests


class Advise(commands.Cog):
    endpoint = 'https://boredapi.com/api/'
    kinds = {
        'busywork': '🔨',
        'cooking': '🔪',
        'education': '📚',
        'charity': '💕',
        'diy': '💪',
        'music': '🎼',
        'recreational': '🚲',
        'relaxation': '🛌',
        'social': '🏙'
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='advise')
    async def advise(self, ctx):
        """Gives a random advise."""
        response = requests.get(url=f'{self.endpoint}activity?participants=1')

        if response.ok:
            data = response.json()

            activity = data['activity']
            kind = self.kinds[data['type']]
            link = data['link']

            embed = Embed(title='Random advise')
            embed.add_field(name='Activity', value=f'{activity} {kind}')
            if len(link) > 0:
                embed.add_field(name='Link', value=link)

            await ctx.send(embed=embed)

        else:
            await ctx.send('No reponse from the API 😫')
