#!/bin/zsh
./gen.sh > out
osacompile -o "$1.scpt" out
python3 osa.py "$1.scpt"
./restart_streamdeck.sh