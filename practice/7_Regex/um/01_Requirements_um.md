# CS50P Problem Checklist - um.py

## 1. Brief Problem Summary
- [ ] Read and understand the problem goal: count occurrences of the word "um" in text.
- [ ] Confirm that matching is case-insensitive.
- [ ] Confirm that "um" must be a standalone word, not part of another word.

## 2. Folder and File Creation
- [ ] Create folder named `um`
- [ ] Create file `um.py` inside the `um` folder
- [ ] Create file `test_um.py` inside the `um` folder
- [ ] Create Markdown file `01_Requirements_file.md` inside the `um` folder
- [ ] Create optional local test scratch file `Test_file.py` if helpful

## 3. Problem Requirements
- [ ] Implement function `count(s: str) -> int`
- [ ] Function returns the number of standalone "um" occurrences
- [ ] Matching must be case-insensitive
- [ ] Substrings inside other words must not be counted
- [ ] Punctuation around "um" must be handled correctly
- [ ] No additional libraries may be imported
- [ ] Use of `re` and `sys` is allowed but optional
- [ ] Follow the provided file structure exactly

## 4. Test Requirements
- [ ] Implement three or more test functions in `test_um.py`
- [ ] Each test function name starts with `test_`
- [ ] Tests include valid and invalid matching cases
- [ ] Tests fail when incorrect logic is introduced intentionally
- [ ] All tests pass with correct implementation

## 5. Manual Verification
- [ ] Run `python um.py` and verify prompt appears
- [ ] Input `um` returns `1`
- [ ] Input `um?` returns `1`
- [ ] Input `Um, thanks for the album.` returns `1`
- [ ] Input `Um, thanks, um...` returns `2`
- [ ] Input `yummy` returns `0`

## 6. Automated Testing
- [ ] Run `pytest test_um.py`
- [ ] All tests pass for correct implementation
- [ ] At least one test fails when logic is intentionally broken

## 7. Final Checks
- [ ] Code follows the provided structure
- [ ] No extra imports added
- [ ] Logic is clear and minimal
- [ ] Files are saved in the correct folder

## 8. Submission
- [ ] Run `check50 cs50/problems/2022/python/um`
- [ ] Review output for failures if any
- [ ] Run `submit50 cs50/problems/2022/python/um`
