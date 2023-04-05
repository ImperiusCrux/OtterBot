import asyncio
import discord
import connect_backup as reddot
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

qtList = []
activeChannel = None


@bot.event
async def on_ready():
    await holdOnASecond(68400)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name="Paddel_nach")
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
            return
        await ctx.send("Okey dokey!")
        await asyncio.sleep(1)
        await activeChannel.send("Nett hier!")
    except Exception as e:
        return


async def checkQTs():
    try:
        global activeChannel
        global qtList
        if activeChannel is None:
            return
        newQTs = await reddot.get_url(await reddot.authenticate(), "Otters", 10)
        i = 0
        if newQTs is None:
            await activeChannel.send("Hoppla ich konnte keine neuen Otter finden.")
            return
        help = []
        for qts in newQTs:
            if "gallery" in qts or "v.redd.it" in qts or qts in qtList:
                newQTs[i] = None
            i += 1
        helpList = qtList
        qtList = newQTs
        if qtList is not None and activeChannel is not None:
            j = 0
            for qts in qtList:
                if qtList[j] is not None:
                    await activeChannel.send(qts)
                    await asyncio.sleep(1)
                j += 1
        qtList = qtList + helpList
    except Exception as e:
        return

async def holdOnASecond(seconds):
    await checkQTs()
    await asyncio.sleep(seconds)
    await holdOnASecond(seconds)

bot.run(os.getenv("TOKEN"))



