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



guildId = [788080898704015391]
@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id = 788080898704015391))
async def first_command(interaction, member: discord.Member, amount: int = 1):
    await interaction.response.send_message("Hello!" + str(amount))

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

client.run(os.environ.get('DISCORD_CONNECT'))

