import discord
import log
import reddit_otters as reddot
import threading as th
import time
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
client.run("MTA4ODM4NTEzMzM2MDQ2ODAyOA.Gg56TW.qObASSxPA1Vx-dzO2cHyByKHBO_AvP6ZVlTrTo")
qtList = []

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


async def checkQTs():
    global qtList
    newQTs = reddot.get_url(reddot.authenticate(), "Otters", 20)
    i = 0
    for qts in newQTs:
        if "gallery" in qts or "v.redd.it" in qts or qtList.count(qts) != 0:
            newQTs[i] = None
        i += 1
    qtList = newQTs
    if qtList is not None and activeChannel is not None:
        for qts in qtList:
            await activeChannel.send(qts)


def holdOnASecond():
    time.sleep(10)
    checkQTs()
    holdOnASecond()


def main():
    timer = th.Thread(target=holdOnASecond(), daemon=True)
    timer.start()


main()
