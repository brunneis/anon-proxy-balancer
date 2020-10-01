#!/bin/bash
/etc/init.d/haproxy start
while true;
  do 
    ./update-haproxy.sh
    sleep 60
  done