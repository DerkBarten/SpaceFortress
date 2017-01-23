#!/usr/bin/env bash

game_vers=$1
experiment=$2
game=${game_vers%-*}
weights_prefix=runs/$game/$experiment/weights/${game}_${experiment}
results=runs/$game/$experiment/$game_$experiment.csv

mkdir -p runs/$game/$experiment/weights

python src/main.py --environment gym --display_screen rgb_array --save_weights_prefix $weights_prefix --csv_file $results $game_vers
