import discord
import aiohttp
import random
import time

tokenFile = open("token.txt", "r")
tokenList = tokenFile.readlines()
token = "";
for x in tokenList:
    token += x[0]
id = 703700230251610172
client = discord.Client()
lastNum = 0
wantPics = True


planeGifUrls = ["https://media1.tenor.com/images/aca8586d66dea2e08350081215a500dd/tenor.gif?itemid=8158374",
                "https://media1.tenor.com/images/83715a6e56f08f82199fd039f7084131/tenor.gif?itemid=14560718",
                "https://media1.tenor.com/images/e3337367c758871c4efb3159baff2c0d/tenor.gif?itemid=8158394",
                "https://media1.tenor.com/images/87583d54ffbdb1b05d3e05fdc1e004b1/tenor.gif?itemid=10577397",
                "https://media1.tenor.com/images/0cbcf3e5ff1086618ff3dceba85f3bce/tenor.gif?itemid=5499077",
                "https://media1.tenor.com/images/d054bce45f7db912cbd7d6eddb84ee5b/tenor.gif?itemid=4951023",
                "https://media1.tenor.com/images/dc15a5beabdbaed14f113c73a51cab2f/tenor.gif?itemid=12120353",
                "https://media1.tenor.com/images/3d6e0950a24bab637d783f217b7074c5/tenor.gif?itemid=17480645",
                "https://media1.tenor.com/images/206e054ea209983d4dbe72a29ac1b26d/tenor.gif?itemid=4891581",
                "https://media1.tenor.com/images/9b0a2828823f4855d52ffd1c634d4c41/tenor.gif?itemid=10498356",
                "https://media1.tenor.com/images/b8a228590919712792210e2bf15fe7f9/tenor.gif?itemid=8806598",
                "https://media1.tenor.com/images/bbcc43c18ca31bbdf266a2d37f535423/tenor.gif?itemid=8825513",
                "https://media1.tenor.com/images/aa3876e89cb39b63a5e948731c5ee3b6/tenor.gif?itemid=12221543",
                "https://media1.tenor.com/images/ed47722a2ba9ce66eaf92a067535d4cf/tenor.gif?itemid=16898320"
        ]

jaishilPics = ["https://i.imgur.com/hkseTHR.png"

]



@client.event
async def on_message(message):
    global lastNum, id, wantPics
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

    if checkCommand("-s"):
        status = "Pictures On: " + str(wantPics)
        await message.channel.send(status)
        await message.channel.send("Jisl: Is still gay")

    elif compare("my balls itch") or compare("mbi"):
        await message.channel.send("same bro")

    elif compare("i'm gay") or compare("im gay"):
        await message.channel.send("I agree, " + message.author.display_name + " is gay")

    elif compare("users"):
        await message.channel.send(f"""Number of Members:  {id.member_count} """)

    elif compare("mihir is gay"):
        await message.author.edit(nick="i am big gay")
        await message.author.edit(voice_channel=None)

    elif compare("i love mihir"):
        embed = embedImage("https://cdn.pixabay.com/photo/2016/10/04/16/33/heart-shape-1714807_960_720.jpg", "Why Thank You")
        await message.channel.send(embed=embed)

    elif compare("dylan is plane"):
        await message.channel.send("plane sex")


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

    if checkCommand("-h"):
        await message.channel.send("-h: help\n-d: disconnects the mentioned person\n-n: (nickname) changes your nickname or the nickname of the person you mentioned\n-s: tells you status\nclear: (number < 50): deletes the number of messages you specified but excludes pinned messages\npclear: (number < 50): deletes the number of messages you specified including pinned messages")

    if checkCommand("clear"):
        if message.author.name == "shrek":
            await message.channel.send("silly child, priveleges are for the men")
        elif message.author.name == "Abhinav":
            await message.channel.send("it is in my professional opinion that you are in fact homosexual and therefore i cannot perform this action")
        elif message.author.name == "J.Shah10":
            await message.channel.send("well how about no silly")
        elif message.author.name == "alexn8":
            await message.channel.send("stop trying to clear it, it'll never go away...")
        else:

            num = int(getCommand(False))
            messages = await message.channel.history(limit=num + 1).flatten()
            if num <= 50:
                for i in range(0, num + 1):
                    if messages[i].pinned == False:
                        await messages[i].delete()
                    else:
                        i -= 1
            else:
                await message.channel.send("bruh stop putting big numbers or you're gay")

    if checkCommand("pclear"):
        if (message.author.name == "SmileyFace21"):
            await message.channel.send("silly child, priveleges are for the men")
        else:
            num = int(getCommand(False))
            messages = await message.channel.history(limit=num + 1).flatten()
            if num <= 50:
                for i in range(0, num + 1):
                    await messages[i].delete()



            else:
                await message.channel.send("bruh stop putting big numbers or you're gay")

    if checkCommand("-o") and getCommand(False) == "":
        if wantPics:
            wantPics = False
        else:
            wantPics = True

    if wantPics:

        if compare("cutest white boy") or compare("caden"):
            embed = embedImage("https://i.imgur.com/6weiAAu.jpg", "the one and only")
            await message.channel.send(embed=embed)

        if compare("alex"):
            embed = embedImage("https://i.imgur.com/JDzXuSa.jpg", "alex man")
            await message.channel.send(embed=embed)

        if compare("jaishil"):
            embed = embedImage("https://i.imgur.com/hkseTHR.png", "ew")
            await message.channel.send(embed=embed)

        if compare("kahil") or compare("lil poop"):
            embed = embedImage("https://i.imgur.com/E3W8sLK.jpg", "oh yes")
            await message.channel.send(embed=embed)

        if compare("dylan"):
            embed = embedImage("https://i.imgur.com/jiTkP0x.jpg", "plane man")
            await message.channel.send(embed=embed)

        if compare("lizzo") or compare("cardi b") or compare("nicki minaj") or compare("megan thee stallion") or compare("travis scott") or compare("lil pump") or compare("lil uzi") or compare("lil xan") or compare("don toliver"):
            embed = embedImage("https://images-na.ssl-images-amazon.com/images/I/417CVAiSffL._AC_SY355_.jpg", "i only speak the truth")
            await message.channel.send(embed=embed)

        if compare("parth"):
            embed = embedImage("https://i.imgur.com/3KoUMsf.png", "very nice")
            await message.channel.send(embed=embed)

        if compare("abhi") or compare("abhinav"):
            embed = embedImage("https://i.imgur.com/Q3rR7b6.jpg", "giraffe")
            await message.channel.send(embed=embed)

        if compare("adam"):
            embed = embedImage("https://i.imgur.com/C2PDNDO.png", "FZ")
            await message.channel.send(embed=embed)

        if compare("mihir"):
            embed = embedImage("https://i.imgur.com/WmykdDd.jpg", "intelligent man")
            await message.channel.send(embed=embed)

        if compare("dj") or compare("dong jong"):
            embed = embedImage("https://i.imgur.com/mAuiKU2.jpg", "tall man")
            await message.channel.send(embed=embed)

        if compare("yeah yeah"):
            embed = embedImage("https://i.imgur.com/Uovs7CM.png", "yeah yeah")
            await message.channel.send(embed=embed)
            await message.channel.send("singing challenge", tts=True)

        if compare("no no"):
            embed = embedImage("https://i.imgur.com/J1mdv2G.png", "no no")
            await message.channel.send(embed=embed)
            await message.channel.send("jisl is a weenie", tts=True)

        if compare("among us"):
            embed = embedImage("https://i.imgur.com/dFz2mbY.png", "inside us hehe")
            await message.channel.send(embed=embed)

        if compare ("kanye") or compare("kanye west"):
            embed = embedImage("https://i.imgur.com/Qpgsg5G.png", "jesus or kanye????")
            await message.channel.send(embed=embed)

        if compare("pain"):
            embed = embedImage("https://i.imgur.com/npbWOQI.jpg", "pain")
            await message.channel.send(embed=embed)

        if compare("frick 12"):
            embed = embedImage("https://i.imgur.com/7O3fsZx.png", "frick 12")
            await message.channel.send(embed=embed)

        if compare("female") or compare("feminism"):
            embed = embedImage("https://i.imgur.com/OffhrKL.png", "females am i right")
            await message.channel.send(embed=embed)

        if compare("devlin"):
            embed = embedImage("https://i.imgur.com/MGEHbxB.jpg", "hot asian man")
            await message.channel.send(embed=embed)

        if compare("spatula"):
            embed = embedImage("https://i.imgur.com/SoHlbwn.jpg", "spatula")
            await message.channel.send(embed=embed)

        if compare("tarun"):
            embed = embedImage("https://i.imgur.com/fTbouWr.jpg", "hot glasses")
            await message.channel.send(embed=embed)






    if compare("plane gif"):
        nextNum = int(random.random() * len(planeGifUrls))
        while nextNum == lastNum:
            nextNum = int(random.random() * len(planeGifUrls))
        lastNum = nextNum
        embed = embedImage(planeGifUrls[nextNum], "plane gif")
        await message.channel.send(embed=embed)


    if checkCommand("-gay"):
        if message.mentions != []:
            user = message.mentions[0]

    if checkCommand("-d"):
        user = message.mentions[0]
        await user.edit(voice_channel=None)
        await message.channel.send(user.display_name + " has been disconnected by " + message.author.display_name)

    if checkCommand("play"):
        vc = message.author.voice
        client.join_voice_channel(vc)
        player = vc.create_ffmpeg_player('Recording(2).mp3', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await time.sleep(1)

#@client.event
#async def on_voice_state_update(member, before, after):
 #   if before.channel != after.channel:
  #      vcList = Guild.voice_channels











        


client.run(token)