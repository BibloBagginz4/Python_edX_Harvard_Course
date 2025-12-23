# CS50P Problem Checklist - um.py

## 1. Brief Problem Summary
- [x] Read and understand the problem goal: count occurrences of the word "um" in text.
- [x] Confirm that matching is case-insensitive.
- [x] Confirm that "um" must be a standalone word, not part of another word.

## 2. Folder and File Creation
- [x] Create folder named `um`
- [x] Create file `um.py` inside the `um` folder
- [x] Create file `test_um.py` inside the `um` folder
- [x] Create Markdown file `01_Requirements_um.md` inside the `um` folder

## 3. Problem Requirements
- [x] Implement function `count(s: str) -> int`
- [x] Function returns the number of standalone "um" occurrences
- [x] Matching must be case-insensitive
- [x] Substrings inside other words must not be counted
- [x] Punctuation around "um" must be handled correctly
- [x] Use findall function from the re module
- [x] No additional libraries may be imported
- [x] Use of `re` and `sys` is allowed but optional
- [x] Follow the provided file structure exactly

## 4. Test Requirements
- [x] Implement three or more test functions in `test_um.py`
- [x] Each test function name starts with `test_`
- [x] Tests include valid and invalid matching cases
- [x] Tests fail when incorrect logic is introduced intentionally
- [x] All tests pass with correct implementation

## 5. Manual Verification
- [x] Run `python um.py` and verify prompt appears
- [x] Input `um` returns `1`
- [x] Input `um?` returns `1`
- [x] Input `Um, thanks for the album.` returns `1`
- [x] Input `Um, thanks, um...` returns `2`
- [x] Input `yummy` returns `0`

## 6. Automated Testing
- [x] Run `pytest test_um.py`
- [x] All tests pass for correct implementation
- [x] At least one test fails when logic is intentionally broken

## 7. Final Checks
- [x] Code follows the provided structure
- [x] No extra imports added
- [x] Logic is clear and minimal
- [x] Files are saved in the correct folder

## 8. Submission
- [x] Run `check50 cs50/problems/2022/python/um`
- [x] Review output for failures if any
- [x] Run `submit50 cs50/problems/2022/python/um`
