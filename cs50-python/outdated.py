def main():
    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = map(int, date.split("/"))

            elif "," in date:
                month_name, day_year = date.split(" ", 1)
                day, year = map(int, day_year.replace(",", "").split())
                months = [
                    "January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"
                ]
                if month_name not in months:
                    raise ValueError
                month = months.index(month_name) + 1

            else:
                raise ValueError

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
