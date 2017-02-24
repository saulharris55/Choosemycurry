import BeautifulSoup

from BeautifulSoup import BeautifulSoup

import urllib2

url = irllib2.urlopen(www.indiacurry.com/Miscel/meatcurrylist.htm)

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("hot")