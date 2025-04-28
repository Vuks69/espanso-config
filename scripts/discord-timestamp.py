import dateparser

# import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python unix.py <timestamp>")
    exit(1)

# Join all arguments after the script name to allow multi-word timestamps
timestamp = " ".join(sys.argv[1:])

try:
    # Change default behavior to prefer future dates for relative times
    parsed = dateparser.parse(timestamp, settings={"PREFER_DATES_FROM": "future"})
except Exception as e:
    print(f"Error parsing date: {e}")
    exit(1)

# try converting to unix timestamp
try:
    unix_timestamp = int(parsed.timestamp())
except Exception as e:
    print(f"Error converting to unix timestamp: {e}")
    exit(1)

print(f"{unix_timestamp}")
