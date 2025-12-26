import re
from pathlib import Path

# -----------------------------
# USER CONFIGURATION
# -----------------------------
TRANSCRIPT_FILE = Path(
    r"C:\Users\sdsug\Documents\Python_edX_Harvard_Course\practice\8_ObjectOrientedProgramming\Lesson_Transcript\Lecture_8_(Transcript).txt"
)

OUTPUT_DIR = Path(
    r"C:\Users\sdsug\Documents\Python_edX_Harvard_Course\practice\8_ObjectOrientedProgramming\Lesson_Transcript\chunks"
)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Chapter definitions: (title, timestamp)
CHAPTERS = [
    ("Introduction", "0:00"),
    ("Object-Oriented_Programming", "0:24"),
    ("Tuples", "1:00"),
    ("Dictionaries", "18:39"),
    ("Classes_and_Objects", "26:45"),
    ("Instance_Methods", "39:18"),
    ("Validating_Attributes", "59:49"),
    ("String_Method", "1:04:25"),
    ("Custom_Methods", "1:11:13"),
    ("Properties_Getters_Setters", "1:15:33"),
    ("Types_and_Classes", "1:38:49"),
    ("Class_Methods", "1:47:23"),
    ("Inheritance", "2:17:29"),
    ("Operator_Overloading", "2:31:59"),
]


# -----------------------------
# HELPERS
# -----------------------------
def timestamp_to_seconds(ts: str) -> int:
    parts = list(map(int, ts.split(":")))
    if len(parts) == 2:
        m, s = parts
        return m * 60 + s
    h, m, s = parts
    return h * 3600 + m * 60 + s


TIMESTAMP_REGEX = re.compile(r"(\d+:\d{2}(?::\d{2})?)")

# -----------------------------
# LOAD TRANSCRIPT
# -----------------------------
with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Pair each line with its timestamp (if present)
parsed_lines = []
current_time = None

for line in lines:
    match = TIMESTAMP_REGEX.search(line)
    if match:
        current_time = timestamp_to_seconds(match.group(1))
    parsed_lines.append((current_time, line))

# -----------------------------
# SPLIT BY CHAPTERS
# -----------------------------
chapter_bounds = []
for i, (title, ts) in enumerate(CHAPTERS):
    start = timestamp_to_seconds(ts)
    end = (
        timestamp_to_seconds(CHAPTERS[i + 1][1])
        if i + 1 < len(CHAPTERS)
        else float("inf")
    )
    chapter_bounds.append((title, start, end))

# -----------------------------
# WRITE OUTPUT FILES
# -----------------------------
for title, start, end in chapter_bounds:
    out_path = OUTPUT_DIR / f"Lecture8_{title}.txt"
    with open(out_path, "w", encoding="utf-8") as out:
        for ts, line in parsed_lines:
            if ts is not None and start <= ts < end:
                out.write(line)

print(f"Transcript split complete. Files written to:\n{OUTPUT_DIR}")
