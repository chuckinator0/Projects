#!/bin/bash

# Test IP addresses with ping. Pipe into python script to send alert to person responsible.
while read ip; do
	if ping -q -c1 "$ip" &>/dev/null 2>&1; then
		:
	else
		echo "$ip"
fi
done
