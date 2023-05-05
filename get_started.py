from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

webpage = 'https://www.boxofficemojo.com/year/2023/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

wb = xl.Workbook()
ws = wb.active
ws['A1'] = 'Test'

wb.save("Crypto_Gainers.xlsx")