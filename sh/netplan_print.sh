#!/bin/bash
# Print every yaml file in the /etc/netplan directory.

for y in /etc/netplan/*; do
    echo ----
    echo $y
    echo ""
    sudo cat $y
done

