import os
import argparse
import time
import requests
from bs4 import BeautifulSoup

# Arguments happen. Don't let it get you down! 
parser = argparse.ArgumentParser(description='Hope you\'re having a good day!')
parser.add_argument('-d','--debug', action='store_true', default=False)
parser.add_argument('-n','--new', action='store_true', default=False)
args = parser.parse_args()

# Some times you needs some constants in life
URL = 'https://www.enchantedlearning.com/wordlist/positivewords.shtml'
DEBUG = args.debug
NEW_VIBES = args.new
VIBES = '../data/positive-vibes.csv'
VIBES_EXIST = os.path.exists(VIBES) 

# Check for those vibes because you know sometimes they be hiding
if not os.path.exists('../data'):
        os.mkdir('../data')
if VIBES_EXIST and not NEW_VIBES:
    if os.stat(VIBES).st_size > 1:
        print('I got you')
        time.sleep(1)
        with open('positive-vibes.txt', 'r') as f:
            print(f.read())
        exit()
    print('You got vibes, but they empty...')
elif NEW_VIBES:
    print("sometimes we need some NEW VIBES!")
    time.sleep(1)

# Get that Positivity <3
page = requests.get(URL)

# Make those V I B E S shine
soup = BeautifulSoup(page.content, 'html.parser')

# (っ◔◡◔)っ ♥ sharing is caring ♥
results = soup.find_all('div', class_='wordlist-item')

# [DEBUG] Check yourself
if DEBUG:
    for r in results:
        print(r.text)

# Save those vibes for later
with open(VIBES, 'w+') as f:
    for r in results:
        f.write(r.text + ',')

# ~~~Check your vibes~~~
with open(VIBES, 'r') as f:
    print(f.read())
    

