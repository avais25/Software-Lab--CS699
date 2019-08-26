#!/bin/bash
file=$(ls ~/Pictures | shuf -n1)
gsettings set org.gnome.desktop.background picture-uri "file:///home/avais/Pictures/$file"
echo $file
