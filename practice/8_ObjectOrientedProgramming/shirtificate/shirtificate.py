"""
(Written by: Jeff Truesdell 2025-12-28)
"""

from fpdf import FPDF, Align


def main():

    page_dims = {"width": 210, "height": 297, "margins": 10}
    image_width = 190
    header_width = 190
    name_width = 120

    name = input("Name: ").strip().title()

    pdf = create_page(page_dims["margins"])

    insert_image(pdf, page_dims["height"])
    insert_header(pdf, page_dims["width"], page_dims["margins"], header_width)
    insert_name(
        pdf,
        name,
        page_dims["width"],
        page_dims["height"],
        page_dims["margins"],
        name_width,
    )

    pdf.output("shirtificate.pdf")


def create_page(margins):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.set_margin(margins)
    pdf.add_page()
    return pdf


def insert_image(pdf, page_h):
    pdf.image(
        "shirtificate.png",
        x=Align.C,
        y=page_h / 3,
        h=(page_h * (2 / 3)),
        keep_aspect_ratio=True,
    )


def insert_header(pdf, page_w, page_m, cell_w):

    header = "CS50 Shirtificate"

    pdf.set_font("Courier", style="BI", size=50)
    pdf.set_text_color(r=0, g=0, b=0)

    header_x = ((page_w - (2 * page_m) - cell_w) / 2) + page_m
    header_y = 25

    pdf.set_xy(header_x, header_y)

    pdf.cell(cell_w, 20, header, border=1, align="C")


def insert_name(pdf, name, page_w, page_h, page_m, name_w):
    pdf.set_font("Courier", style="BI", size=20)
    pdf.set_text_color(r=255, g=255, b=255)

    name_x = (page_w - (2 * page_m) - name_w) / 2 + page_m
    name_y = page_h / 2

    pdf.set_xy(name_x, name_y)

    pdf.cell(name_w, 20, f"{name} took CS50P", align="C")


if __name__ == "__main__":
    main()
