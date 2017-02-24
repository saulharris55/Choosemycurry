from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen("http://www.indiacurry.com/Miscel/meatcurrylist.htm").read()

soup = BeautifulSoup(r,"lxml")
