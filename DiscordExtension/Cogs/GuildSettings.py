import discord
from discord.ext import commands
import sqlite3


class GuildSettings(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Set the antiImage channel for the server.
    @commands.command(pass_context=True, aliases=['anti-image', 'antiimage', 'imageblacklist', 'noimage'])
    async def _antiImage(self, ctx, channel: discord.TextChannel):
        if (ctx.message.author.guild_permissions.administrator):
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM anti_image WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO anti_image(guild_id, channel_id) VALUES(?,?)")
                val = (ctx.guild.id, channel.id)
                await ctx.send(f"Anti-Image Channel has been set to {channel.mention}")
            elif result is not None:
                sql = ("UPDATE anti_image SET channel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f"Anti-Image Channel has been updated to {channel.mention}")
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()
        else:
            await ctx.send("Only server administrators can use this command!")


def setup(client):
    client.add_cog(GuildSettings(client))
