#!/bin/bash

gawk -F',' 'NR > 1 && $3 == 2 && $13 ~ /^S/ {print}' titanic.csv | 
sed -E 's/ male/,M/; s/ female/,F/' | 
gawk -F',' '$7 > 0 {sum += $7; n++} END {if (n > 0) print sum/n}'