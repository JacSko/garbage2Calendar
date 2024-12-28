# garbage2Calendar

## Overview

Simple script that converts json file with garbage colletion schedule to ICS file that can be easily imported to any calendar (tested with Google/Apple) and provide notifications.
As for now, json file have to be prepared manually but there are ongoing trials to use some CV/OCR algorithms to convert PDF table into json. This will fully automate event conversions and avoid potential errors when data is being passed from PDF to json.

## Usage
1. Prepare garbageSchedule.json file
2. Run script
```bash
$ python garbage2Calendar.py garbageSchedule.json
```
3. Output file will be created with the name basing on 'area' key in json file.

## TODO
[] Use CV/OCR to convert PDF table into json
