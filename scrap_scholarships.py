import requests
import math
#from openpyxl import Workbook
from bs4 import BeautifulSoup as bs
import regex as re
from selenium import webdriver
from selenium.webdriver.chrome.options import (Options)
from database import db,Hackathons


# URL of the NSP portal
url = "https://www.india.gov.in/gsearch?s=engineering+scholarships&op=Search&as_fid=fae3a6e748cb3f7ba85e959ce9de2c552c99d98a"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page!")
    
    # Parse the page content
    soup = bs(response.content, 'html.parser')
    
    # Now, let's extract data based on tags or classes (you may need to inspect the website structure)
    
    # Example: Extracting all links from the page
    links = soup.find_all('a')  # Find all 'a' tags (hyperlinks)
    
    divs = soup.find_all('div',class_ = 'gsc-webResult_gsc-result')
    for link in links:
        href = link.get('href')
         # If the href attribute exists, print it
            
    
    # Example: Extracting a specific section (e.g., all paragraphs within a class 'content')
     # Replace 'content' with the actual class or tag you're targeting
    for div in divs:
        print(div.prettify())  # Extract text from the paragraph
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
