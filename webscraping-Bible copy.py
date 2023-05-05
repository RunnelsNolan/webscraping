import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



url = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser') # a pasrser is a way to separate data, parses according to the html tags


print(soup.title.text)
table_rows = soup.find_all("div")
#print(table_rows)

verses_list = soup.findAll("p", class_= "reg") #gets versus untill next section of verses

#for verse in verses_list:
    #print(verse.text)

verse_list = [v.text.split('.')for v in verses_list] # splitting each verse based on a period
#print(verse_list)

print(random.choice(random.choice(verse_list))) # gives a SINGLE random verse from a cluster of seperated verses
