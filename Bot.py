
import discord
import aiohttp
import random
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


tokenFile = open("token.txt", "r")
tokenList = tokenFile.readlines()
token = "";
for x in tokenList:
    token += x[0]
id = 703700230251610172
client = discord.Client()
lastNum = 0
wantPics = True
nokahil = True

cannotClearFile = open("cannotclear.txt", "r")
lines = cannotClearFile.read().split("|")
cannotClear = {}
for i in range(0, len(lines) - 1, 2):
    cannotClear.update({lines[i] : lines[i + 1]})

output = []
test = {"kahil" : "gay", "mihir" : "not gay", "cannotclear" : {"smiley" : "no", "shrek" : "yes", "fatlips" : "pooppoo"}}
for i in range(3):
    output.append(test)

jobj = json.dumps(output, indent = 4)
with open("serverinfo.json", "w") as outfile:
    outfile.write(jobj)

with open("serverinfo.json", "r") as openfile:
    obj = json.load(openfile)
    print(obj)

print(cannotClear)
canChangeClear = ["SmileyFace21"]

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
    global lastNum, id, wantPics, nokahil
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

    def getStringDict(dict):
        list = dict.items()
        string = ""
        for entry in list:
            string += entry[0] + "|" + entry[1] + "|"
        return string

    def checkExist(name, guild):
        exists = False
        people = guild.members
        for person in people:
            if person.name == name:
                exists = True

        return exists

    def sendtt(title, text):
        embed = discord.Embed(title=title, description=text, color=discord.Color.dark_magenta())
        return embed

    def sendt(title):
        embed = discord.Embed(title=title, color=discord.Color.dark_magenta())
        return embed

    def sendttt(title, text, tn):
        embed = discord.Embed(title=title, descriptiom=text, color=discord.Color.dark_magenta())
        embed.set_thumbnail(tn)
        return embed

    def getImgurLink(link):
        PATH = ".\\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(link)
        image = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div[1]/div[1]/div[2]/div[1]/a/img")
        image.click()
        time.sleep(1)
        image2 = driver.find_element_by_class_name("image-placeholder")
        image2.click()
        image3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div/img")
        link = image3.get_attribute("src")
        return link

    if checkCommand("-search"):
        if len(getCommand(True)) > 1:
            arr = getCommand(True)
            link = "https://imgur.com/search/score?q="
            for word in range(0, len(arr) - 1):
                link += word + "+"
            link+= arr[len(arr) - 1]
            await message.channel.send(getImgurLink(link))
        else:
            link = "https://imgur.com/search/score?q=" + getCommand(False)
            await message.channel.send(getImgurLink(link))





    if compare("jaishil is gay"):
        await message.channel.send(embed=sendtt("who is gay?", "jaishil shah is"))

    if checkCommand("-s"):
        status = "Pictures On: " + str(wantPics)
        await message.channel.send(embed=sendtt(status, "Jisl: Is still gay"))


    elif compare("my balls itch") or compare("mbi"):
        await message.channel.send(embed=sendt("same bro"))

    elif compare("i'm gay") or compare("im gay"):
        await message.channel.send(embed=sendt("I agree, " + message.author.display_name + " is gay"))

    elif compare("i love mihir"):
        embed = embedImage("https://cdn.pixabay.com/photo/2016/10/04/16/33/heart-shape-1714807_960_720.jpg", "Why Thank You")
        await message.channel.send(embed=embed)

    elif compare("dylan is plane"):
        await message.channel.send(embed=sendt("plane sex"))


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

    if checkCommand("-noclear"):
        getStringDict(cannotClear)
        if canChangeClear.count(message.author.name) > 0:
            command = getCommand(True)
            sendback = ""
            for i in range(1, len(command)):
                sendback += command[i] + " "
            name = command[0]
            exists = checkExist(name, message.guild)
            if exists:
                cannotClear.update({name : sendback})
                file = open("cannotclear.txt", "w")
                file.write(getStringDict(cannotClear))
                await message.channel.send(embed=sendt("clearing capabilites are updated for " + name))

            else:
                await message.channel.send \
                    (embed=sendtt("this user does not exist", "please enter their username, not their display name"))
        else:
            await message.channel.send("you do not have permission do make this change", "please ask the administrator to make this change", "https://i.pinimg.com/originals/af/2d/fd/af2dfd726ed01af133fcaf3e4707ebdf.png")

    if checkCommand("-canclear"):
        if canChangeClear.count(message.author.name) > 0:
            name = getCommand(True)[0]
            exists = checkExist(name, message.guild)
            if exists:
                    exists = True
                    cannotClear.pop(name)
                    file = open("cannotclear.txt", "w")
                    file.write(getStringDict(cannotClear))
                    await message.channel.send(embed=sendt("this change has been successfully made"))

            if exists == False:
                await message.channel.send(embed=sendttt("this user does not exist", "make sure you are typing their username, not their display name", "https://i.pinimg.com/originals/af/2d/fd/af2dfd726ed01af133fcaf3e4707ebdf.png"))
        else:
            await message.channel.send(embed=sendttt("you do not have permission to make this change", "please as an administrator to make this change", "https://i.pinimg.com/originals/af/2d/fd/af2dfd726ed01af133fcaf3e4707ebdf.png"))




    if checkCommand("-nokahil"):
        if message.author.name != "shrek":
            if nokahil == True:
                nokahil = False
            else:
                nokahil = True







    if checkCommand("-h"):
        await message.channel.send \
            ("-h: help\n-d: disconnects the mentioned person\n-n: (nickname) changes your nickname or the nickname of the person you mentioned\n-s: tells you status\nclear: (number < 50): deletes the number of messages you specified but excludes pinned messages\npclear: (number < 50): deletes the number of messages you specified including pinned messages")

    if checkCommand("clear"):
        print(cannotClear)
        noClear = cannotClear.keys()
        canClear = True
        for key in noClear:
            if key == message.author.name:
                canClear = False
                await message.channel.send(cannotClear.get(key))

        if canClear:

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

    if checkCommand("-whoclear"):
        stringg = ""
        people = getStringDict(cannotClear)
        peopleList = people.split("|")
        for i in range(0, len(peopleList) - 1, 2):
            stringg += peopleList[i] + ": " + peopleList[ i +1] + "\n"

        await message.channel.send(stringg)


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

        if compare("lizzo") or compare("cardi b") or compare("nicki minaj") or compare \
                ("megan thee stallion") or compare("travis scott") or compare("lil pump") or compare \
                ("lil uzi") or compare("lil xan") or compare("don toliver"):
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


    if compare("mihir is gay"):
        if message.author.dm_channel == None:
            await message.author.create_dm()
            print("yes")
        await message.author.dm_channel.send \
            (embed=sendtt("I will literally murder you", "don't ever speak of my dad like that again"))
        print(message.author.dm_channel)




# @client.event
# async def on_voice_state_update(member, before, after):
 #   if nokahil and member.name == "fatlips":
  #      await member.edit(voice_channel=None)












        


client.run(token
)