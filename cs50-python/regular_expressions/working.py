import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid time")

    h1_24 = convert_to_24(h1, p1)
    h2_24 = convert_to_24(h2, p2)

    return f"{h1_24:02}:{m1:02} to {h2_24:02}:{m2:02}"

def convert_to_24(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
