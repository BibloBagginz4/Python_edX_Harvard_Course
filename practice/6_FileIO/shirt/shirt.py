"""
(Written by Jeff Truesdell 12-17-2025)
1) This program expects exactly two command-line arguments:
    1a. In sys.argv[1], the name (or path) of a JPEG or PNG to read
        (i.e., open) as input.
    1b. In sys.argv[2], the name (or path) of a JPEG or PNG to write
        (i.e., save) as output
2) The program will overlay shirt.png (which has a transparent
   background) on the input after resizing and cropping the input to be
   the same size, saving the result as its output.
3) It will open the input with Image.open, per
   pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
   3a. resize and crop the input with ImageOps.fit, per
       pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
   3b. Use default values for method, bleed, and centering,
   3c. overlay the shirt with Image.paste, per
       pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste
   3d. Then save the result with Image.save, per
       pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save
4) The program will exit via sys.exit if:
   4a. the user does not specify exactly two command-line arguments.
   4b. the input’s and output’s names do not end in .jpg, .jpeg, or
       .png, case-insensitively,
   4c. the input’s name does not have the same extension as the output’s
       name
   4d. if the specified input does not exist.
5) Assume that the input will be a photo of someone posing in just the
   right way, like these demos, so that, when they’re resized and
   cropped, the shirt appears to fit perfectly.
"""

import sys
import os
from PIL import Image, ImageOps


def main():
    # Validate command-line arguments equals 2
    if len(sys.argv) != 3:
        sys.exit("Error: Incorrect number of Input Arguments")

    input_file = sys.argv[1]
    _, in_extension = os.path.splitext(input_file)
    in_extension = in_extension.lower()
    output_file = sys.argv[2]
    _, out_extension = os.path.splitext(output_file)
    out_extension = out_extension.lower()

    # Verifying that file extension
    ok_file_types = [".png", ".jpeg", ".jpg"]
    if in_extension not in ok_file_types or out_extension not in ok_file_types:
        sys.exit("Error: Wrong file type(s)")

    # Verifying that Input and Output file extensions match
    if in_extension != out_extension:
        sys.exit("Error: Input and output file extensions do not match")

    # Opening merging and saving images
    try:
        im1 = Image.open(input_file)
        shirt = Image.open("shirt.png")

    except FileNotFoundError:
        sys.exit("Error: File not Found")

    im_new = ImageOps.fit(im1, shirt.size)
    im_new.paste(shirt, shirt)
    im_new.save(output_file)


if __name__ == "__main__":
    main()
