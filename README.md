# Scripts

## Execution:
```

pip install pycurl

python resolverCurl.py 'www.cloudera.com, www.hortonworks.com,www.google.com, www.github.com'

```

```
Get jps PID and execute:
td_capture.sh 12345

```


```
chmod +x import-hive-caller.sh

export JAVA_HOME=/usr/java/jdk1.8.0_232/
export PATH=$PATH:$JAVA_HOME/bin

beeline -u "jdbc:hive2://$(hostname -f):10000/default" --silent=true --outputformat=csv2 --showheader=false -e 'show databases;' > databases_hive.txt

nohup ./import-hive-caller.sh databases_hive.txt > import-hive-caller.log 2>&1

tailf import-hive-caller.log

```