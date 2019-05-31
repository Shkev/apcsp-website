#!/bin/bash

#!/bin/bash


echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Alive</h1>"
echo "<font face="bold" size="5">$(hostname)</font>"
echo "<p> </p>"
echo "<font size="4">$(hostname -I)</font>"

echo "<pre>$(./rpiStatus)</pre>"


