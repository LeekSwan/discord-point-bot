import os
import discord
from discord import app_commands
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

load_dotenv()
connect = cursor = db = None

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@tree.command(name = "commandname", description = "My first application Command") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

client.run(os.environ.get('DISCORD_CONNECT'))
