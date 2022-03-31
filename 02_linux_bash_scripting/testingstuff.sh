#!/bin/bash

DIR=/home/cmchugh/Desktop/emails
cd $DIR

for i in $*;
do
    if [ -s $! ]:then
    echo "this file was inspected" >> $i
    else;
        rm -f $i
    fi
done