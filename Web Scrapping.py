import requests
from bs4 import BeautifulSoup
import os

# URL of NIRF ranking webpage
url = 'https://www.nirfindia.org/2022/UniversityRanking.html'

# Send a request to the webpage
page = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find all links on the webpage
links = soup.find_all('a')

# Loop through all links
i = 1
for link in links:
    href = link.get('href')
    if href and href.endswith('.pdf'):
        # Download the PDF file
        filename = str(i).zfill(3) + os.path.basename(href)
        with open(filename, 'wb') as file:
            response = requests.get(href)
            file.write(response.content)
            print(f'{filename} downloaded successfully.')
            i += 1
            if i > 100:
                break
