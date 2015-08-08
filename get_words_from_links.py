'''
Wrapper script. Reads each link from terms_links.csv
and runs link through get_words_from_link.py
writes to file
'''
import csv,re,os,sys
from get_words_from_link import *

import logging
logger=logging.getLogger()
logging.basicConfig(filename='./log.log',level=logging.WARNING)

inFile=csv.reader(open('terms_links.csv','r'),delimiter='\t')

outFile=csv.writer(open('out.csv','w'),delimiter='\t')

n=0

if os.path.isfile('ontology_terms.txt'):
    os.remove('ontology_terms.txt')

for [term,link] in inFile:
    if n%100==0:logging.warning('Term #%d' % n)
    logging.info(term)

    translated=getTerms(link,term)

    if translated:
        for t in translated:
            logging.info(t)
        outFile.writerow(translated)
    else:
        logging.warning('URL error: Skipping %s' % term)
    n+=1
