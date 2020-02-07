import discord
import datetime
import pytesseract
from PIL import Image
from PIL import ImageFilter
from discord.ext import commands

token = "Token"
client = commands.Bot(command_prefix="!")
client = discord.Client()


#Reads all of the channel IDs into a List
def storedChannelIDs():
    idList = []
    with open ("channel ID.txt", "r") as file:
        for id in file:
            idList.append(int(id.strip()))
    return idList

#OCR Function 
def OCRImage():
    return "test"

#Import prompts Here
#Import prompts Here
#Import prompts Here


channelIDList = storedChannelIDs()
print("loaded")
print(channelIDList)

@client.event
async def on_message(message):
    if message.channel.id in channelIDList:
        print (message.attachments)
    

client.run(token,bot=True)