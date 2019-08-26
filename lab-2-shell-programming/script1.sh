#!/bin/bash

echo "enter time after which you want to shut down (example 5s,5m,5h)"
read -p Time: time

sleep $time
echo shutting down ................
sleep 1s

shutdown -h +0
