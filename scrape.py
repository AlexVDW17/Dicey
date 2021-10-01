#want to scrape the data from the website
#import the libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import requests

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
#set the url
url = 'https://magicalscrolls.com/'


html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup.prettify()) # print the parsed data of html
print(soup.title) # print the title of the website

#get the h1 headers tagged with id matching the pattern spellnameX
headers = soup.find_all('h1', id=lambda x: x and x.startswith('spellname'))
#now we need to take the text from the headers
spell_names = [header.text for header in headers]
#we want to remove TM from the spell names
spell_names = [spell_name.replace('TM', '') for spell_name in spell_names]

#for each spell name, we want to get the spell description.
#each spell description has the class spelltext and the id matching the pattern spelltextX
#where X is the same as in spellnameX
headers = soup.find_all('div', class_='spelltext')
spell_descriptions = [header.text for header in headers]

#print(spell_descriptions)
#now we want to associate the spell names with the spell details
spell_dict = dict(zip(spell_names, spell_descriptions))

#now we want to create a dataframe with the spell names and spell descriptions
spell_df = pd.DataFrame(spell_dict.items(), columns=['Spell Name', 'Spell Description'])
#now we store the dataframe in a csv file
spell_df.to_csv('spell_data.csv', index=False)
