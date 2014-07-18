'''
Wrapper script. Reads each link from terms_links.csv
and runs link through get_words_from_link.py
writes to file
'''
import csv,re,os,sys
from get_words_from_link import *

inFile=csv.reader(open('terms_links.csv','r'),delimiter='\t')

outFile=csv.writer(open('out.csv','w'),delimiter='\t')

for [term,link] in inFile:
    print term

    translated=getTerms(link)

    for t in translated:
        print t
    outFile.writerow(translated)
