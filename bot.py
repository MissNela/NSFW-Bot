import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = ':')

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: :"))
    print("The bot is online and connected with Discord!") 

@client.command()
async def help():
    embed = discord.Embed(
        title = "Help Commands!",
        description = """
        **:help**
        Ukáže ti tuto zpravu.
        
        **:verify**
        Pokud bys ses chtel nekdy verifikovat ;).

        **:modmail**
        Napiš nám mail o problému!!
.      
        **:warn @clovek duvod**
        Varuje cloveka
        
        **:suggest**
        Chceš něco přidat na server?
        
        **:announce**
        Ohlaš něco! \manage_roles pravomoc potřeba!/
        
        **:userinfo**
        Gets info about user!
        
        **:cube**
        Chooses randome number between 1-6.
        
        **:ping**
        :ping_pong: Pong!
        """,
        color = 0x800000
        

)
    await client.say(embed=embed)
  
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def warn(ctx, userName: discord.User, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='🎀logs-1🎀')
    
    embed = discord.Embed(color = 0xB22222,
        
        title = "Varování",
        description = """ __**You has been warned!**__
        Člověk varován:
        ``{0}``
        Moderator:
        ``{1}`` 
        Dúvod:
        ``{2}``""".format(userName, ctx.message.author, message)
        
)
    await client.send_message(userName, embed=embed)
 
client.run(os.getenv("BOT_TOKEN"))
