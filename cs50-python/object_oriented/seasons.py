from datetime import date
import sys
import inflect

def compute_age_in_minutes(birth_date, today=None):
    if today is None:
        today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words

def main():
    user_input = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(user_input)
    except Exception:
        print("Invalid date")
        sys.exit(1)

    minutes = compute_age_in_minutes(birth_date)
    words = minutes_to_words(minutes).capitalize()
    print(f"{words} minutes")


if __name__ == "__main__":
    main()
