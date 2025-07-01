import sys
from fpdf import FPDF

def generate_shirtificate(name, template_path="shirtificate.png", output_path="shirtificate.pdf"):
    pdf = FPDF(format="A4", orientation="P", unit="mm")
    pdf.add_page()

    pdf.set_font("helvetica", size=36)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", ln=1)

    img_w = 100
    x = (210 - img_w)/2
    y = 40
    pdf.image(template_path, x=x, y=y, w=img_w)

    text = f"{name} took CS50"
    pdf.set_font("helvetica", size=24, style="B")
    pdf.set_text_color(255, 255, 255)

    text_y = y + (img_w * (template_aspect_ratio :=1)) /2
    text_w = pdf.get_string_width(text)
    text_x = (210 - text_w)/2
    pdf.text(text_x, text_y, text)

    pdf.output(output_path)
    print(f"Generated{output_path}")

def main():
    try:
        name = input("Name: ").strip()
        if not name:
            raise ValueError
    except Exception:
        sys.exit("Usage: Please provide a non-empty name.")
    generate_shirtificate(name)

if __name__ == "__main__":
    main()




