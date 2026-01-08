#!/bin/bash
# Ping every IP address in a given network (1-254: assumes subnet /24).
# Print each device that responds.

# TODO parse $1, try to get subnet
if [$1 == ""] ; then
    echo "Usage:  ./ipsweep.sh 192.168.1"
else
    for ip in `seq 1 254`; do
        ping $1.$ip -c 1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
fi
