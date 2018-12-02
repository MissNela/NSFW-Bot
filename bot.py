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

        **:ping**
        :ping_pong: Pong!
        """,
        color = 0x800000
        

)
    await client.say(embed=embed)
  

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content=':ping_pong: Pong! Actual ping: {}ms'.format(int(ms)))
    
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def warn(ctx, userName: discord.User, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='logs')
    
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
    await client.send_message(channel, embed=embed)
 
@client.command(pass_context=True)
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='logs-1')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context=True)
async def suggest(ctx, *, msg=None):


    channel = discord.utils.get(client.get_all_channels(), name='logs-1')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def announce(ctx, userName: discord.User, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='announcements')
    
    embed = discord.Embed(
        
        title = "Succesful!",
        description = """ __**Announce has been successfully made!**__"""
        
)
    await client.delete_message(ctx.message)
    await client.send_message(userName, embed=embed)
 

    
        
        
    await client.send_message(channel, """**Nové Oznámení!**
    __Ozbámení:__
    
    {0}
    
    __Oznámeno od:__
    ``{1}``""".format(message, ctx.message.author))
    
@client.command(pass_context = True)
     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Jméno", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Nejvišší role", value=user.top_role)
    embed.add_field(name="Připojil", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text = "Vytvořila Nela | Bot verze: 0.3")
    await client.say(embed=embed)


client.run(os.getenv("BOT_TOKEN"))
