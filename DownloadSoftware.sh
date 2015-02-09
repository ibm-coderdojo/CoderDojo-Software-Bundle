#!/bin/bash

#set -x

echo
startTime=`date +%s`
echo Begin  [$(date --date=@${startTime})] ...
echo


root="~/Downloads/CoderDojoSoftware"

### Log Errors
function error_log(){
    $1 $2
    err=$? 
    ERR[ERR_C]="$1=${err}";
    ERR_C=$[${ERR_C} + 1]
    if [ ${err} -ne 0 ];then
	exit -1;
    fi
}

### Clear Error Log
function clear_log(){
    unset ERR
    unset ERR_C
}

### Print Error Log
function print_log(){
    for i in  ${ERR[*]}; do echo $i;  done
}


### Get files
function getfiles(){
    mkdir -p "${1}"
    #echo ${2}
    afile=$(echo ${2}|awk -F '/' '{print $NF}')
    #echo ${afile}
    #wget -q -O "${1}/${afile}" "$2";
    curl -L -s -w "%{filename_effective} : %{time_total}s\n" -o "${1}/${afile}" "$2";
}

### Process
function process(){
    dir=$(dirname ${0})
    file=$(basename ${0}|cut -d \. -f1)
    
    to=["","",""]
    i=0
    while read line; do 
	#echo $line; 
	loc="${root}/${to[0]}/${to[1]}/${to[2]}/"
	if [ "${line:0:3}" = '###' ] ; then
	    #echo $line
	    to[2]=$(echo ${line}|sed 's,###,,g')
	elif [ "${line:0:2}" = '##' ] ; then
	    #echo $line
	    to[1]=$(echo ${line}|sed 's,##,,g')
	    to[2]=""
	elif [ "${line:0:1}" = '#' ] ; then
	    #echo $line
	    to[0]=$(echo ${line}|sed 's,#,,g')
	    to[1]=""
	    to[2]=""
	elif [ ! -z ${line} ]; then
	    #echo $line
	    getfiles "${loc}" "${line}"& 
	    proc[${i}]=$!
	    echo "${proc[${i}]} : ${loc} : ${line}"
	fi
	i=$[${i}+1]
	#echo "${loc}"
        #file "${loc}"
    done <  ${dir}/${file}.properties
}

clear_log

error_log process

print_log

for i in ${proc[@]}; do wait $i; done

echo
echo "... [$(date) - $[`date +%s` - ${startTime}]s] End"
echo

exit 0
