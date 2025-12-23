# CS50P - Working Hours Conversion (working.py)

## 1. Brief Problem Summary
- Convert a time range from 12-hour format to 24-hour format.
- Input formats may include hours with or without minutes.
- Output must always be in HH:MM to HH:MM (24-hour time).
- Invalid formats or invalid times must raise `ValueError`.
- A separate test file must thoroughly test the conversion logic.

---

## 2. Folder and File Creation
- [x] Create project folder: `working/`
- [x] Create main program file: `working.py`
- [x] Create test file: `test_working.py`
- [x] Create requirements checklist file: `01_Requirements_file.md`
- [ ] (Optional) Create scratch or sandbox test file: `Test_file.py`

---

## 3. Problem Requirements

### Core Functionality
- [ ] Implement `convert(s: str) -> str`
- [ ] Accept only the specified 12-hour input formats:
  - `9:00 AM to 5:00 PM`
  - `9 AM to 5 PM`
  - `9:00 AM to 5 PM`
  - `9 AM to 5:00 PM`
- [x] Ensure there is exactly one space before `AM` / `PM`
- [x] Ensure `AM` / `PM` are capitalized
- [x] Handle ranges that cross midnight correctly
- [x] Return output in strict `HH:MM to HH:MM` format

### Validation Rules
- [x] Raise `ValueError` for invalid formats
- [x] Raise `ValueError` for invalid times (hours or minutes out of range)
- [x] Do not assume start time is AM and end time is PM

### File Structure Constraints
- [x] Follow the provided `working.py` structure
- [x] Do not import any libraries beyond what is allowed
- [x] `main()` must prompt for input and print the converted result
- [x] `convert()` must contain the conversion logic

### Testing Requirements
- [x] Implement at least three test functions
- [x] All test functions must begin with `test_`
- [x] Tests must include valid inputs
- [x] Tests must include invalid inputs that raise `ValueError`
- [x] Tests must fail if `convert()` is incorrect or incomplete

---

## 4. Check and Submission Steps

### Manual Testing
- [x] Run `python working.py`
- [x] Verify correct output for valid inputs
- [x] Verify `ValueError` is raised for invalid inputs

### Automated Testing
- [x] Run `pytest test_working.py`
- [x] Confirm all tests pass with correct logic
- [x] Intentionally break logic and confirm tests fail

### Final Validation
- [x] Run `check50 cs50/problems/2022/python/working`
- [x] Review any failures and correct issues

### Submission
- [x] Run `submit50 cs50/problems/2022/python/working`
- [x] Confirm successful submission

---
