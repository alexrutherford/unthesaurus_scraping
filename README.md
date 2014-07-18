# UN Thesaurus Scraping

Series of scripts to grab the content on the [UNBIS thesaurus](http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/$$searche?OpenForm)

# Usage

`./grab_categories.sh'
`python parse\_links\_categories.py'

Produces each term and its direct link in a TSV file; `terms\_links.csv'

`python get\_words\_from\_links.py'

Cycles through each term,link pair in `terms\_links.csv', grabs translations in all 6 languages and writes to file.


# Dependencies

Uses core Python libraries and command line tools `curl' and `uniq'.

Only third-party library is (Beautiful Soup)[http://www.crummy.com/software/BeautifulSoup/bs4/doc/]
