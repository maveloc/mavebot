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


#esto ya es personal
@bot.command()

async def tonto(ctx):
    """te insulta"""
    insultos = ["la de trabajar te la sabes?",
                "ve a incordiar a otro lado","no tienes nada mejor que pelear contra un bot? tonto",
                "calla cabacepas", "te huele el pito feo","bajas el coeficiente intelectual de todos con solo entrar en discord",
                "me voy a coger a tu papá y le voy a dar un hijo que de verdad quiera.","eres el mejor del grupo de educacion especial",
                "tus dos neuronas pelean a ver quién llega en tercer lugar","tu mami no te deja usar cuchillos todavía?"]
    ruleta_insultos = random.randint(1,10)
    print(ruleta_insultos)
    await ctx.send(insultos[ruleta_insultos])




#comando quotes de famosos
@bot.command()
async def animame(ctx):
    """Te saca la quote mas buena del mundo"""
    categories = 'success,wisdom,love,philosophy'
    api_url = 'https://api.api-ninjas.com/v2/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': alpsctr.quoteToken}, 
                            params={'categories': categories})
    #la respuesta de la api la guardamos como json al 
    #cual luego accedemos en el index 0 (todo) a claves especificas
    data= response.json()
    autor = data[0]['author']
    quote = data[0]['quote']
    if response.status_code == requests.codes.ok:
        await ctx.send(f"{autor} dijo una vez: {quote}..\n que razon tenia.")
    else:
        print("Error:", response.status_code, response.text)


#comando chistes
@bot.command()
async def chiste(ctx):
    """cuenta un chiste (posiblemente malo)"""
    j = await Jokes()  # Initialise the class
    chiste = await j.get_joke(response_format="txt")  # Retrieve a random joke
    await ctx.send(chiste)

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