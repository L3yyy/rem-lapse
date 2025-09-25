import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
from better_profanity import profanity
import aiohttp

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
profanity.load_censor_words()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='y!', intents=intents)

role = "kokak"
secret_role = "kokak"

@bot.event
async def on_ready():
    print(f"We're ready, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event

# assign
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{secret_role} has been assigned to {ctx.author.mention}")
    else:
        await ctx.send("Role not found.")

# catto command
@bot.command()
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

# doggo command
@bot.command()
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

# fact command
@bot.command()
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

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said '{msg}'")

@bot.command()
async def helpme(ctx):
    embed = discord.Embed(
        title = "Here's the command menu, senpai:",
        color = discord.Color.blue()
    )
    embed.add_field(name = "HELPFUL LINKS", value = ("[Support Server](https://discord.gg/gxM5TufB8Y)\n" "[GitHub](https://github.com/L3yyy)\n" "[Invite This Bot](https://discord.com/oauth2/authorize?client_id=1380535770489688114&permissions=378295814145&integration_type=0&scope=bot)"), inline = False)
    embed.add_field(name = "COMMANDS", value = "List of available commands:", inline = False)

    embed.add_field(name = "y!assign", value = "Assign the <@&1416039574517321831> to yourself", inline = False)
    embed.add_field(name = "y!helpme", value = "Get a list of available commands", inline = False)
    embed.add_field(name = "y!catto", value = "Grabs a random cat image online", inline = False)
    embed.add_field(name = "y!doggo", value = "Grabs a random dog image online", inline = False)
    embed.add_field(name = "y!fact", value = "Gives you a random useless fact", inline = False)
    embed.set_footer(text = "More features coming soon!")
    await ctx.send(embed = embed)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)