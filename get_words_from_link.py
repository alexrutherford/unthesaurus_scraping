'''
Script to take a URL from UN thesaurus site and scrape translations and
ontology information.
TODO: run regex on string in each table element to allow for variable lengths
e.g. 'Scope' might be present in one but not all
Build dictionary of all keys such as 'used for','scope note','realted terms'
in all languages. Then don't assume each elements has same structure and
parse arbitrarily.
'''
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/bs4')
sys.path.append('/private/var/folders/8j/pq_2b12s5s13byqkqc0hhbyw0000gn/T/pip_build_alex/BeautifulSoup4/bs4')
sys.path.append('/usr/local/bin')
sys.path.append('/Library/Python/2.7/site-packages')
sys.path.append('/usr/local/lib/python2.7/site-packages')

import bs4,re 
from urllib2 import urlopen

#################
def getTerms(url='http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/fee3fb01c865ac5d85256cf400648b1f/0005b5294ea0c1ce85256aa000601fa9?OpenDocument'):
#################
    '''Give default URL for debugging'''
    html=urlopen(url).read()

    soup = bs4.BeautifulSoup(html, "lxml")

    tableBody=soup.body.form.table.tbody

    tables=soup.findAll('table')

# 0 Arabic 
# 1 Chinese
# 2 English
# 3 Arabic ontology
# 4 Chinese ontology
# 5 English ontology
# 6 French
# 7 Russian
# 8 Spanish
# 9 French ontology
# 10 Russian ontology
# 11 Spanish ontology
# Same number of panels repeated

    elements=soup.findAll(attrs={'width':'33%'})
    # Extract all table elements with text we want

    termsDict={}
    # Basic dictionary, English is key, value 
    # is list of translations into other languages

    if False:

        for ee,e in enumerate(elements):
            print ee,e.get_text().encode('utf-8')
            print ''
    # Print contents of each table element

    masterElement=elements[2].get_text()
    # Get English text
    englishKey=(masterElement.split('\n')[0]).lower()
    termsList=[]
    
#    print masterElement.split('\n')

    if True:
        for ee,e in enumerate(elements):
#            print e.get_text().encode('utf-8')
#            print '------'
            cleanedText=e.get_text().encode('utf-8').split(':')
            cleanedText=' '.join(cleanedText)
            cleanedText=cleanedText.split('\n')

            cleanedText[0]=re.split('[0-9]{2}\.[0-9]{2}\.[0-9]{2}',cleanedText[0],re.U)[0]
            # Clean first line: sometimes joined to second line
            # where related terms are referenced by index e.g. 08.01.00
            '''
            for t,tok in enumerate(cleanedText):
                print t,tok
            print ''
            '''
            if ee in [0,1,2,6,7,8]:
                termsList.append(cleanedText[0].lower())
            # Just grab table elements with translations

    if False:
        for k in termsList:
            print '\t',k

    return termsList
