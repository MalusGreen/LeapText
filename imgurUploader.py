import pyimgur
import requests

#CLIENT_ID = "d5e44e95a75c648"
#PATH = "C:\Users\Sakeeb\Documents\Development\TheRealSurface\hello.png"

#im = pyimgur.Imgur(CLIENT_ID)
#uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
#print(uploaded_image.title)
#print(uploaded_image.link)

def uploadImage(path):
    CLIENT_ID = "d5e44e95a75c648"  #my account's key, found on https://imgur.com/account/settings/apps
    PATH = path
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur") 
    
    print(uploaded_image.link)
    #Sends the request
    url = 'http://localhost:3000'
    response = requests.post(url, data = {'imgurLink':uploaded_image.link})

 
#test image on my computer 
path = "C:\Users\Sakeeb\Documents\Development\TheRealSurface\hello.png"  
uploadImage(path)