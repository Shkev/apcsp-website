#!/bin/bash

echo "Which Pi would you like to check?"
read input
if [ "$input" ==  "" ]; then 	
	for var in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
	do
		if [ $var -lt 10 ]; then	
			name="rpi0$var"
		else
			name="rpi$var"
		fi
	
		if ping -c 1 -W 1 "$name" >/dev/null 2>&1; then
			echo "$name : alive"
		else
			echo "$name : down"
		fi
	done

else
	if ping -c 1 -W 1 "$input" >/dev/null 2>&1; then
		echo "$input : alive"
	else
		echo "$input : down"
	fi
fi
