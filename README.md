# py_web_monitor
Simple script to monitor for changes on a webpage.

## Description

py_web_monitor can be used to get a notification when changes are made
to a certain webpage.

It works by downloading the page source and calculating its sha256 hash value, 
then storing it in a JSON file. Next time the program is run it will compare the 
hash in the JSON file with the current hash of the downloaded page and send a notification
if they are different.

## Usage

Before using it, you must create a ``page_list.txt`` file where you will list the 
pages you want to monitor, one URL on a line.

To run it repeatedly, add the script as a system cron job. 
