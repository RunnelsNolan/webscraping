
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


url = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser') # a pasrser is a way to separate data, parses according to the html tags

print(soup.title.text)

myclasses =['MW 1:00 p.m.', 'MW 2:30 p.m', 'TR 8:00 a.m.']

finals_rows = soup.findAll('tr') #will loop through both tables


for row in finals_rows:
    final = row.findAll('td')
    if final: #says if final is not null
        myclass = final[0].text
        if myclass in myclasses:
            print(f'For class {myclass} the final is scheduled for {final[1].text} at {final[2].text}')

#if you wanted to isolate just the 2nd table
#all_tables = soup.findall('tables)
#course_table = all_tables[1]