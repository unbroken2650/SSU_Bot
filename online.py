import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA4OTc4ODgzODM1Mzg1MDQyMA.G3MVZG.D4zWPLG8VIbOrRSxHt88_8_kPxwfkW7BEX_sZ8')