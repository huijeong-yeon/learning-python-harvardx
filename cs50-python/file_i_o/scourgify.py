import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            students = []

            for row in reader:
                try:
                    first, last = row["name"].split(", ")
                    students.append({
                        "first": last,
                        "last": first,
                        "house": row["house"]
                    })
                except ValueError:
                    sys.exit("Invalid name format in CSV file")

        with open(output_file, "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
