from bs4 import BeautifulSoup
from urllib2 import urlopen

# http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/BrowseEng?OpenView&StartKey=b&Count=100000

BASE_URL = "http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/BrowseEng?OpenView&StartKey=a&Count=100000"

html = urlopen(section_url).read()
soup = BeautifulSoup(html, "lxml")



