"""
    I cannot run this file, because it appears that the mtehods required in it
    were in a class or other file that was not accessible.
    If I have questions, just re-watch the video again.
"""

def main():
    counts = {}
    words = get_words("address.txt")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts [word] = 1

    save_counts(counts)    