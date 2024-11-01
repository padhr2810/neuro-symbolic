

"""
Web scraping tool for Wicklow County Council.

https://www.geeksforgeeks.org/downloading-pdfs-with-python-using-requests-and-beautifulsoup/

https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d

Avoid detection like a ninja: 
https://www.zenrows.com/blog/stealth-web-scraping-in-python-avoid-blocking-like-a-ninja

https://www.zenrows.com/blog/robots-txt-web-scraping 

https://www.reddit.com/r/learnpython/comments/zhuh39/help_with_first_bs4_project/ 
"""

"""
HOW TO GET PDF DOWNLOADED: 
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
 
# Find all hyperlinks present on webpage
links = soup.find_all('a')
 
i = 0
 
# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
 
        # Get response object for link
        response = requests.get(link.get('href'))
 
        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
 
print("All PDF files downloaded")
"""

import os 

from bs4 import BeautifulSoup
import requests 

os.environ["http_proxy"] = "http://proxy.emea.etn.com:8080" 
os.environ["https_proxy"] = "http://proxy.emea.etn.com:8080" 

"""
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
"""

the_headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


wicklow_url = "https://www.wicklow.ie/Living/Services/Planning/Planning-Applications/Weekly-Planning-Lists/Weekly-Planning-Lists-2023"

session = requests.Session()
response = session.get(wicklow_url, headers=the_headers)
print(f"response = {response}") 

html_soup = BeautifulSoup(response.text, 'html.parser')
print(f"html_soup  =  {html_soup }")
