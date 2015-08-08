'''
Script to take a URL from UN thesaurus site and scrape translations and
ontology information.
'''
import sys,csv
sys.path.append('/usr/local/lib/python2.7/site-packages/bs4')
sys.path.append('/private/var/folders/8j/pq_2b12s5s13byqkqc0hhbyw0000gn/T/pip_build_alex/BeautifulSoup4/bs4')
sys.path.append('/usr/local/bin')
sys.path.append('/Library/Python/2.7/site-packages')
sys.path.append('/usr/local/lib/python2.7/site-packages')

import bs4,re
from urllib2 import urlopen

import logging
logger=logging.getLogger()
logging.basicConfig(filename='./log.log',level=logging.WARNING)

#################
def getTerms(url='http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/fee3fb01c865ac5d85256cf400648b1f/0005b5294ea0c1ce85256aa000601fa9?OpenDocument',term=''):
#################
    '''Give default URL for debugging'''
    try:
        html=urlopen(url).read()
    except:
        logging.warning('URL ERROR %s' %url)
        return None

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
            logging.info(ee,e.get_text().encode('utf-8'))
            loging.info('')
    # Print contents of each table element

    masterElement=elements[2].get_text()
    # Get English text
    englishKey=(masterElement.split('\n')[0]).lower()
    termsList=[]

    tempFile=csv.writer(open('ontology_terms.txt','a'),delimiter='\t')
    # This stores all the lines representing ontology relations

    if len(elements)==12:
    # Check all languages are there
        for ee,e in enumerate(elements):

            cleanedText=e.get_text().encode('utf-8').split(':')
            cleanedText=' '.join(cleanedText)
            cleanedText=cleanedText.split('\n')

            cleanedText[0]=re.split('[0-9]{2}\.[0-9]{2}\.[0-9]{2}',cleanedText[0],re.U)[0]
            # Clean first line: sometimes joined to second line
            # where related terms are referenced by index e.g. 08.01.00

            if ee in [0,1,2,6,7,8]:
                termsList.append(cleanedText[0].lower())
            # Just grab table elements with translations
            tempFile.writerow(['***TERM %s' % term])
            tempFile.writerow(['***AR ontology'])
            tempFile.writerow([u'***AR',elements[3].get_text().encode('utf-8')])
            tempFile.writerow(['***CN ontology'])
            tempFile.writerow(['***CN',elements[4].get_text().encode('utf-8')])
            tempFile.writerow(['***FR ontology'])
            tempFile.writerow(['***FR',elements[9].get_text().encode('utf-8')])
            tempFile.writerow(['***RU ontology'])
            tempFile.writerow(['***RU',elements[10].get_text().encode('utf-8')])
            tempFile.writerow(['***ES ontology'])
            tempFile.writerow(['***ES',elements[11].get_text().encode('utf-8')])
            tempFile.writerow(['***EN ontology'])
            tempFile.writerow(['***EN',elements[5].get_text().encode('utf-8')])
    else:
        logging.warning('Term %s only has %d elements' % (elements[2].get_text(),len(elements)))

    return termsList
