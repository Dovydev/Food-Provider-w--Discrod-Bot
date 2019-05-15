import discord, os, time, codecs

TOKEN = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!info'):
        await message.channel.send('Projekt innom programering 1, såkallad slutprojekt. \nSkapad av https://github.com/dovydev - Dovydas Bumblauskas\nVersion: 0.102')
        
    if message.content.startswith('!invite'):
        await message.channel.send('https://discordapp.com/oauth2/authorize?client_id=577830723805773844&scope=bot&permissions=93184')
        time.sleep(3)
        await message.delete()

    if message.content.startswith('!veckans'):
        message = await message.channel.send('Data hämtas...')
        file1 = open("food.txt","a")
        file1.write("")
        file1.close()
        os.system('python get.py')
        time.sleep(1)
        f = codecs.open("food.txt", "r", "utf-8")
        await message.delete()
        for x in f:
            await message.channel.send(x)
        f.close()
        
client.run(TOKEN)