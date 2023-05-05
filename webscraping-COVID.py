# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"pip3 install bs4




url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser') # a pasrser is a way to separate data, parses according to the html tags

print(soup.title.text)

#TR tage - row within a table
#TD tag - within a TR tag has this for each colum

table_rows = soup.find_all("tr") #uses table rows dicted by their tr tag

#print(table_rows[2:20]) #start on 3rd row up to 20 elements, technically starts at 3rd TR tag
#^comes out as a lost, and each elemnt represents a row

state_death_ratio = ""
state_best_testing = ""
state_worst_testing = ""
high_death_ratio = 0.0
high_test_ratio = 0.0
low_test_ratio = 100.0
for row in table_rows[2:52]:
    td = row.findAll("td") # goes through each row and find each TD tag
    state = td[1].text #pull second TD tag and will only give you text stuff
    
    #cant just convert the numbers because of the comma, must replace it!
    
    total_cases = int(td[2].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    total_tested = int(td[10].text.replace(",",""))
    total_population = int(td[12].text.replace(",",""))
    
    death_ratio = total_deaths/total_cases
    test_ratio = total_tested/total_population

    if death_ratio > high_death_ratio:
        state_death_ratio = state
        high_death_ratio = death_ratio

    if test_ratio > high_death_ratio:
        state_best_testing = state
        high_test_ratio = test_ratio

    if test_ratio < low_test_ratio:
        state_worst_testing = state
        low_test_ratio = test_ratio

print("State with highest death ratio is:", state_death_ratio)
print("Death Ratio:", format(high_death_ratio, ".2%"))
print()
print("State with best testing ratio:", state_best_testing)
print("Test Ratio:", format(low_test_ratio,".2%" ))
print()
print("State with worst testing ratio:", state_worst_testing)
print("Test Ratio:", format(high_test_ratio,".2%" ))



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

