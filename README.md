# UN Thesaurus Scraping

Series of scripts to grab the content of the [UNBIS thesaurus](http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/$$searche?OpenForm)

# Usage

_Please use this script sensibly, do not hit the UN BIS server any more than necessary. A copy of the output is provided here, this code is just for informational purposes._

`./grab_categories.sh`

`python parse_links_categories.py`

Produces each term and its direct link in a TSV file; `terms_links.csv`

`python get_words_from_links.py`

Cycles through each term,link pair in `terms_links.csv`, grabs translations in all 6 languages and writes to file.


# Dependencies

Uses core Python libraries and command line tools `curl` and `uniq`

Only third-party library is [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Still To Do

Update to grab other terms related to each term.
