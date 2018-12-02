#!/bin/bash
INPUTFILE=input.txt
NOA=0
NOB=0
NOC=0
NOD=0
NOE=0
NOF=0
NOG=0
NOH=0
NOI=0
NOJ=0
NOK=0
NOL=0
NOM=0
NON=0
NOO=0
NOP=0
NOQ=0
NOR=0
NOS=0
NOT=0
NOU=0
NOV=0
NOW=0
NOX=0
NOY=0
NOZ=0
NOTWO=0
NOTHREE=0
while IFS= read -r line
do
  TWOFOUND=0
  THREEFOUND=0
  NOA=`echo $line | grep -o a |wc -l`
  NOB=`echo $line | grep -o b |wc -l`
  NOC=`echo $line | grep -o c |wc -l`
  NOD=`echo $line | grep -o d |wc -l`
  NOE=`echo $line | grep -o e |wc -l`
  NOF=`echo $line | grep -o f |wc -l`
  NOG=`echo $line | grep -o g |wc -l`
  NOH=`echo $line | grep -o h |wc -l`
  NOI=`echo $line | grep -o i |wc -l`
  NOJ=`echo $line | grep -o j |wc -l`
  NOK=`echo $line | grep -o k |wc -l`
  NOL=`echo $line | grep -o l |wc -l`
  NOM=`echo $line | grep -o m |wc -l`
  NON=`echo $line | grep -o n |wc -l`
  NOO=`echo $line | grep -o o |wc -l`
  NOP=`echo $line | grep -o p |wc -l`
  NOQ=`echo $line | grep -o q |wc -l`
  NOR=`echo $line | grep -o r |wc -l`
  NOS=`echo $line | grep -o s |wc -l`
  NOT=`echo $line | grep -o t |wc -l`
  NOU=`echo $line | grep -o u |wc -l`
  NOV=`echo $line | grep -o v |wc -l`
  NOW=`echo $line | grep -o w |wc -l`
  NOX=`echo $line | grep -o x |wc -l`
  NOY=`echo $line | grep -o y |wc -l`
  NOZ=`echo $line | grep -o z |wc -l`

  if [ "$NOA" -eq 2 ] || [ "$NOB" -eq 2 ] || [ "$NOC" -eq 2 ] || [ "$NOD" -eq 2 ] || [ "$NOE" -eq 2 ] || [ "$NOF" -eq 2 ] || [ "$NOG" -eq 2 ] || [ "$NOH" -eq 2 ] || [ "$NOI" -eq 2 ] || [ "$NOJ" -eq 2 ] || [ "$NOK" -eq 2 ] || [ "$NOL" -eq 2 ] || [ "$NOM" -eq 2 ] || [ "$NON" -eq 2 ] || [ "$NOO" -eq 2 ] || [ "$NOP" -eq 2 ] || [ "$NOQ" -eq 2 ] || [ "$NOR" -eq 2 ] || [ "$NOS" -eq 2 ] || [ "$NOT" -eq 2 ] || [ "$NOU" -eq 2 ] || [ "$NOV" -eq 2 ] || [ "$NOW" -eq 2 ] || [ "$NOX" -eq 2 ] || [ "$NOY" -eq 2 ] || [ "$NOZ" -eq 2 ];then
    TWOFOUND=1
  fi 
  if [ "$NOA" -eq 3 ] || [ "$NOB" -eq 3 ] || [ "$NOC" -eq 3 ] || [ "$NOD" -eq 3 ] || [ "$NOE" -eq 3 ] || [ "$NOF" -eq 3 ] || [ "$NOG" -eq 3 ] || [ "$NOH" -eq 3 ] || [ "$NOI" -eq 3 ] || [ "$NOJ" -eq 3 ] || [ "$NOK" -eq 3 ] || [ "$NOL" -eq 3 ] || [ "$NOM" -eq 3 ] || [ "$NON" -eq 3 ] || [ "$NOO" -eq 3 ] || [ "$NOP" -eq 3 ] || [ "$NOQ" -eq 3 ] || [ "$NOR" -eq 3 ] || [ "$NOS" -eq 3 ] || [ "$NOT" -eq 3 ] || [ "$NOU" -eq 3 ] || [ "$NOV" -eq 3 ] || [ "$NOW" -eq 3 ] || [ "$NOX" -eq 3 ] || [ "$NOY" -eq 3 ] || [ "$NOZ" -eq 3 ];then
    THREEFOUND=1
  fi
  NOTWO=$(($NOTWO + $TWOFOUND))  
  NOTHREE=$(($NOTHREE + $THREEFOUND))  
  done < "$INPUTFILE"
  echo "aantal 2: "$NOTWO
  echo "aantal 3: "$NOTHREE
CHECKSUM=$(( $NOTWO * $NOTHREE ))
echo $CHECKSUM
