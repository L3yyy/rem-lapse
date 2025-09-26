import os
import logging
import discord
import aiohttp

from discord.ext import commands
from dotenv import load_dotenv
from better_profanity import profanity
from discord import app_commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
profanity.load_censor_words()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix = ['rem ', 'rem'], intents = intents, case_insensitive = False)

@bot.event
async def on_ready():
    activity = discord.Game(name = "with Ley-senpai")

    await bot.change_presence(status = discord.Status.online, activity=activity)
    print(f"We're ready, {bot.user.name}")

    try:
        synced = await bot.tree.sync()  # sync slash commands
        print(f"✔ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# MEMBER JOIN FUNCTION
@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title = "💌  Invite Rem-lapse",
        description = (
            f"Oh! Welcome to the server, {member.mention}-senpai!\n\n"
            "If you are interested on having me in your server, here's my invite link:\n"
            "[✨ Invite me ✨](https://discord.com/oauth2/authorize?client_id=1380535770489688114&permissions=378295814145&scope=bot%20applications.commands)\n\n"
        ),
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url = bot.user.avatar.url if bot.user.avatar else None)
    await member.send(embed = embed)

# CATTO COMMAND
@bot.hybrid_command(name = "catto", description = "Get a random picture of a cat.", aliases = ['cat'])
async def catto(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            image_url = data[0]["url"]

    embed = discord.Embed(
        title = "Here's a random *neko* for you! Nyahhh~! 🐱",
        color = discord.Color.blue()
    )
    embed.set_image(url = image_url)
    embed.set_footer(text = "Powered by The Cat API")

    await ctx.send(embed = embed)

# DOGGO COMMAND
@bot.hybrid_command(name = "doggo", description = "Get a random picture of a dog.", aliases = ['dog'])
async def doggo(ctx):
    url = "https://api.thedogapi.com/v1/images/search"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            image_url = data[0]["url"]

    embed = discord.Embed(
        title = "Here's a random *doggo* for you! Woof~! 🐶",
        color = discord.Color.blue()
    )
    embed.set_image(url = image_url)
    embed.set_footer(text = "Powered by The Dog API")

    await ctx.send(embed = embed)

# FACT COMMAND
@bot.hybrid_command(name = "fact", description = "Receive a random fun fact.")
async def fact(ctx):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            fact_text = data ["text"]
    
    embed = discord.Embed(
        title = "💡 Did you know?",
        description = fact_text,
        color = discord.Color.blue()
    )
    embed.set_footer(text = "Powered by Useless Facts API")

    await ctx.send(embed = embed)

# INVITE COMMAND
@bot.hybrid_command(name = "invite", description = "Get the bot's invite link.")
async def inv(ctx):
    embed = discord.Embed(
        title = "💌  Invite Rem-lapse",
        description = (
            f"Oh! You want me to join your server, {ctx.author.mention}-senpai?\n\n"
            "Aww.. Thank you so much! Here's my invite link:\n"
            "[✨ Invite me ✨](https://discord.com/oauth2/authorize?client_id=1380535770489688114&permissions=378295814145&scope=bot%20applications.commands)\n\n"
            "Feeling lost? Join our support server:\n"
            "[🔎 Join here 🔎](https://discord.gg/hg7vtGfVQ8)"
        ),
        color = discord.Color.blue()
    )

    embed.set_thumbnail(url = bot.user.avatar.url if bot.user.avatar else None)
    await ctx.send(embed = embed)

bot.remove_command('help')
# HELP COMMAND
@bot.hybrid_command(name = "help", description = "Show all available commands.")
async def help(ctx):
    embed = discord.Embed(
        title = f"Here's the command menu, senpai:",
        description = f"Prefix `{bot.command_prefix[1]}`",
        color = discord.Color.blue()
    )
    embed.add_field(name = "🔗 HELPFUL LINKS", value = ("[Support Server](https://discord.gg/gxM5TufB8Y)\n" "[GitHub](https://github.com/L3yyy)\n" "[Invite This Bot](https://discord.com/oauth2/authorize?client_id=1380535770489688114&permissions=378295814145&scope=bot%20applications.commands)"), inline = False)
    embed.add_field(name = "⚙️ COMMANDS", value = "List of available commands:", inline = False)

    embed.add_field(name = "fun", value = "Show all fun commands", inline = False )
    embed.add_field(name = "help", value = "Show all available commands.", inline = False)
    embed.add_field(name = "catto, cat", value = "Get a random picture of a cat.", inline = False)
    embed.add_field(name = "doggo, dog", value = "Get a random picture of a dog.", inline = False)
    embed.add_field(name = "fact", value = "Receive a random fun fact.", inline = False)
    embed.add_field(name = "invite", value = "Get the bot's invite link.", inline = False)
    embed.add_field(name = "serverinfo, svinfo, svinf", value = "View information about this server.", inline = False)
    embed.set_footer(text = "✨ More features coming soon!")
    await ctx.send(embed = embed)

# FUN COMMANDS
@bot.hybrid_command(name = "fun", description = "Show all fun commands.")
async def fun(ctx):
    embed = discord.Embed(
        title = f"Here's a list of fun commands, senpai:",
        color = discord.Color.blue()
    )
    embed.add_field(name = "catto, cat", value = "Get a random picture of a cat.", inline = False)
    embed.add_field(name = "doggo, dog", value = "Get a random picture of a dog.", inline = False)
    embed.add_field(name = "fact", value = "Receive a random fun fact.", inline = False)

    embed.set_footer(text = "type `rem help` to get a list of all available commands.")
    
    await ctx.send(embed = embed) 

@bot.hybrid_command(name = "serverinfo", description = "View information about this server.", aliases = ['svinf', 'svinfo'])
async def serverinfo(ctx):
    guild = ctx.guild
    author = ctx.author
    boost_level = guild.premium_tier
    boost_count = guild.premium_subscription_count

    embed = discord.Embed(
        title = f"Server info of {guild.name}",
        color = discord.Color.blue()
    )

    embed.set_author(name = f"{author}", icon_url=author.avatar.url if author.avatar else None)
    embed.set_thumbnail(url = guild.icon.url if guild.icon else None)

    embed.add_field(name = "Server Name", value = guild.name, inline = True)
    embed.add_field(name = "Server ID", value = guild.id, inline = True)
    embed.add_field(name = "Owner", value = guild.owner.mention, inline = True)
    embed.add_field(name = "Members", value = guild.member_count, inline = True)

    embed.add_field(name = "Text Channels", value = len(guild.text_channels), inline = True)
    embed.add_field(name = "Voice Channels", value = len(guild.voice_channels), inline = True)

    embed.add_field(name = "Roles", value = len(guild.roles), inline = True)
    embed.add_field(name = "Boosts & Level", value = f"{boost_level} {boost_count}", inline = True)
    
    embed.set_footer(text = "Server Info")
    await ctx.send(embed = embed)

# COPILOT-GENERATED CODE | PING COMMAND
@bot.hybrid_command(name = "ping", description = "Check the bot's latency")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

bot.run(token, log_handler = handler, log_level = logging.DEBUG)
