#!/usr/bin/env bash

snapshot=$2
#full=${1##*/}
game=$1

if [ "$1" == "-h" ]; then
	echo "Plays a single game with the specified weights. "
	echo "Usage: ./play.sh GAME WEIGHTS"
  exit 1;
fi

python src/main.py  $game --backend cpu --environment gym --play_games 20 --display_screen true --load_weights $snapshot

