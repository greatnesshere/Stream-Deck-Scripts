#!/bin/zsh
cat /dev/null > tmp
A=4
cat ./data/p.0
read line
echo -n $line
cat ./data/p.1
read line
echo -n $line > tmp
while read line;do
cat tmp
if [[ -z $line ]];then
cat ./data/p.3
break
fi
cat ./data/p.i
echo -n $line > tmp
let A++
done
echo
while [ $A -gt 0 ];do
echo end
let A--
done