#!/bin/bash
file_path=$1

i=1
if [ -f "$file_path" ]; then
  while read line; do
    echo "================= Starting script execution DB $i =========="
    echo "Getting kerberos ticket"
    echo "============================================================"
    NAME=atlas; kinit -kt $(find /run/cloudera-scm-agent/process -name ${NAME}*.keytab -path "*${NAME}*" | sort | tail -n 1) $(klist -kt $(find /run/cloudera-scm-agent/process -name ${NAME}*.keytab -path "*${NAME}*" | sort | tail -n 1) | awk '{ print $4 }' | grep "^${NAME}*" | head -n 1)
    klist
    echo "============================================================"
    echo "================ Starting Import ==========================="
    echo "============================================================"
    echo "Importing --------- $line"
    /opt/cloudera/parcels/CDH/lib/atlas/hook-bin/import-hive.sh -d $line
    echo "============================================================"
    echo "================= Finishing Import ========================="
    echo "============================================================"
    echo "================= Finishing script execution DB $i ========="
    ((i++))

  done < "$file_path"
else
  echo "File not found: $file_path"
fi