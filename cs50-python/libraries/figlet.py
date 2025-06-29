import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid font name.")

    else:
        sys.exit("Usage: python figlet.py [-f FONT_NAME]")

    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()

