# UN Thesaurus Scraping

Series of scripts to grab the content on the [UNBIS thesaurus](http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/$$searche?OpenForm)

# Usage

`./grab_categories.sh'
`python parse\_links\_categories.py'

Produces each term and its direct link in a TSV file; `terms_links.csv'

# Dependencies

Uses core Python libraries and command line tools `curl' and `uniq'
