def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_started:
                number_started = True
                if s[i] == "0":
                    return False 
            else:
                continue
        elif number_started:
            return False
    if not s.isalnum():
        return False
    return True

main()
