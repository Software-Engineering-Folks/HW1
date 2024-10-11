#!/bin/bash

grep -l "sample" dataset/file* | xargs -I {} sh -c 'echo "{} $(grep -o "CSC510" "{}" | wc -l) $(wc -c < "{}")"' | awk '$2 >= 3' | sort -k2,2nr -k3,3nr | awk '{print $1, $2}' | sed 's/file_/filtered_/'