# shirt.py - Requirements Checklist

## 1. Command-line arguments
- [x] Program expects exactly two command-line arguments
- [x] `sys.argv[1]` is the input image path (JPEG or PNG)
- [x] `sys.argv[2]` is the output image path (JPEG or PNG)

## 2. Image processing behavior
- [x] Overlay `shirt.png` (transparent background) on the input image
- [x] Resize and crop the input image to match shirt dimensions
- [x] Save the final composited image as output

## 3. Pillow API usage
- [x] Open input image with `Image.open`
- [x] Resize and crop input using `ImageOps.fit`
- [ ] Use default values for:
  - [x] `method`
  - [x] `bleed`
  - [x] `centering`
- [x] Overlay shirt using `Image.paste`
- [x] Save output using `Image.save`

## 4. Error handling (exit via sys.exit)
- [x] Incorrect number of command-line arguments
- [x] Input or output file extension not `.jpg`, `.jpeg`, or `.png` (case-insensitive)
- [x] Input and output extensions do not match
- [x] Input file does not exist

## 5. Assumptions
- [x] Input photo is properly posed so resized/cropped shirt fits correctly
