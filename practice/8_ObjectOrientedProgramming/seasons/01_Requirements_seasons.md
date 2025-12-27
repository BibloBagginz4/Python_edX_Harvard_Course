- [x] Create a new directory named `seasons` in the working environment.
- [x] Change into the `seasons` directory.
- [x] Create a new file named `seasons.py`.
- [x] Create a new file named `test_seasons.py`.
- [x] Import `date` from the `datetime` module in `seasons.py`.
- [ ] Import any additional required built-in libraries, ensuring they
      are permitted by the problem description.
- [x] Install the `inflect` module using pip.
- [x] Define a `main()` function in `seasons.py`.
- [x] Prompt the user for their date of birth in `YYYY-MM-DD` format.
       `Date of Birth: `
- [ ] Validate the input format and exit using `sys.exit` if the format
      is invalid.
- [ ] Convert the valid input string into a `date` object.
- [x] Assume the birth time is midnight on the given date.
- [x] Retrieve today’s date using `date.today()`.
- [x] Assume the current time is also midnight on today’s date.
- [x] Subtract the birth date from today’s date to obtain a `timedelta`
      object.
- [x] Convert the total number of days in the `timedelta` to minutes.
- [ ] Round the total minutes to the nearest integer.
- [x] Convert the minute total into English words using `inflect`.
- [x] Ensure the output uses words only, with no numerals.
- [x] Ensure the output does not include the word “and” between words.
- [x] Print the final result exactly once.
- [x] Ensure the program does not raise any unhandled exceptions.
- [x] Add the standard `if __name__ == "__main__": main()` guard.
- [x] Identify all non-`main` functions that contain testable logic.
- [x] Import those functions into `test_seasons.py`.
- [x] Write one or more test functions in `test_seasons.py` for each
      testable function.
- [x] Ensure all test function names begin with `test_`.
- [x] Include tests for correct calculations.
- [x] Include tests for edge cases such as leap years.
- [ ] Include tests for invalid input handling.
- [x] Run `pytest test_seasons.py` and confirm all tests pass.
- [x] Intentionally break logic in `seasons.py` to confirm tests fail
      as expected.
- [x] Restore correct logic and re-run tests to confirm recovery.
- [x] Manually test `seasons.py` with valid dates one year ago.
- [x] Manually test `seasons.py` with valid dates two years ago.
- [x] Manually test `seasons.py` with invalid date formats.
- [x] Run Check50 and review results:
      `check50 cs50/problems/2022/python/seasons`
- [x] Submit the solution using submit 50:
      `submit50 cs50/problems/2022/python/seasons`
