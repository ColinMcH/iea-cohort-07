#!/bin/bash
set -e 

if [ $# = 0 ]; then
    echo "Script was run with no arguments. Try again."
    exit
fi

filename=$1

if [ -e $filename ]; then
    echo "Files exists" >/dev/null
else
    echo "file does not exist"
    exit 1
fi
