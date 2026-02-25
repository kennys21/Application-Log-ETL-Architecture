#Importing necessary libraries
import re
import csv

#this is the pattern for cleaning the log lines cause we will use regex to split and clean it
pattern = re.compile(r"""
    (?P<timestamp>[\d\-:\s,]+)
    \s-\s
    (?P<level>\w+)
    \s-\s
    user_id=(?P<user_id>\w+\d+)
    \-Action=(?P<action>\w+)
    \-status=(?P<status>\w+)
""", re.VERBOSE)

#making the new csv file and write the header
with open("structured_logs.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp",
                     "level", "user_id", "action", "status"])
    #open the log file and read it line by line, then apply the regex pattern to extract the relevant information and write it to the csv file
    with open("random_app.log", "r") as f:
        for line in f:
            match = pattern.search(line)

            if match:
                writer.writerow([
                    match.group("timestamp").strip(),
                    match.group("level"),
                    match.group("user_id"),
                    match.group("action"),
                    match.group("status")
                ])
