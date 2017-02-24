import bs4 as BeautifulSoup
import urllib

# url = urllib2.urlopen('http://www.indiacurry.com/Miscel/meatcurrylist.htm')
# content = url.read()
# soup = BeautifulSoup(content)
# tables = soup.find_all("table")
# print tables

from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.indiacurry.com/Miscel/meatcurrylist.htm').read()
soup = BeautifulSoup(r,"lxml")

tables = soup.find_all("table")

names = tables[3].find_all("tr")
print names[0:3]

# print soup.prettify()[:]

# links = soup.findAll("hot")