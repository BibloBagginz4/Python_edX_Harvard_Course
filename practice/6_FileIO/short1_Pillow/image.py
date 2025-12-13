from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        # print(img.size)
        # print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


if __name__ == "__main__":
    main()
