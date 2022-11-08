#!/bin/bash

PID_THREAD=$1
echo "Starting capture of jstack for PID ${PID_THREAD}"
for i in {1..2}; do 
	jstack -l ${PID_THREAD}  > /tmp/jstack-$(hostname)-${PID_THREAD}-$(date "+%Y-%m-%d-%H-%M-%S-%Z").txt;
	echo "/tmp/jstack-$(hostname)-${PID_THREAD}-$(date "+%Y-%m-%d-%H-%M-%S-%Z").txt written";
	sleep 2;
done

tar -cvzf thread_dump_${PID_THREAD}.tar.gz /tmp/jstack-$(hostname)-${PID_THREAD}-*.txt