# 01_Requirements_numb3rs.md

## Setup
- [x] Create project directory `numb3rs`
- [x] Change into `numb3rs` directory
- [x] Create `numb3rs.py`
- [x] Create `test_numb3rs.py`
- [x] Follow required file structure per CS50 course website

---

## Functional Requirements (numb3rs.py)
- [x] Accept IPv4 address input as a string
- [x] Validate format as `#.#.#.#`
- [x] Ensure exactly four octets
- [x] Ensure each octet is numeric
- [x] Ensure each octet is between 0 and 255 (inclusive)
- [x] Reject any octet with leading zeros (e.g., `001`)
- [x] Return `True` for valid IPv4 addresses
- [x] Return `False` for invalid IPv4 addresses

---

## Manual Validation Checks
- [x] `127.0.0.1` returns `True`
- [x] `255.255.255.255` returns `True`
- [x] `512.512.512.512` returns `False`
- [x] `1.2.3.1000` returns `False`
- [x] `192.168.001.1` returns `False`
- [x] `cat` returns `False`

---

## Test Requirements (test_numb3rs.py)
- [x] Create two or more test functions
- [x] Ensure all test function names start with `test_`
- [x] Test valid IPv4 addresses
- [x] Test invalid numeric ranges
- [x] Test invalid formatting
- [x] Test non-numeric input

---

## Test Execution
- [x] Run `pytest test_numb3rs.py`
- [x] Confirm all tests pass
- [x] Intentionally break `validate` logic
- [x] Re-run `pytest` and confirm tests fail as expected
- [x] Restore correct logic

---

## Automated Course Validation
- [x] Run `check50 cs50/problems/2022/python/numb3rs`
- [x] Verify all checks pass (green output)

---

## Submission
- [x] Run `submit50 cs50/problems/2022/python/numb3rs`
- [x] Confirm successful submission
