# CS50P Lesson 7 - Response (Email Validation)

## 1. Brief Problem Summary
- Create a Python program that prompts the user for an email address.
- Determine whether the email is syntactically valid.
- Print `Valid` or `Invalid` based on the result.
- Use a third-party validation library. Do not use `re`.
---

## 2. Folder and File Creation
- [x] Create folder: `response`
- [x] Create main program file: `response.py`
- [x] Create Markdown notes file: `01_Requirements_response.md`
- [x] ~~Create test script file: `Test_response.py` (NOT REQUIRED)~~

---

## 3. Problem Requirements
- [x] Prompt user for an email address using `input()`
- [x] Use **one** of the following libraries:
  - `validator-collection`
  - `validators`
- [x] Do **not** use the `re` module
- [x] Validate syntax only (do not check whether the domain exists)
- [x] Output exactly `Valid` or `Invalid` (case-sensitive)
- [x] Follow the required CS50 structure and constraints

---

## 4. Testing Checklist
- [x] Run `python response.py`
- [x] Input: `malan@harvard.edu` -> Output: `Valid`
- [x] Input: your own correct email -> Output: `Valid`
- [x] Input: `malan@@@harvard.edu` -> Output: `Invalid`
- [x] Input: email with malformed punctuation (e.g. extra dot) -> Output: `Invalid`

---

## 5. Check and Submission Steps
- [x] Run `check50 cs50/problems/2022/python/response`
- [x] Review any failed tests and correct output or logic
- [x] Re-run `check50` until all tests pass
- [x] Submit with: submit50 cs50/problems/2022/python/response
