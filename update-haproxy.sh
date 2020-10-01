#!/bin/bash
python get_proxies.py
cp haproxy.cfg /etc/haproxy/haproxy.cfg
/etc/init.d/haproxy reload