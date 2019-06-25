
import requests
#import MySQLdb
from bs4 import BeautifulSoup

#URL to be scraped
url_to_scrape = 'http://www.google.com/'

#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)

#checking whether the website is accessible or not
print(plain_html_text.status_code)

#Checking the HTTP headers of the website
print(plain_html_text.headers)

# Storing the page content into a variable
page_content = plain_html_text.content

# Print page_content
#print(page_content)


#parse the data
soup = BeautifulSoup(plain_html_text.text, "html.parser")

# Getting all of the links in the page and storing it into links variable
links_in_the_page = soup.find_all("a")

print(links_in_the_page)
print("\n")

#What if, we want only those links which contains the text "About"
for link in links_in_the_page:
	if "About" in link.text:
		print(link)
		print(link.attrs['href'])