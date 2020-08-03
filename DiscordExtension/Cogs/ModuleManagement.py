from discord.ext import commands
from DiscordExtension import bot_admin
import TwitterExtension


class ModuleManagement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='enable')
    async def _enable(self, ctx, module):
        await bot_admin(ctx)
        module = module.upper()
        if module == 'TWITTER':
            if (TwitterExtension.enable_Twitter()):
                await ctx.send(f'Twitter Module already running!')
            else:
                await ctx.send(f'Twitter Module started :white_check_mark:')
        else:
            await ctx.send(f'Enable What?')

    @commands.command(name='disable')
    async def _disable(self, ctx, module):
        await bot_admin(ctx)
        module = module.upper()
        if module == 'TWITTER':
            if TwitterExtension.disable_Twitter():
                await ctx.send(f'Disabled Twitter Extension!')
            else:
                await ctx.send(f'Twitter Module is already off!')


def setup(client):
    client.add_cog(ModuleManagement(client))
