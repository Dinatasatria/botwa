import instaloader as perdigay
import shlex
import sys
import requests
import os
import time
Arta_Botz = " ".join(map(shlex.quote, sys.argv[1:]))
kontol = perdigay.Instaloader()
profile = perdigay.Profile.from_username(kontol.context, mr_dark)
params = {
    'tkn': '125',
    'd': '3000',
    'u': f'https://gramhir.com/profile/{ᴀʀᴛᴀ sᴀᴛʀɪᴀᴅɪ}/{profile.userid}',
    'fs': '0',
    'w': '1280',
    'h': '1280',
    's': '100',
    'z': '100',
    'f': 'jpg',
    'rt': 'jweb',
}
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)
print ("_© ᴀʀᴛᴀ sᴀᴛʀɪᴀᴅɪ ~ MultiDevice 2022_")
#os.system("rm ssweb.jpg")
#response = requests.get('https://api.pikwy.com/', params=params).text
#a = response.split('"iurl":"')[1];
#b = a.split('"')[0];
#print ('url screenshot: '+b)
#response = requests.get(b)
#with open("ssweb.jpg", "w") as f:
#    f.write(response.text)
