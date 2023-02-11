import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks
from nextcord.utils import get
import os, sys
import apikeys, utils

class General(commands.Cog):
    serverIdList = apikeys.serverIdList()

    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(name = "help", description = "Help for using the bot", guild_ids=serverIdList)
    async def help(self, interaction: Interaction):
        help_message = '''Thanks for using **AkagiBot**. 
The bot was written by Fenway Powers in 2023, based off of his work re-writing the Computer Interest Floor's Discord Bot.
'''
        await interaction.response.send_message(help_message)

def setup(client):
    client.add_cog(General(client))