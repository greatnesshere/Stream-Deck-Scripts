#!/bin/zsh
./gen.sh > out
osacompile -o "$1.scpt" out