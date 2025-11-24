import dateparser
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

label_to_format = {
    "Relative Time | 3 years ago": "R",
    "Default | 28 November 2018 09:01": "f",
    "Short | Time 09:01": "t",
    "Long | 09:01:00": "T",
    "Short Date | 28/11/2018": "d",
    "Long Date | 28 November 2018": "D",
    "Short Date/Time | 28 November 2018 09:01": "f",
    "Long Date/Time | Wednesday, 28 November 2018 09:01": "F",
}

if len(sys.argv) < 3:
    print("Usage: python discord-timestamp.py <timestamp> <format_label>")
    exit(1)

timestamp = sys.argv[1]
fmt_label = sys.argv[2] if len(sys.argv) > 1 else None

try:
    parsed = dateparser.parse(timestamp, settings={"PREFER_DATES_FROM": "future"})
except Exception as e:
    print(f"Error parsing date: {e}")
    exit(1)

if not parsed:
    print("Error: Could not parse date.")
    exit(1)

try:
    unix_timestamp = int(parsed.timestamp())
except Exception as e:
    print(f"Error converting to unix timestamp: {e}")
    exit(1)

fmt_char = label_to_format.get(fmt_label, "R")

print(f"<t:{unix_timestamp}:{fmt_char}>")
