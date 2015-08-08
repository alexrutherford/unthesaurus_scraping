# UN Thesaurus Scraping

Series of scripts to grab the content of the [UNBIS thesaurus](http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/$$searche?OpenForm)

# Usage

_Please use this script sensibly, do not hit the UN BIS server any more than necessary. A copy of the output is provided here, this code is just for informational purposes._

`./grab_categories.sh`

`python parse_links_categories.py`

Produces each term and its direct link in a TSV file; `terms_links.csv`

`python get_words_from_links.py`

Cycles through each term,link pair in `terms_links.csv`, grabs translations in all 6 languages and writes to file.

`parse_relations.py`

Parses the panels on each page describing how the term relates to other terms in each language e.g. related terms, broader terms.

Outputs `relationsHash` which has the following schema

`relationsHash[lang][translatedTerm][relation]=[relatedTerm1,relatedTerm2...relatedTermN]`

Example (taken from [here](http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/MultiEng/0037CF0C07DD6D2485256AA0005FA8F3?OpenDocument)):

`relationsHash['ES']['INDUSTRIA METALMECANICA']['Broader terms']=['INDUSTRIA PESADA']`

# Dependencies

Uses core Python libraries and command line tools `curl` and `uniq`

Only third-party library is [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Ontology

The ontology terms that are included for each language are

1. Term Relationships:
2. Broader terms:
3. Narrower terms:
4. Related terms:
5. Top terms:

# Still To Do

Update to grab other terms related to each term.
