# 02_Requirements_watch.md

## Setup
- [x] Log into cs50.dev
- [x] Create project directory `watch`
- [x] Change into `watch` directory
- [x] Create file `watch.py`
- [x] Follow required code structure per CS50 course website

---

## Problem Understanding
- [x] Input is a string of HTML
- [x] Implement `parse(s) function where s is a str
- [x] Extract any YouTube URL that's the value of a `src` attribute of an `iframe`
  - Assume `src` value is surrounded by double quotes
- [x] Expect only these embed URL formats:
  - `http://youtube.com/embed/<id>`
  - `https://youtube.com/embed/<id>`
  - `https://www.youtube.com/embed/<id>`
- [x] Return the shorter, shareable `youtu.be` URL as a `str`
  - `https://youtu.be/<id>`
- [x] Assume that Input contains *at most* one URL
- [x] If input does not contain any URL, return `None`
- [x] Prefix raw string regular expressions with `r`

---

## Parsing Constraints
- [x] Do not import libraries other than `re` and/or `sys`
- [x] Regex usage is allowed but not required
- [x] Regex should extract the video ID, not hardcode it

---

## Manual Test Cases
- [x] `<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>`  
      returns `https://youtu.be/xvFZjo5PgG0`
- [x] `<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>`  
      returns `https://youtu.be/xvFZjo5PgG0`
- [x] `<iframe src="https://cs50.harvard.edu/python"></iframe>`  
      returns `None`

---

## Validation Logic Checklist
- [x] Detect presence of an iframe `src` attribute
- [x] Confirm URL matches one of the allowed embed formats
- [x] Extract the YouTube video ID correctly
- [x] Construct the shortened `youtu.be` URL correctly
- [x] Return `None` when no valid match exists

---

## Automated Course Validation
- [x] Run `check50 cs50/problems/2022/python/watch`
- [x] Confirm all checks pass (green output)

---

## Submission
- [x] Run `submit50 cs50/problems/2022/python/watch`
- [x] Confirm successful submission
