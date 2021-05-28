import os
from re import findall
import re
import requests
from bs4 import BeautifulSoup

pat = r'\d+\.'
URL = 'https://www.workflowmax.com/blog/101-engineering-quotes-from-the-minds-of-innovators'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results =  soup.find_all('p')

quotes = []
for i in range(len(results)):
    mat = re.match(pat,results[i].text)
    if mat is not None:
        print(f'{results[i].text}')
        # quotes.append(results[i].text.replace(mat.group() + " ","").\
        #     replace("”","\"").replace("“","\"").replace("\"-","\"\n-"))
        temp = results[i].text.replace(mat.group() + " ","").\
            replace("”","\"").replace("“","\"").replace(".-","\"-").split("\"-")
        temp[0].join("\"")    
        print(temp)
        quotes.append((temp[0],temp[1]))    
for i in range(len(quotes)):
    print(f"{quotes[i][0]} \n by, {quotes[i][1]}")