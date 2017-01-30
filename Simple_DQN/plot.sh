#!/usr/bin/env bash

inputfile=$1

# ignore the extension of the output file
outputfile=`echo $2 | cut -d . -f 1`.png 

# get the extension of the input file
extension=`echo $inputfile | cut -d . -f 2`

if [ $extension != "csv" ];then
	echo "Please select a csv file"
	exit 1;
fi

echo $2

if [ -z $2 ]; then
	python src/plot.py $inputfile
	exit
fi

python src/plot.py $inputfile --png_file $outputfile