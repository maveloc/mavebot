import discord
from discord.ext import commands
from jokeapi import Jokes
import requests
import alpsctr


#le declaramos a discord la intencion de usar sus cositas y leer el contenido
#de mensajes
intents = discord.Intents.default()
intents.message_content = True


bot= commands.Bot(command_prefix="$", intents=intents)

#comando chistes
@bot.command()
async def chiste(ctx):
    """cuenta un chiste (posiblemente malo)"""
    j = await Jokes()  # Initialise the class
    chiste = await j.get_joke(lang="es", amount=1, joke_type="single", response_format="txt")  # Retrieve a random joke
    await ctx.send(chiste)
#linea de control
#comando para que el bot salude
@bot.command()
async def hola(ctx):
    """saluda al usuario"""
    respuesta=ctx.author.name

    if respuesta== "mave7609":
        respuesta="creador"
    await ctx.send(f"hola {respuesta}")



#simplemente hago que al ejecutarse diga que está listo
@bot.event
async def on_ready():
    print(f"{bot.user} está listo!")


bot.run(alpsctr.token)