rm categories.txt

for letter in {a..z}
do

echo $letter

#echo "http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/BrowseEng?OpenView&StartKey="$letter"&Count=100000" 

curl "http://lib-thesaurus.un.org/LIB/DHLUNBISThesaurus.nsf/BrowseEng?OpenView&StartKey="$letter"&Count=100000" | grep 'OpenDocument' >> categories.txt

done

uniq categories.txt > categories_unique.txt
