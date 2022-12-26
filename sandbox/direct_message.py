import os
from discord.ext import commands
import discord
# from kcjargon.kcjargon.openai import conversation

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


# class MyBot(commands.Bot):
#     def __init__(self):
#         super().__init__(command_prefix='!', intents=intents)

#     async def on_ready(self):
#         print('Logged in as')
#         print(self.user.name)
#         print(self.user.id)
#         print('------')

#     async def on_message(self, message):
#         # we do not want the bot to reply to itself
#         if message.author.id == self.user.id:
#             return

#         if message.content.startswith('!hello'):
#             await message.channel.send('Hello {0.author.mention}'.format(message))


class MyChatbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello! How can I help you?')

    @commands.command()
    async def dm(self, ctx, *, message):
        user = ctx.message.author
        await user.send(message)


def setup(bot):
    bot.add_cog(MyChatbot(bot))


setup(bot)
# bot = MyChatBot()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))

# @bot.command(pass_context=True)
# async def DM(ctx, user: discord.User, *, message=None):
#     message = message or "Please enter a description"
#     if not user:
#         print(f"User is none: {user}")
#     # TODO: THIS IS NULL
#     await bot.send_message(user, message)
# @bot.command()
# async def reply(ctx, message):
#     await ctx.send(f"You said: {message}")

# @bot.command()
# async def chat(ctx, message):
#     if message == "hello":
#         await ctx.send("Hi there!")
#     elif message == "how are you?":
#         await ctx.send("I'm doing great, thanks for asking!")
#     else:
#         await ctx.send("I'm sorry, I don't understand.")

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('------')

#     async def on_message(self, message):
#         # we do not want the bot to reply to itself
#         if message.author.id == self.user.id:
#             return

#         if message.content.startswith('!hello'):
#             await message.reply('Hello!', mention_author=True)


# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run('token')



