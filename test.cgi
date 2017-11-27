#!/bin/sh

. /usr/share/libubox/jshn.sh

echo "Content-type: text/html"
echo ""

O=$(wget "http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1" -O -)

echo "$O"
json_load "$O"
json_select wind
json_get_var var1 speed
echo "speed: $var1"

