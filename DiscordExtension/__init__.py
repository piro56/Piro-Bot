from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import asyncio
import random
import discord
import sqlite3

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix=',', case_insensitive=True)
client.remove_command('help')

###TODO: SAVE CHANNEL & GUILD OPTIONS SEPARATELY TO FILE.
###TODO: ADMIN SYSTEM
###TODO: CHANGE ANTIIMAGE TO HAVE OPTION FOR SECOND DURATION
### TODO: COOLODWN SYSTEM.

pirobot_channel = 737420676973199423
general_channel = 654323128369020955
_loop = asyncio.get_event_loop()


### IF GUILDID -> CHANNEL. MESSAGE CHANNEL ID == CHANNEL. DELETE.


# bot admin requirement
async def bot_admin(ctx):
    if (ctx.author.id != 393982976125435934):
        await ctx.send(f'Only bot admins can use this command!')
        return False
    else:
        return True


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Pain.", url="https://www.twitch.tv/sad"))
    print(f'Piro bot started!')
    for guild in client.guilds:
        print(f'Piro Bot running on: {guild.name} ID: {guild.id}')


# Send message operations other extensions can access (not in a cog for ease of use)
async def send_embed(channel, embed):
    channel = client.get_channel(channel)
    await channel.send(embed=embed)


async def send_Message(channel, text):
    channel = client.get_channel(channel)
    await channel.send(text)


def on_Tembed(emb):
    asyncio.run_coroutine_threadsafe(
        send_embed(pirobot_channel, emb), _loop
    )


def on_TMessage(msg):
    asyncio.run_coroutine_threadsafe(
        send_Message(pirobot_channel, msg), _loop
    )


# Handles command errors
@client.event
async def on_command_error(ctx, error):
    err = getattr(error, "original", error)
    if isinstance(err, commands.CommandNotFound):
        return


###LOAD/UNLOAD  COGS.
@client.command()
async def load(ctx, extension):
    if await bot_admin(ctx):
        client.load_extension(f'DiscordExtension.Cogs.{extension}')
        await ctx.send(f'Loaded {extension}')


@client.command()
async def unload(ctx, extension):
    if await bot_admin(ctx):
        client.unload_extension(f'DiscordExtension.Cogs.{extension}')
        await ctx.send(f'Unloaded {extension}')


@client.command()
async def reload(ctx, extension):
    if (await bot_admin(ctx)):
        client.unload_extension(f'DiscordExtension.Cogs.{extension}')
        client.load_extension(f'DiscordExtension.Cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')


async def antiImageChannel(ctx):
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT channel_id FROM anti_image WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if (ctx.channel.id == int(result[0]) and not ctx.author.guild_permissions.administrator):
        await ctx.delete(delay=15)
    cursor.close()
    db.close()


@client.event
async def on_message(ctx):
    global client
    if not ctx.author.bot:
        message_content = ctx.content.upper()
        if (message_content == 'BALLS'):
            reactions = ['<:balls_B:738913015839195158>', '<:balls_A:738913015994515487>',
                         '<:balls_L1:738913016221007972>', '<:balls_L2:738913015822548993>',
                         '<:balls_S:738913016103436318>']
            for i in reactions:
                await ctx.add_reaction(i)
            # Deletes images in general channel after 10seconds.

        if len(ctx.attachments) > 0 or "HTTP" in message_content: await antiImageChannel(ctx)
    await client.process_commands(ctx)


# Runs/Starts PiroBot.
def PiroBot_Run():
    # Load COGS.
    for filename in os.listdir('./DiscordExtension/Cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'DiscordExtension.Cogs.{filename[:-3]}')
            print(f'Loaded Cog: {filename[:-3]}')
    print("Cogs loaded!")
    client.run(TOKEN)
