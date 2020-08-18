import discord
import aiohttp

tokenFile = open("token.txt", "r")
tokenList = tokenFile.readlines()
print(tokenList)
token = "";
for x in tokenList:
    token += x[0]
print(token)
id = 703700230251610172
client = discord.Client()




@client.event
async def on_message(message):
    id = client.get_guild(703700230251610172)

    def compare(word):
        check = message.content.lower()
        if check.find(word.lower()) == -1:
            return False
        else:
            return True

    def checkCommand(command):
        words = message.content.split()
        if words[0].lower() == command:
            return True
        else:
            return False

    def getCommand(wantList):
        words = message.content.split()
        command = []
        for i in range(1, len(words)):
            command.append(words[i])
        if wantList:
            return command
        else:
            wordCom = ""
            for i in range(len(command)):
                wordCom += command[i] + " "
            return wordCom

    def embedImage(purl, title):
        pUrl = purl
        embed = discord.Embed(
            title=title,
            url=purl
        )
        embed.set_image(url=pUrl)

        return embed

    if compare("jaishil is gay"):
        await message.channel.send("very gay indeed", tts=True)

    elif compare("my balls itch") or compare("mbi"):
        await message.channel.send("same bro")

    elif compare("i'm gay") or compare("im gay"):
        await message.channel.send("I agree, " + message.author.display_name + " is gay")

    elif compare("users"):
        await message.channel.send(f"""Number of Members:  {id.member_count} """)

    elif compare("mihir is gay"):
        await message.author.edit(nick="i am big gay")

    elif compare("i love mihir"):
        embed = embedImage("https://cdn.pixabay.com/photo/2016/10/04/16/33/heart-shape-1714807_960_720.jpg", "Why Thank You")
        await message.channel.send(embed=embed)

    if checkCommand("-n"):
        if message.mentions != []:
            words = getCommand(True)
            user = message.mentions[0]
            newName = ""
            for i in range(1, len(words)):
                newName += words[i] + " "
        else:
            newName = getCommand(False)
            user = message.author

        await user.edit(nick=newName)


    if checkCommand("clear"):
        num = int(getCommand(False))
        deleted = await message.channel.purge(limit=num)
        await message.channel.send('Deleted {} message(s)'.format(len(deleted)))

    if compare("cutest white boy") or compare("caden"):
        embed = embedImage("https://i.imgur.com/6weiAAu.jpg", "the one and only")
        await message.channel.send(embed=embed)

    if compare("alex"):
        embed = embedImage("https://i.imgur.com/JDzXuSa.jpg", "alex man")
        await message.channel.send(embed=embed)

    if compare("jaishil"):
        embed = embedImage("https://i.imgur.com/hkseTHR.png", "ew")
        await message.channel.send(embed=embed)

    if compare("kahil"):
        embed = embedImage("https://i.imgur.com/E3W8sLK.jpg", "oh yes")
        await message.channel.send(embed=embed)

    if compare("dylan"):
        embed = embedImage("https://i.imgur.com/jiTkP0x.jpg", "plane man")
        await message.channel.send(embed=embed)

    if compare("lizzo") or compare("cardi b"):
        embed = embedImage("https://images-na.ssl-images-amazon.com/images/I/417CVAiSffL._AC_SY355_.jpg", "i only speak the truth")
        await message.channel.send(embed=embed)

    if compare("parth"):
        embed = embedImage("https://i.imgur.com/3KoUMsf.png", "very nice")
        await message.channel.send(embed=embed)

    if compare("abhi") or compare("abhinav"):
        embed = embedImage("https://i.imgur.com/tmrfmuC.jpg", "giraffe")
        await message.channel.send(embed=embed)

    elif compare("mihir"):
        embed = embedImage("https://i.imgur.com/WmykdDd.jpg", "intelligent man")
        await message.channel.send(embed=embed)

    elif compare("dj") or compare("dong jong"):
        embed = embedImage("https://i.imgur.com/L3uXwVI.jpg", "tall man")
        await message.channel.send(embed=embed)





        


client.run(token)