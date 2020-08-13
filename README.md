# Lucky Draw GUI
Simple lucky draw program with GUI. This program will randomly draw one candidate from "unsafe" and add it into "safe".
It is used to choose a lucky guy in our group to do presentation next week :)

# Dependency
- Python 3
- Numpy

# Usage
Start the program by navigating to this folder and typing the following command:
```
python you_are_the_next.py
```
1. Click "Start" button to start lucky draw. 
2. Click "Stop" to confirm. 
3. If everybody agree on the result, click "Update database" to update the json file (move the name from "unsafe" to safe).

# Note:
- Once all people have been drawn and added to the "safe" list, the next batch will start and all people will be moved backed to the "unsafe" list.
- A sample database is provided, update it accordingly if you want to try it yourself.
