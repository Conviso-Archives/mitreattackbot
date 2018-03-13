#!/bin/bash

#export SLACK_BOT_TOKEN=[YOUR SLACK APP EXPORT TOKEN HERE]
python mitreattackbot.py 
while true; do
	pgrep -f "python mitreattackbot.py" > /dev/null || python mitreattackbot.py
done
