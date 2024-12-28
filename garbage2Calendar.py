import sys
import json
from datetime import datetime

months_list = {"Styczeń":1,
               "Luty":2,
               "Marzec":3,
               "Kwiecień":4,
               "Maj":5,
               "Czerwiec":6,
               "Lipiec":7,
               "Sierpień":8,
               "Wrzesień":9,
               "Paźdzernik":10,
               "Listopad":11,
               "Grudzień":12}

def addHeader():
    return ("BEGIN:VCALENDAR\n"+
           "VERSION:2.0\n"+
           "CALSCALE:GREGORIAN\n"+
           "METHOD:PUBLISH\n")

def addAlarm(trigger, name):
    return ("BEGIN:VALARM\n" +
           f"TRIGGER:{trigger}\n" +
           "ACTION:DISPLAY\n" +
           f"DESCRIPTION:{name}\n" +
           "END:VALARM\n")

def addEvent(date: datetime, name, event_no):
    timestamp = format(date, "%Y%m%dT%H%M%SZ")
    return ("BEGIN:VEVENT\n" +
           f"DTSTART;TZID=Europe/Warsaw:{timestamp}\n" +
           f"SUMMARY:Odbior odpadow ({name})\n" +
           f"UID:{timestamp}-{event_no}-jacekskowronekk@gmail.com\n" +
           addAlarm('-P1D', f'Odbior odpadow ({name}) za 24h') +
           addAlarm('-PT0M', f'Odbior odpadow ({name})')+
           "END:VEVENT\n")

def addFooter():
    return "END:VCALENDAR\n"

with open(sys.argv[1]) as file:
    json_file = json.load(file)
    year = json_file["rok"]
    area = json_file["obszar"]
    schedule = json_file["harmonogram"]
    event_id = 0
    ics_data = addHeader()
    for month in schedule:
        for garbage_type in schedule[month]:
            for day in schedule[month][garbage_type]:
                ics_data += addEvent(datetime(year, months_list[month], day, 7, 0),
                                     garbage_type,
                                     event_id)
                event_id +=1
    ics_data += addFooter()
    with open(f'obszar{area}.ics', 'w') as out:
        out.write(ics_data)
