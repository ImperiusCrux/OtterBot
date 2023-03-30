import time
import discord
import log
import reddit_otters as reddot
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
intents=discord.Intents.all()
client = discord.Client(intents=intents)

activeChannel = None


@client.event
async def on_ready():
    log.log(0, "Bot is ready.")


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="Paddel_nach")
@commands.has_role("Enhydra lutris")
async def setChannel(ctx, nextChannel: str):
    global activeChannel
    guild = ctx.guild
    for channel in guild.channels:
        current = channel.GuildChannel.name
        if current is nextChannel and current is discord.ChannelType.text:
            activeChannel = client.get_channel(current.id)
            break

    if activeChannel is None:
        ctx.send("Hoppla, diesen Channel kann ich nicht finden.")
        log.log(1, "Channel not found :C" )
        return
    await ctx.send("Okey dokey!")
    time.sleep(1)
    await activeChannel.send("Nett hier!")
    log.log(0, "Connected to new Channel.")

def main():
    reddot.get_top_otters(3, "reddit.com")


