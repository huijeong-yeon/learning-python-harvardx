import re

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid")
    else:
        print("Invalid")

def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, ip)
    if not match:
        return False

    for number in match.groups():
        if not 0 <= int(number) <= 255:
            return False
        if number != "0" and number.startswith("0"):
            return False

    return True

if __name__ == "__main__":
    main()
