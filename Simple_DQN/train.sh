#!/usr/bin/env bash

game=$1
experiment=$2
backend=gpu
# standard version
version=-v0

if [ -z $3 ]; then
	backend=gpu
elif [ $3 == "CPU" -o $3 == "cpu" ]; then
	backend=cpu
fi

if [ $1 == "-h" -o $1 == "--help" ]; then
	echo "Usage:"
	echo "./train.sh P1 P2 P3"
	echo "P1 = [AIM, SFC, SF, SFS] or -h / --help to show this message"
	echo "P2 = The name of the training, for instance MyFirstTraining"
	echo "P3 = Backend, default gpu"
	echo "Example: ./train.sh AIM MyFirstTraining cpu"
	exit
fi
# create the directories of they are not present
mkdir -p runs/$game/$experiment/weights

# how the weights will be stored
weights_prefix=runs/$game/$experiment/weights/${game}_${experiment}

# place where the results will be stored as csv
results=runs/$game/$experiment/${game}_${experiment}.csv

# python call
python src/main.py 	${game}${version}\
			--backend ${backend}\
			--environment gym \
			--display_screen rgb_array \
			--save_weights_prefix ${weights_prefix}\
			--csv_file ${results}
