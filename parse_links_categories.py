import re,sys,csv

###################
def makeLink(id):
    return 'http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/'+id+'?OpenDocument'
###################
def getParts(rawString):
    urlParts=re.split(r'DHLUNBISThesaurus\.nsf\/|\?OpenDocument',rawString)
    url=makeLink(urlParts[1])
    try:
        termParts=re.split(r'OpenDocument">|<\/a>',rawString)
        term=termParts[1]
        return term,url
    except:
        print url
        return None,None
###################
def main():


    with open('categories_uniq.txt','r') as inFile:

        outFile=csv.writer(open('terms_links_2.csv','w'),delimiter='\t')

        for line in inFile.read().split('\n'):

            lineParts,url=getParts(line)
            if lineParts and url:
                outFile.writerow(list(lineParts))


if __name__=='__main__':
    main()
