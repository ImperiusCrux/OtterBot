import asyncio
from threading import Timer
import threading as th
import discord
import log
import reddit_otters as reddot
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

qtList = []
activeChannel = None


@bot.event
async def on_ready():
    await holdOnASecond(10)
    log.log(0, "Bot is ready.")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name="paddel_nach")
@commands.has_role("Enhydra lutris")
async def moveChannel(ctx, nextChannel):
    try:
        global activeChannel
        guild = ctx.guild
        for channel in guild.channels:
            if channel.name == nextChannel and channel.type == discord.ChannelType.text:
                activeChannel = bot.get_channel(channel.id)
                break

        if activeChannel is None:
            await ctx.send("Hoppla, diesen Channel kann ich nicht finden.")
            log.log(1, "Channel not found :C" )
            return
        await ctx.send("Okey dokey!")
        time.sleep(1)
        await activeChannel.send("Nett hier!")
        log.log(0, "Connected to new Channel.")
    except Exception as e:
        log.log(2, str(e) + "Die FLosse klemmt.")


@tasks.loop(seconds=10)
async def loopDeLoop():
    print("loop")


async def checkQTs():
    print("check running")
    try:
        global activeChannel
        global qtList
        newQTs = await reddot.get_url(await reddot.authenticate(), "Otters", 20)
        i = 0
        for qts in newQTs:
            if "gallery" in qts or "v.redd.it" in qts or qtList.count(qts) != 0:
                newQTs[i] = None
            i += 1
        qtList = newQTs
        if qtList is not None and activeChannel is not None:
            print("hopp")
            for qts in qtList:
                await activeChannel.send(qts)
    except Exception as e:
        log.log(2, str(e) + "Hilfe wo sind meine Otter?")


async def holdOnASecond(seconds):
    await checkQTs()
    await asyncio.sleep(seconds)
    await holdOnASecond()


async def holdOnTwoSecs():
    print("1")
    await asyncio.sleep(10)
    print("2")
    await holdOnTwoSecs()


#async def loopDeLooper():
#    await loopDeLoop.start()

bot.run("MTA4ODM4NTEzMzM2MDQ2ODAyOA.Gg56TW.qObASSxPA1Vx-dzO2cHyByKHBO_AvP6ZVlTrTo")
#asyncio.run(loopDeLooper())



