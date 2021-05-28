import argparse
import os
import json
import re
import requests
from bs4 import BeautifulSoup


# argparser 
parser = argparse.ArgumentParser(description='Hope you\'re having a good day!')
parser.add_argument('-d','--debug', action='store_true', default=False)
parser.add_argument('-n','--new', action='store_true', default=False)
args = parser.parse_args()

# CONSTANTS
CWD = os.getcwd()
DEBUG = args.debug
NEW_FILE = args.new
PAT = r'\d+\.'
URL  = 'https://www.workflowmax.com/blog/101-engineering-quotes-from-the-minds-of-innovators'
FILE_NAME = "engineering_quotes.json"
SAVE_DIR = "../data/" if CWD.endswith("python") else "./data/" 
SAVE_PATH = SAVE_DIR + FILE_NAME

# Check for SAVE_DIR and create if not found
print(f"Searching for \"{SAVE_DIR}\"")
if not os.path.exists(SAVE_DIR):
    print(f"Creating \"{SAVE_DIR}\"")
    os.mkdir(SAVE_DIR)
print(f"SAVE_PATH : \"{SAVE_PATH}\"\nReady to gather data!")


# Get and parse URL
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results =  soup.find_all('p')
print(f"Successfully received data from \"{URL}\"")

# Clean data from URL
print(f"Preparing data to be saved...")
quotes = []
id = 0
for i in range(len(results)):
    mat = re.match(PAT,results[i].text)
    if mat is not None:
        id += 1
        temp = results[i].text.replace(mat.group() + " ", "").\
            replace("”", '"').replace("“", '"').replace(".-", '"-').\
            replace("’","'").replace("…","...").replace("—","--").\
            replace("‘","'").replace("\u00a0"," ").split('"-')
        temp[0] = temp[0].replace("\"", "")
        if temp[1].startswith(" "):
            temp[1] = temp[1].replace(" ", "", 1)
        quotes.append({"id":id,"author":temp[1],"quote":temp[0]})
print("Data sanitized!")

# [DEBUG]
if DEBUG:
    for q in quotes:
        print(f"id: {q['id']}.\t{q['quote']} \nby, {q['author']}")

# Save data to FILE_NAME
print(f"Saving data to \"{SAVE_PATH}\"")
with open(SAVE_PATH,'w') as out:
    json.dump(quotes, out)
print("Data Saved!")
