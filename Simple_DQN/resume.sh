#!/usr/bin/env bash

game_vers="$1"
experiment="$2"
game="${game_vers%-*}"


# the directory where the weights are stored
weights_dir=runs/$game/$experiment/weights

# the name of the last weights we managed to reach
weights_name=`ls -v $weights_dir | tail -n 1`

# the last epoch we managed to reach
epoch=`echo $weights_name | cut -d . -f 1 | cut -d _ -f 3`
 
# the location of the weights were using
get_weights=$weights_dir/$weights_name

# the prefix of the name where the weights will be stored
store_weights=$weights_dir/${game}_${experiment}

# create a new csv file because simple dqn will overwrite the last results if we give it the same output file
session=`ls runs/AIM/First/*.csv | wc -l`

# place where the results will be stored as csv
results=runs/$game/$experiment/${game}_${experiment}_${session}.csv

# combine all arguments in the python call
python src/main.py 	--environment gym \
			--display_screen rgb_array \
			--save_weights_prefix ${store_weights}\
			--csv_file ${results} ${game_vers}\
			--load_weights ${get_weights}\
			--start_epoch ${epoch}