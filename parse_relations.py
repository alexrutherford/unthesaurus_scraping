# -*- coding: utf-8 -*-
'''
Script to parse ontology_terms.csv: the output of get_words_from_link.py
This relates each term in each language to other terms through relations such
as 'Broader terms', 'Related terms'
'''

import csv,re,json
import collections

import logging
logger=logging.getLogger()
logging.basicConfig(filename='./log.log',level=logging.WARNING)

relationsHash={}
relationsHash['EN']={}
relationsHash['AR']={}
relationsHash['CN']={}
relationsHash['ES']={}
relationsHash['FR']={}
relationsHash['RU']={}
# This stores the full set of relations between terms in each language

relationsFile=csv.reader(open('relations.csv','r'),delimiter=',')
relationsDict=collections.defaultdict(list)
###########################################
for line in relationsFile:
    relationsDict[line[0].decode('utf-8')]=[l.decode('utf-8') for l in line[1:]]
    # These are ontology terms in each language to be searched for
    # Key={'Broader terms','Related terms','Top terms','Narrower terms'}
    # Value=[translationES,translationRU,translationAR,translationCN,translationFR]
###########################################
termsFile=csv.reader(open('out.csv','r'),delimiter='\t')
termsDict={}

for line in termsFile:
    termsDict[line[2]]=line[0:2]
    termsDict[line[2]].extend(line[3:]+[line[2]])
    # Dictionary of each term in thesaurus, Key is English term, value is list of translations [AR,CN,FR,RU,FR,EN]
    # e.g. termsDict['electronic publications']=['لمنشورات الإلكترونية','电子出版物','publications electroniques'
    # 'Электронные издания','publicaciones electronicas','electronic publications']
logging.info('Finised reading input files')
###########################################
def translateRelation(relation,lang,originalTerm,text,langN):
    '''
    Function to take an ontology relation in one language, finds the corresponding English
    i.e. Finds 'Related terms' from 'Términos relacionados'
    Commits the relation to relationsHash
    '''
    relation=re.sub(':','',relation,re.U)
    # Clean out comma

    for k,v in relationsDict.items():
        if relation in [k]+v:
            # First level is language
            # Second is the original term in language
            # Third is EN translation of relationship
            # Value is the synonmy itself
            relationsHash[lang][termsDict[originalTerm.lower()][langN]][k].append(text)
            return k
###########################################
def parseOntology(text,lang,originalTerm):
    '''
    Parses each line in ontology_terms.csv
    Each line represents all ontology relations and terms
    for a given term in a given language
    '''
    logging.debug('Parsed:')
    parts=text.split('\n')[1:]
    langN=['AR','CN','FR','RU','ES','EN'].index(lang)
    relationsHash[lang][termsDict[originalTerm.lower()][langN]]=collections.defaultdict(list)

    for n,p in enumerate(parts):
        # Throw out first line =>'Term Relationships'

        if re.search(':',p):
            # Find an ontology relation signified by a comma

            while n+1<len(parts) and not re.search(':',parts[n+1]):
                # Then keep parsing the terms that follow until another relation is found (comma)
                logging.debug('\t=>',translateRelation(p.decode('utf-8'),lang,originalTerm,parts[n+1],langN))
                n+=1
            n+=1
###########################################
def main():

    ontologiesFile=csv.reader(open('ontology_terms.txt','r'),delimiter='\t')

    nLine=0

    for line in ontologiesFile:
        logging.warning('LINE %d:' %(nLine))

        #for n,part in enumerate(line):
        #    print '\t',n,part

        if re.search(r'\*\*\*TERM',line[0]):
            term=line[0].partition(' ')[2]
        elif re.search(r'ontology',line[0]):
            nextLine=ontologiesFile.next()
            lang=re.sub('\*','',nextLine[0])
            logging.debug('Lang %s' % lang)
            logging.debug('Ontology %s' % nextLine[1])
            if term.lower() in termsDict.keys():
                # Some terms not in the dictionary
                parseOntology(nextLine[1],lang,term)

    with open('ontology.json','w') as jsonFile:
        json.dump(relationsHash,jsonFile)
if __name__=="__main__":
    main()
