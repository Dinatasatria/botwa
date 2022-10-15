import requests,sys,shlex
ᴀʀᴛᴀ sᴀᴛʀɪᴀᴅɪ = " ".join(map(shlex.quote, sys.argv[2:]))
bahasa = sys.argv[1];
params = {
    'p1': 'auto',
    'p2': bahasa,
    'p3': ᴀʀᴛᴀ sᴀᴛʀɪᴀᴅɪ,
}

response = requests.get('https://t24.freetranslations.org/freetranslationsorg.php', params=params).text
#a = response.split('"text":"')[1];
#b = a.split('"')[0];
print (f"""{response}

_© ᴀʀᴛᴀ sᴀᴛʀɪᴀᴅɪ ~ Multi Device 2022_
""")
