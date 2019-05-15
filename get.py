import time, re, string, requests, urllib.request, re, json, codecs
from bs4 import BeautifulSoup

url = "https://mkcatering.se/dagens.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

FoodList = []
dagen = ""
z = 0

for x in range(2,7):
    item = soup.select('p')[x].getText().lstrip()
    fixed1 = re.sub(r'(?<=[a-z])(?=[A-Z])', ' & ', item)
    regex = re.compile(r'[\n\r\t]')
    fixed1 = regex.sub('', fixed1)
    FoodList.append(fixed1) 
    
outF = codecs.open("food.txt", "w", "utf-8")
for line in FoodList:
    z += 1
    if z == 1:
      dagen = "Måndag: "
    elif z == 2:
      dagen = "Tisdag: "
    elif z == 3:
      dagen = "Onsdag: "
    elif z == 4:
      dagen = "Torsdag: "
    elif z == 5:
      dagen = "Fredag: "
    else:
      dagen = "error - "
    outF.write(dagen+line)
    outF.write("\n")
outF.close()