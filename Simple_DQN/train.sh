#!/usr/bin/env bash

game=$1
experiment=$2
# standard version
version=-v0

# create the directories of they are not present
mkdir -p runs/$game/$experiment/weights

# how the weights will be stored
weights_prefix=runs/$game/$experiment/weights/${game}_${experiment}

# place where the results will be stored as csv
results=runs/$game/$experiment/${game}_${experiment}.csv

# python call
python src/main.py 	${game}${version}\
			--environment gym \
			--display_screen rgb_array \
			--save_weights_prefix ${weights_prefix}\
			--csv_file ${results}
