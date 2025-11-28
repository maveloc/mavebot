import random
from discord.ext import commands
import requests
from jokeapi import Jokes
import alpsctr

class ComandosBasicos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def lilith(self, ctx):
        await ctx.send("Es asi como rarita no?")


    @commands.command()
    async def sonia(self, ctx):
        await ctx.send("Esa anda desaparecida o que")

    #esto ya es personal
    @commands.command()

    async def tonto(self, ctx):
        """te insulta"""
        insultos = ["la de trabajar te la sabes?",
                "ve a incordiar a otro lado","no tienes nada mejor que pelear contra un bot? tonto",
                "calla cabacepas", "te huele el pito feo","bajas el coeficiente intelectual de todos con solo entrar en discord",
                "me voy a coger a tu papá y le voy a dar un hijo que de verdad quiera.","eres el mejor del grupo de educacion especial",
                "tus dos neuronas pelean a ver quién llega en tercer lugar","tu mami no te deja usar cuchillos todavía?"]
        ruleta_insultos = random.choice(insultos)
        await ctx.send(ruleta_insultos)

        #comando quotes de famosos
    @commands.command()
    async def animame(self, ctx):
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
    @commands.command()
    async def chiste(self, ctx):
        """cuenta un chiste (posiblemente malo)"""
        j = await Jokes()  # Initialise the class
        chiste = await j.get_joke(response_format="txt")  # Retrieve a random joke
        await ctx.send(chiste)

    #comando para que el bot salude
    @commands.command()
    async def hola(self, ctx):
        """saluda al usuario"""
        respuesta=ctx.author.name

        if respuesta== "mave7609":
            respuesta="creador"
        elif respuesta == "guisantegordito":
            respuesta=", que cachondita me pones guarro"
        await ctx.send(f"hola {respuesta}")

# Esta función es OBLIGATORIA para que el bot cargue el Cog
async def setup(bot):
    await bot.add_cog(ComandosBasicos(bot))