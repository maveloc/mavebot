import os
import discord
from discord.ext import commands
from jokeapi import Jokes
import requests
import alpsctr
import random


#le declaramos a discord la intencion de usar sus cositas y leer el contenido
#de mensajes
intents = discord.Intents.default()
intents.message_content = True


bot= commands.Bot(command_prefix="$", intents=intents)

# Función para cargar todos los cogs
async def load_extensions():
    # Itera sobre los archivos en el directorio 'cogs'
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            # El nombre del Cog es 'cogs.nombre_archivo_sin_.py'
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Cog cargado: {filename}")

# Evento para asegurar que los cogs se carguen al iniciar
@bot.event
async def on_ready():
    print(f'Bot iniciado como {bot.user.name}')
    await load_extensions()



bot.run(alpsctr.token)