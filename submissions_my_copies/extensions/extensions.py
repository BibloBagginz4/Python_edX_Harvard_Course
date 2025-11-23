"""
(Written by Jeff Truesdell 11/21/2025)
This program prompts the user for the name of a file and then outputs that file’s media type
if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, this common default output instead:
application/octet-stream
"""

def main():
    file_name = input("File name: ").lower().strip()
    print(output_type(file_name))

def output_type(file_name):
    allowed = ("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip")
    
    if "." not in file_name:
        return "application/octet-stream"
    
    ending = file_name.rsplit(".", 1)[1]

    if ending not in allowed:
        return "application/octet-stream"
    
    if ending in ("gif", "jpeg", "png"):
        return "image/" + ending
    
    if ending == "jpg":
            return "image/jpeg"
    
    if ending == "pdf":
            return "application/pdf"
    
    if ending == "txt":
        return "text/plain"
    
    if ending == "zip":
        return "application/zip"
    

main()