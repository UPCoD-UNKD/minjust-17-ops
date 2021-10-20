#!/bin/bash

function get_data(){
	data_dir=$1
	[ -d $data_dir ] && rmdir $data_dir
	mkdir $data_dir
	cd $data_dir

	echo -e "Downloading..."
	fname='17-UFOP_FULL.zip'
	url=$( curl -silence https://nais.gov.ua/m/ediniy-derjavniy-reestr-yuridichnih-osib-fizichnih-osib-pidpriemtsiv-ta-gromadskih-formuvan | grep 17-UFOP_FULL | cut -d '=' -f2 | cut -d ">" -f1 | tr -d '"' )
	wget -c -O $fname $url --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.19 Safari/537.36"
	echo -e "Downloaded. Size: " `du -hs $fname`
	echo -e "Extracting..."
	7z x -y $fname
	# 7z x -y $fname 15.1-EX_XML_EDR_UO.xml
	# 7z x -y $fname 15.2-EX_XML_EDR_FOP.xml
	echo -e "Extracted."

	rm $fname
	echo -e "Delete $fname"
cd ..
}

function process_data(){
	[ -e $1/17-ufop_full*/17.1* ] && mv $1/17-ufop_full*/17.1* $1/17.1-EX_XML_EDR_UO_FULL.xml
	[ -e $1/17-ufop_full*/17.2* ] && mv $1/17-ufop_full*/17.2* $1/17.2-EX_XML_EDR_FOP_FULL.xml
	cd $1
	echo "Convertiong Orgs to UTF-8"
	time iconv -f cp1251 17.1-EX_XML_EDR_UO_FULL.xml > UO.xml.utf8


	echo "Convertiong FOPs to UTF-8"
	time iconv -f cp1251 17.2-EX_XML_EDR_FOP_FULL.xml > FOP.xml.utf8

	echo "Converting UO file to multy line"
	sed -i -e "s/<RECORD>/\n<RECORD>/g" UO.xml.utf8

	echo "Converting FOP file to multy line"
	sed -i -e "s/<RECORD>/\n<RECORD>/g" FOP.xml.utf8

	echo "mode tag </DATA> to new line"
	sed -i -e "s/<\/DATA>/\n<\/DATA>/g" UO.xml.utf8
	sed -i -e "s/<\/DATA>/\n<\/DATA>/g" FOP.xml.utf8

	echo "Fix charset"
	sed -i -e '0,/windows-1251/{s/windows-1251/utf-8/}' UO.xml.utf8
	sed -i -e '0,/windows-1251/{s/windows-1251/utf-8/}' FOP.xml.utf8

	echo "Cut bad charset"
	sed -i -E  's/(\&#[0-9]{1,10};)//gm' 17-xml/UO.xml
	sed -i -E  's/(\&#[0-9]{1,10};)//gm' 17-xml/FOP.xml
	cd ..
}

dd=data

get_data $dd
process_data $dd

mkdir 17-xml

mv $dd/*.utf8 17-xml/
mv 17-xml/UO.xml.utf8 17-xml/UO.xml
mv 17-xml/FOP.xml.utf8 17-xml/FOP.xml

xml_split -s 1Gb /17-xml/UO.xml
xml_split -s 1Gb /17-xml/FOP.xml

#tar czf data.tgz 17-xml


#echo "Parsing data"
#time ./parseuo.py


#rm sed*
#rm UO.xml.utf8

# TODO: COMMIT HERE

echo 'done'
