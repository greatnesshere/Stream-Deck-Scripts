#!/bin/zsh
./gen.sh > out
osacompile -o "$1.scpt" out
python3 osa.py "$1.scpt"
killall "Stream Deck"
sleep 1
osascript -e 'activate application "Elgato Stream Deck"'