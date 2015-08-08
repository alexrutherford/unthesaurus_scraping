import csv,re
import collections

relationsHash={}
'''
relationsHash['EN']=collections.defaultdict(collections.defaultdict(list))
relationsHash['AR']=collections.defaultdict(collections.defaultdict(list))
relationsHash['CN']=collections.defaultdict(collections.defaultdict(list))
relationsHash['ES']=collections.defaultdict(collections.defaultdict(list))
relationsHash['FR']=collections.defaultdict(collections.defaultdict(list))
relationsHash['RU']=collections.defaultdict(collections.defaultdict(list))
'''
relationsHash['EN']={}
relationsHash['AR']={}
relationsHash['CN']={}
relationsHash['ES']={}
relationsHash['FR']={}
relationsHash['RU']={}

relationsFile=csv.reader(open('relations.csv','r'),delimiter=',')
relationsDict=collections.defaultdict(list)
###########################################
for line in relationsFile:
#    relationsDict[line[0]]=[l.decode('utf-8') for l in line[1:]]
    relationsDict[line[0].decode('utf-8')]=[l.decode('utf-8') for l in line[1:]]
###########################################
termsFile=csv.reader(open('out.csv','r'),delimiter='\t')
termsDict={}

for line in termsFile:
    termsDict[line[2]]=line[0:2]
    termsDict[line[2]].extend(line[3:]+[line[2]])

###########################################
def translateRelation(relation,lang,originalTerm,text,langN):
    relation=re.sub(':','',relation,re.U)

    for k,v in relationsDict.items():
        if relation in [k]+v:
            # First level is labguage
            # Second is the original term in language
            # Third is EN translation of relationship
            # Value is the synonmy itself
            relationsHash[lang][termsDict[originalTerm.lower()][langN]][k].append(text)
            return k
        '''
        print 'IS %s in %s?' % (relation,v)
        for word in [k]+v:
            print '>>%s<<==>>%s<<' % (relation,word)
            print repr(relation),repr(word)
            print type(relation),type(word)
            if relation==word:
                return k
        '''
###########################################
def parseOntology(text,lang,originalTerm):
    print 'Parsed:'
    parts=text.split('\n')[1:]
    langN=['AR','CN','FR','RU','ES','EN'].index(lang)
    relationsHash[lang][termsDict[originalTerm.lower()][langN]]=collections.defaultdict(list)

    for n,p in enumerate(parts):
        # Throw out first line =>'Term Relationships'
#        print '\t',p

        if re.search(':',p):
#            print '\tRELATION',p,langN,originalTerm,termsDict[originalTerm.lower()]
#            if n+1<len(parts):
                # If there are no terms for that relation

            while n+1<len(parts) and not re.search(':',parts[n+1]):
                print '\tWORD',p
                print '\t=>',translateRelation(p.decode('utf-8'),lang,originalTerm,parts[n+1],langN)
                n+=1
            n+=1
###########################################
def main():

    # Key=>EN
    # Value=>
    # 0 AR
    # 1 CN
    # 2 FR
    # 3 RU
    # 4 ES

    ontologiesFile=csv.reader(open('ontology_terms.txt','r'),delimiter='\t')

    nLine=0

    for line in ontologiesFile:
        print 'LINE %d:' %(nLine)

        for n,part in enumerate(line):
            print '\t',n,part

        if re.search(r'\*\*\*TERM',line[0]):
            term=line[0].partition(' ')[2]
        elif re.search(r'ontology',line[0]):
            nextLine=ontologiesFile.next()
            lang=re.sub('\*','',nextLine[0])
            print 'LANG',lang
            print 'ONT',nextLine[1]
            if term.lower() in termsDict.keys():
                # Some terms not in the dictionary
                parseOntology(nextLine[1],lang,term)

        if nLine==-600:
            break
        nLine+=1

if __name__=="__main__":
    main()
