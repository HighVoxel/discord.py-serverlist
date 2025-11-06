import discord 
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def serverlist(ctx):
    for guild in bot.guilds:
        await ctx.send(await guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True))
    await ctx.send("全サーバーの招待リンクを取得しました")

bot.run("Token")
