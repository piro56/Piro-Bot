from discord.ext import commands
from discord import Embed
from discord import Color
from discord.utils import get
from DiscordExtension import bot_admin
from datetime import date
from discord import User
import asyncio
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.simpLevels = self.initSimpLevels()
        self.susLevels = self.initSusLevels()
        self.sadLevels = self.initSadLevels()
    def initSimpLevels(self):
        f = open("./DiscordExtension/Cogs/simpRate.txt", "r", encoding='utf-8', errors="backslashreplace")
        lines = f.readlines()
        simpLevelArr = []
        for i in range(9):
            simpLvl = ""
            for j in range((i - 1) * 5, (i * 5)):
                simpLvl += lines[j]
            simpLevelArr.append(simpLvl)
        return simpLevelArr
    def initSadLevels(self):
        f = open("./DiscordExtension/Cogs/sadRate.txt", "r", encoding='utf-8', errors="backslashreplace")
        lines = f.readlines()
        sadLevelArr = []
        for i in range(11):
            sadLvl = ""
            for j in range((i - 1) * 5, (i * 5)):
                sadLvl += lines[j]
            sadLevelArr.append(sadLvl)
        return sadLevelArr
    def initSusLevels(self):
        f = open("./DiscordExtension/Cogs/susRate.txt", "r", encoding='utf-8', errors="backslashreplace")
        lines = f.readlines()
        susLevelArr = []
        for i in range(11):
            susLvl = ""
            for j in range((i - 1) * 5, (i * 5)):
                susLvl += lines[j]
            susLevelArr.append(susLvl)
        return susLevelArr

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong :ping_pong:! {round(self.client.latency * 1000)}ms')

    @commands.command(name='testembed')
    async def embed(self, ctx):
        if await bot_admin(ctx):
            embed = Embed(
                title='User1',
                colour=Color.blue(),
                description='Cool man, I didn\'t know that.'
            )
            await ctx.send(embed=embed)
    @commands.command(name='piroball')
    async def _piroball(self, ctx):

        questions = [
            'Are you racist?', 'Would you rather join ROTC or Band', 'Where do you see yourself in 5 years?',
            'Are you able to comprehend emotions well?', 'Do you shower in the morning or night? Also is there a window in your bathroom?',
            'Do you think robots like me have emotions?', 'Do you think I chose to be a robot?', 'Balls?', 'What is your meaning of life?',
            'If you had the life of the person above your message, how do you think it would go?', 'Are you happy {user}?', 'Thanks for letting me ask you questions {user} <3',
            'Will my pain ever end?', 'I hope we are here for a reason...Do you think I have a reason?', 'What is your favorite musical artist?',
            'Do you have a good relationship with your family?', 'Poptarts or Hot Pockets?', 'How are you, {user}?', 'Hey {user}, I hope you\'re doing good today! Are you doing well?',
            'What is your favorite color?', 'Would you kiss an alien?', 'Love is a emotion brought upon by chemicals in our bodies. Does love control you?', 'What is your interpretation of death?',
            'Bootimus Maximus, or Chest Pillow?', 'Discord?', 'Do you want to be my friend {user}?', 'Apple Juice or Orange Juice?', 'Get 100million dollars but die in 10 years or get 1million and live to 100?',
            'Do you like pineapple on pizza?', 'Where do you store your money?', 'Give me your best pickup line ;)', 'Do you think god is disappointed in his creation?'
        ]
        randChoice = random.randint(0, len(questions)-1)
        await ctx.send(questions[randChoice].replace('{user}', ctx.author.name))

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):

        why_responses = [
            'Because life.', 'I think it\'s because of the duality of the situation at hand.', 'No one knows...',
            'There is no explanation for it.', 'I don\'t know man, why do cheez-itz taste terrible after a while? It\'s just how it is.',
            'Bro...why not?'
        ]

        when_responses = [
            'Tomorrow', 'It\'s already happened.', 'Never.',
            'In a year', 'In 5 years.', 'When you learn to stop asking a bot for answers to all of your questions',
            'Maybe in a few days.', 'A week or two.', 'Never ever ever ever ever', 'I do not know, nor do I care.'
        ]
        how_responses = [
            'With a great deal of focus...', 'Don\'t give up, thats about it.', 'Try asking your dad.', 'Don\'t ask me, I\'m a bot.',
            'Try using a lot of lotion.', 'Just get a car and drive off into the sunset.', 'Use a toothbrush. You know what to do with the rest ;)',
        ]
        yes_responses = [
            'Yes', 'Of course!',
            'Most likely',
            'Certainly', 'bruh...yeah', 'balls...yes', 'Duhh', 'Obviously, yeah.',
            'Hold on let me ask science 🔍 \nSources point towards yes.',
            'The alphabet soup said yes 🥄',
        ]
        no_responses = [
            'No', 'Nah', 'Probably not', 'Nope, not at all', 'No...definitely not',
            'Nope...', 'balls...no', 'Hold on let me ask science 🔍 \nSources point towards: **No.**',
            'FBI Agent Says🕵️: **No.**'
        ]
        if(question[0:3].upper() == 'HOW'):
            hashInt = hash(question)
            hashInt += ctx.author.id / 2
            random.seed(hashInt)
            response = how_responses[random.randint(0, len(how_responses)-1)]
            await ctx.send(response)
            return
        if(question[0:3].upper() == 'WHY'):
            hashInt = hash(question)
            hashInt += ctx.author.id / 2
            random.seed(hashInt)
            response = why_responses[random.randint(0, len(why_responses)-1)]
            await ctx.send(response)
            return
        if(question[0:4].upper() == 'WHEN'):
            hashInt = hash(question)
            hashInt += ctx.author.id / 2
            random.seed(hashInt)
            response = when_responses[random.randint(0, len(when_responses)-1)]
            await ctx.send(response)
            return
        if (ctx.author.id == 393982976125435934):
            hashInt = hash(question)
            if (question[-1] == '?'):
                random.seed(a=hashInt)
                response = no_responses[random.randint(0, len(no_responses))]
                await ctx.send(response)
                return
            else:
                response = yes_responses[random.randint(0, len(yes_responses))]
                await ctx.send(response)
                return
        else:
            hashInt = hash(question)
            hashInt += ctx.author.id / 2
            random.seed(a=hashInt)
            yn = random.randint(1, 2)
            if yn == 1:
                response = yes_responses[random.randint(0, len(yes_responses) - 1)]
                await ctx.send(response)
                return
            else:
                response = no_responses[random.randint(0, len(no_responses) - 1)]
                await ctx.send(response)
                return

    @commands.command(name='sad')
    async def _sad(self, ctx, user:User = None):
        if (user == None):
            random.seed(ctx.author.id/5 + date.today().day)
            authName = ctx.author.name
            urlIcon = ctx.author.avatar_url
        else:
            random.seed(user.id/5 + date.today().day)
            authName = user.name
            urlIcon = user.avatar_url
        sadRate = random.randint(1, len(self.sadLevels))
        if(user is None):
            if ctx.author.id == 393982976125435934:
                sadRate = len(self.sadLevels)
        sadEmbed = Embed(
            title='Sad Rating:',
            description=self.sadLevels[1]
        )
        sadEmbed.set_author(name=authName, icon_url=urlIcon)
        newSadEmbed = Embed(
            title='Sad Rating:',
            description=self.sadLevels[1]
        )
        newSadEmbed.set_author(name=authName, icon_url=urlIcon)
        sadEmbedmsg = await ctx.send(embed=sadEmbed)
        for slvl in range(1, sadRate):
            newSadEmbed.description = self.sadLevels[slvl]
            await asyncio.sleep(1.5)
            await sadEmbedmsg.edit(embed=newSadEmbed)
    @commands.command(name='simp')
    async def _simp(self, ctx, user: User = None):
        if (user == None):
            random.seed(ctx.author.id + date.today().day)
            authName = ctx.author.name
            urlIcon = ctx.author.avatar_url
        else:
            random.seed(user.id + date.today().day)
            authName = user.name
            urlIcon = user.avatar_url
        simpRate = random.randint(1, len(self.simpLevels))
        simpEmbed = Embed(
            title='Simp Rating:',
            description=self.simpLevels[1]
        )
        simpEmbed.set_author(name=authName, icon_url=urlIcon)
        newSimpEmbed = Embed(
            title='Simp Rating:',
            description=self.simpLevels[1]
        )
        newSimpEmbed.set_author(name=authName, icon_url=urlIcon)
        simpEmbedmsg = await ctx.send(embed=simpEmbed)
        # simpMsg = await ctx.send(self.simpLevels[1])
        for slvl in range(1, simpRate):
            newSimpEmbed.description = self.simpLevels[slvl]
            await asyncio.sleep(1.5)
            await simpEmbedmsg.edit(embed=newSimpEmbed)
            # await simpMsg.edit(content=self.simpLevels[slvl])
        if (simpRate == 7):
            role = get(ctx.server.roles, name='Simp')
            await self.client.add_roles(ctx.author, role)
            await ctx.send(f'{ctx.author.name} has been given Simp role.')

    @commands.command(name='sus')
    async def _sus(self, ctx, user: User = None):
        if (user == None):
            random.seed(ctx.author.id/2 + date.today().day)
            authName = ctx.author.name
            urlIcon = ctx.author.avatar_url
        else:
            random.seed(user.id / 2 + date.today().day)
            authName = user.name
            urlIcon = user.avatar_url
        susRate = random.randint(1, len(self.susLevels))
        susEmbed = Embed(
            title='Sus Rating:',
            description=self.susLevels[1]
        )
        susEmbed.set_author(name=authName, icon_url=urlIcon)
        newSusEmbed = Embed(
            title='Sus Rating:',
            description=self.susLevels[1]
        )
        newSusEmbed.set_author(name=authName, icon_url=urlIcon)
        susEmbedmsg = await ctx.send(embed=susEmbed)

        for slvl in range(1, susRate):
            newSusEmbed.description = self.susLevels[slvl]
            await asyncio.sleep(1.5)
            await susEmbedmsg.edit(embed=newSusEmbed)
        if (susRate == 8):
            role = get(ctx.server.roles, name='sus.')
            await self.client.add_roles(ctx.author, role)
            await ctx.send(f'{ctx.author.name} has been given the sus. role.')

    @commands.command(aliases=['racist', 'racism'])
    async def _racist(self, ctx, user: User = None):
        if (user == None):
            random.seed(ctx.author.id / 3 + date.today().day)
            authName = ctx.author.name
            urlIcon = ctx.author.avatar_url
        else:
            random.seed(user.id / 3 + date.today().day)
            authName = user.name
            urlIcon = user.avatar_url

        racRate = random.randint(1, len(self.susLevels))
        racEmbed = Embed(
            title='Racism Rating:',
            description=self.susLevels[1].replace('SUS', 'RACIST')
        )
        racEmbed.set_author(name=authName, icon_url=urlIcon)
        newRacEmbed = Embed(
            title='Racism Rating:',
            description=self.susLevels[1].replace('SUS', 'RACIST')
        )
        newRacEmbed.set_author(name=authName, icon_url=urlIcon)
        racEmbedmsg = await ctx.send(embed=racEmbed)
        for slvl in range(1, racRate):
            newRacEmbed.description = self.susLevels[slvl].replace('SUS', 'RACIST')
            await asyncio.sleep(1.5)
            await racEmbedmsg.edit(embed=newRacEmbed)

        # embed = Embed(
        #     title = 'Test Title',
        #     description='This is a description',
        #     colour = Color.blue()
        # )
        # embed.set_footer(text='Test Footer')
        # embed.set_image(url="https://images-na.ssl-images-amazon.com/images/I/810lx2GJaPL._AC_SX466_.jpg")
        # embed.set_thumbnail(url="https://www.moving-minds.com/cmsstatic/m-50638-ReflectEDFidgetBalls.jpg")
        # embed.set_author(name='Piro', icon_url="https://www.gannett-cdn.com/presto/2019/09/29/PPOH/58ee8a0a-6974-473a-a38e-96247ff8ff36-American_Crow.GaryHenry.jpg?auto=webp&crop=2047,1152,x0,y0&format=pjpg&width=1200")
        # embed.add_field(name='Field Name1', value='Field Value1', inline=False)
        # embed.add_field(name='Field Name2', value='Field Value2', inline=True)
        # embed.add_field(name='Field Name3', value='Field Value3', inline=True)

    @commands.group(name='help')
    async def _help(self, ctx):
        helpEmbed = Embed(
            title='Help',
            colour=Color.dark_gold(),
        )
        helpEmbed.add_field(name='Fun :game_die:', value="```ping, 8ball,\nsus, simp, sad```", inline=True)
        helpEmbed.add_field(name='Settings :gear:', value="```noimage```", inline=True)
        helpEmbed.add_field(name='Twitter :bird:', value="```stream,\nstop```", inline=False)
        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(Fun(client))
