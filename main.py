import discord, discordRadio, sys, check
from discord.ext import commands

skyplus_url = "https://skymedia.babahhcdn.com/SKYPLUS_boadcast"
elmar_url = "https://router.euddn.net/8103046e16b71d15d692b57c187875c7/elmar.mp3"

TOKEN = check.isFile()

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    activity = discord.Game(name="Raadio Elmar", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot online")

@client.command()
async def abi(ctx):
    embed=discord.Embed(title="Käsud", color=discord.Color.gold())
    embed.add_field(name=".laula", value="- Laulab parimat raadiot maailmas.", inline=False) 
    embed.add_field(name=".skyplus", value="- Laulab mitte nii head raadiot kui Raadio Elmar.", inline=False) 
    embed.add_field(name=".lahku", value="- Lahkub kõnest.", inline=False) 
    await ctx.send(embed=embed)
  
@client.command()
async def lahku(ctx):
    if not ctx.guild.voice_client in client.voice_clients:
        await ctx.send("Ma olen juba lahkunud tola!")
    else:
        print("Leaving voice channel")
        await ctx.send("Tsauki!")
        await ctx.voice_client.disconnect()

@client.command()
async def laula(ctx):
    await discordRadio.play(ctx, elmar_url, await check.inVoice(ctx, client), await check.isPlaying(ctx), "elmar")

@client.command()
async def skyplus(ctx):
    await discordRadio.play(ctx, skyplus_url, await check.inVoice(ctx, client), await check.isPlaying(ctx), "skyplus")

client.run(TOKEN)