import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_exts = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_exts or output_ext not in valid_exts:
        sys.exit("Invalid file extension. Only .jpg, .jpeg, .png are allowed.")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions.")

    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(input_file)
        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)
        photo.save(output_file)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
