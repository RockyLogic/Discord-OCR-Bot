import io
import requests
import pytesseract
from PIL import Image
response = requests.get("https://cdn.discordapp.com/attachments/601402280691892226/694694467319365692/Screenshot_20200322-204546_Snapchat.jpg")
# print( type(response) ) # <class 'requests.models.Response'>
img = Image.open(io.BytesIO(response.content))
# print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
text = pytesseract.image_to_string(img)
print(text)
