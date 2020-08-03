from discord.ext import commands
from DiscordExtension import bot_admin
import TwitterExtension
pirobot_channel = 737420676973199423
#Gets current event loop to create a coroutine.

class Twitter(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.group(name='twitter', invoke_without_command='True')
    async def _twitter(self, ctx):
        if TwitterExtension.checkStatusTwitter():
            await ctx.channel.send(f'Twitter is On and is currently streaming: {TwitterExtension.myTwitterExtension.filter}, and Silencing is: {TwitterExtension.myTwitterExtension.silenced}')
        else:
            await ctx.channel.send(f'Twitter is Off!')
    @_twitter.command(name='stream')
    async def _twitter_stream(self, ctx, streamName):
        if not await bot_admin(ctx):
            return
        TwitterExtension.myTwitterExtension.createStream(streamName)
        await ctx.send(f'Created stream with filter \"{streamName}\"')
    @_twitter.command(name='stop')
    async def _twitter_disable(self, ctx):
        TwitterExtension.myTwitterExtension.stopStream()
        await ctx.send(f'Stream Stopped!')
    @_twitter.command(name='silent')
    async def _twitter_silence(self, ctx):
        TwitterExtension
def setup(client):
    client.add_cog(Twitter(client))






