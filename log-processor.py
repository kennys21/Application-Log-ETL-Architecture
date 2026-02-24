import re
import csv

pattern = re.compile(r"""
    (?P<timestamp>[\d\-:\s,]+)
    \s-\s
    (?P<level>\w+)
    \s-\s
    user_id=(?P<user_id>\w+\d+)
    \-Action=(?P<action>\w+)
    \-status=(?P<status>\w+)
""", re.VERBOSE)

with open("structured_logs.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "level", "user_id", "action", "status"])

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
