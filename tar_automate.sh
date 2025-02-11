#!/bin/bash


while true; do

    file=$(ls ~/Downloads/*.tar 2>/dev/null | head -n 1)

    if [ -z "$file" ]; then
        echo "No more tar files"
        break
    fi

    tar -xf "$file"

    rm "$file"
done
