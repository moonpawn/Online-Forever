import discord
import os
from keep_alive import keep_alive
from discord.ext import commands

name_of_stream_status = "Hello World" #Name that show on stream status, Ex : {username} streaming [...]
stream_link = "https://twitch.tv/CustomStreamLink" #Must be a twitch link only, nothing else will work 
client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Streaming(name = f"{name_of_stream_status}", url = f"{stream_link}"))
  os.system('clear')
  print(f'Logged in as {client.user} (ID: {client.user.id})')

keep_alive()
client.run(os.getenv("TOKEN")) #Must be a secret on replit, if you are hosting this script without replit or if you have a hacker plan on, check for the code needed on the readme.md
