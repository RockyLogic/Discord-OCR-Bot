import io
import discord
import datetime
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from discord.ext import commands


client = commands.Bot(command_prefix="!")
client = discord.Client()


#Grabbing List of Channel IDs
def storedChannelIDs():
    idList = []
    with open ("channel ID.txt", "r") as file:
        for id in file:
            idList.append(int(id.strip()))
    return idList

#Grabbing Token
def getToken():
    with open ("token.txt","r") as file:
        token = file.readLine()
        return token
    
#OCR Function 
def OCRImage(imageLink):
    response = requests.get(imageLink)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    print(text)


channelIDList = storedChannelIDs()
print("loaded")
print(channelIDList)

@client.event
async def on_message(message):
    if message.channel.id in channelIDList:
        print (message.attachments)
    

client.run(token,bot=True)