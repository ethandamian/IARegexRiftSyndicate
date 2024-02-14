import discord
from ChatBot import ChatBot
from discord.ext import commands

chatbot = ChatBot()


# async function to send message
async def send_message(message, user_message, is_private):
    respoonse = chatbot.responder(user_message)
    (
        await message.author.send(respoonse)
        if is_private
        else await message.channel.send(respoonse)
    )


def run_discord_bot():

    TOKEN = ""

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # este es un comando para el bot, al escribirlo en el chat, se tiene que poner !<nombre del comando>
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def downloadLol(ctx):

        await ctx.send(
            "¿Quieres descargar LOL? aquí tienes:\nhttps://signup.leagueoflegends.com/es-mx/signup/redownload"
        )

    @bot.command()
    async def matate(ctx):
        """Te contesta descaradamente"""
        await ctx.send("Ni sabes jugar bien hazlo tu")

    @bot.command()
    async def rangos(ctx):
        """ "Muestra los rangos disponibles de lol"""
        await ctx.send(
            "-Hierro\n-Bronce\n-Plata\n-Oro\n-Platino\n-Esmeralda\n-Diamante\n-Maestro\n-Gran Maestro\n-Retador"
        )

    @bot.event
    async def on_ready():
        print(f"{bot.user} bienvenido a la ruta del invocador")

        await ctx.send(
            "¿Quieres descargar LOL? aquí tienes:\nhttps://signup.leagueoflegends.com/es-mx/signup/redownload"
        )

    @bot.command()
    async def musicaInsana(ctx):
        await ctx.send(
            "Aqui te dejo una rola para que te motives:\nhttps://www.youtube.com/watch?v=C3GouGa0noM"
        )

    @bot.command()
    async def musicaAntiTilteo(ctx):
        await ctx.send(
            "Aqui te dejo una rola para que te relajes:\nhttps://www.youtube.com/watch?v=eeNYBMe0dAE"
        )

    @bot.command()
    async def bestPlayer(ctx):
        await ctx.send(
            "¿Quieres conocer al mejor jugador de LOL? aquí tienes:\nhttps://www.youtube.com/@T1_Faker"
        )

    @bot.command()
    async def wiki(ctx):
        await ctx.send(
            "¿Quieres conocer la wiki de LOL:\nhttps://leagueoflegends.fandom.com/es/wiki/League_of_Legends_Wiki"
        )

    @bot.event
    async def on_ready():
        print(f"{bot.user} bienvenido a la ruta del invocador")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: {user_message} in {channel}")

        if (
            isinstance(message.channel, discord.TextChannel)
            and message.channel.name == "bot-testing"
        ):
            if user_message.startswith("!priv"):
                user_message = user_message[5:]  # Eliminar el comando "!priv"
                await send_message(message, user_message, is_private=True)
            else:
                if not user_message.startswith("!"):
                    await send_message(message, user_message, is_private=False)

        await bot.process_commands(message)

    bot.run(TOKEN)

    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print("Proceso interrumpido. Saliendo...")
        bot.logout()


run_discord_bot()
