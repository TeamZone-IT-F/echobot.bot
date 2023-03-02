import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_join(member):
    overwrites = {
        member: discord.PermissionOverwrite(read_messages=True),
        member.guild.default_role: discord.PermissionOverwrite(read_messages=False)
    }
    channel = await member.guild.create_text_channel(f"{member.name}-private", overwrites=overwrites)
    await channel.send(f"Welcome {member.mention} to your private channel! This channel is only visible to you and the bot.")

bot.run(os.environ["DISCORD_TOKEN"])

