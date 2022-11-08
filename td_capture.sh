#!/bin/bash

PID_THREAD=$1
COMPRESSED_FILE="thread_dump_${PID_THREAD}"
FILE_LIST="jstack-$(hostname)-${PID_THREAD}-*.txt"

echo "Starting capture of jstack for PID ${PID_THREAD}"
for i in {1..2}; do 
	jstack -l ${PID_THREAD}  > jstack-$(hostname)-${PID_THREAD}-$(date "+%Y-%m-%d-%H-%M-%S-%Z").txt;
	echo "jstack-$(hostname)-${PID_THREAD}-$(date "+%Y-%m-%d-%H-%M-%S-%Z").txt written";
	sleep 2;
done

mkdir ${COMPRESSED_FILE}
mv ${FILE_LIST} ${COMPRESSED_FILE}
tar -cvzf ${COMPRESSED_FILE}.tar.gz ${COMPRESSED_FILE} --remove-files