import re,sys,csv

###################
def makeLink(id):
    return 'http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/'+id+'?OpenDocument' 

###################
def getParts(rawString):
    urlParts=re.split(r'DHLUNBISThesaurus\.nsf\/|\?OpenDocument',rawString)
    url=makeLink(urlParts[1])

    termParts=re.split(r'OpenDocument">|<\/a>',rawString)
    term=termParts[1]

    return term,url

###################
def main():

    inFile=open('categories_unique.txt','r')

    outFile=csv.writer(open('terms_links.csv','w'),delimiter='\t')

    for line in inFile.read().split('\n'):
        try:
            lineParts=getParts(line)
            outFile.writerow(list(lineParts))
        except:
            print line

if __name__=='__main__':
    main() 
