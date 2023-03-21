from dotenv import load_dotenv
from os import getenv, listdir
from discord.ext import commands
from discord import app_commands, Intents
from tree_commands.gpt import Gpt

intents = Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

load_dotenv()


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(len(synced), 'commands synced')
    except Exception as e:
        print(e)
    for filename in listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    print(f'Logged in as {bot.user}')


@bot.tree.command(name='gpt', description='Generate text with GPT-3')
@app_commands.describe(question='What would you like to ask GPT-3?')
async def gpt(ctx, question: str):
    gpt = Gpt(bot).gpt
    await gpt(ctx, question)


bot.run(getenv('TOKEN'))
