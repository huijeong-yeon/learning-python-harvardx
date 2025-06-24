def main():
    grocery = {}

    try:
        while True:
            item = input().strip().lower()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
    except EOFError:
        print()

    for item in sorted(grocery):
        print(f"{grocery[item]} {item.upper()}")

main()
