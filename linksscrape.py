
from bs4 import BeautifulSoup
import requests
 
url = "https://www.google.com/search?client=safari&rls=en&q=1550+wewatta&ie=UTF-8&oe=UTF-8"
 
# Getting the webpage, creating a Response object.
response = requests.get(url)
 
# Extracting the source code of the page.
data = response.text
 
# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')
 
# Extracting all the <a> tags into a list.
tags = soup.find_all('a')
 
# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
    print(tag.get('href'))
