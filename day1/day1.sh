#!/bin/bash
INPUTFILE=input.txt
START=0
COUNT=0
ARR[0]=0
FOUND="false"
while true
do
  while IFS= read -r line 
  do
    LENGTH=${#line}
    POS=$LENTH-2
    OPERATION=${line:0:1}
    NUMBER=`echo $line |cut -c2-`
    if [[ $OPERATION == "+" ]];then
      START=$(($START + $NUMBER))
    else 
      START=$(($START - $NUMBER))
    fi
    COUNT=$(($COUNT+1))
    if [[ ${ARR[*]} == $START ]];then
      echo "found duplicate value" $START
      exit 0
    fi
    ARR[$COUNT]=$START
  done < "$INPUTFILE"
  if [[ $FOUND = "false" ]]; then
    echo "Solution for day 1, challenge 1: $START"
    FOUND="true"
  fi
done
