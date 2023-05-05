import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import math

chapters = list(range(1,22))
chapter = random.choice(chapters)
if chapter < 10:
    chapter = '0' + str(chapter)
else:
    chapter = str(chapter)

url = 'https://ebible.org/asv/JHN' + chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser') # a pasrser is a way to separate data, parses according to the html tags


print(soup.title.text)

verses_list = soup.findAll('div', class_= "p")

verse_list = [v.text.split('.')for v in verses_list]
print()
my_choice = random.choice(random.choice(verse_list))
verse = f'Chapter: {chapter} Verse: {my_choice}'
print(verse)
print()

import keys 
from twilio.rest import Client

client = Client(keys.accountSID, keys.auth_token)

TwilioNumber = "+15074605741"

mycellphone = "+12145194721"


textmessage = client.messages.create(to=mycellphone, from_= TwilioNumber,body= verse)


print(textmessage.status)

#call = client.calls.create(url ="https://demo.twilio.com/docs/voice.xml", to=mycellphone, from_= TwilioNumber)