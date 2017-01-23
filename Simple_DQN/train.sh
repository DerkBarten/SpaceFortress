#!/usr/bin/env bash

game_vers=$1
experiment=$2
game=${game_vers%-*}

# create the directories of they are not present
mkdir -p runs/$game/$experiment/weights

# how the weights will be stored
weights_prefix=runs/$game/$experiment/weights/${game}_${experiment}

# create a new csv file because simple dqn will overwrite the last results if we give it the same output file
session=`ls runs/${game}/${experiment}/*.csv 2>/dev/null | wc -l`

# place where the results will be stored as csv
results=runs/$game/$experiment/${game}_${experiment}_${session}.csv

# python call
python src/main.py --environment gym --display_screen rgb_array --save_weights_prefix $weights_prefix --csv_file $results $game_vers
