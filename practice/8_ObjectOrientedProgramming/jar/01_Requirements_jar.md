- [x] Create a new folder named `jar` in the workspace.
- [x] Change directory into the `jar` folder.
- [x] Create a new file named `jar.py`.
- [x] Define a class named `Jar`.
- [x] Implement the `__init__` method with a default capacity of 12.
- [x] Validate that `capacity` is a non-negative integer and raise
      `ValueError` if it is not.
- [x] Initialize the internal cookie count to 0.
- [x] Implement the `__str__` method to return one cookie emoji per
      cookie currently stored.
- [x] Implement the `deposit` method to add a given number of cookies.
- [x] Enforce the capacity limit in `deposit` and raise `ValueError`
      if exceeded.
- [x] Implement `withdraw` method to remove a given number of cookies.
- [x] Prevent withdrawing more cookies than are present and raise
      `ValueError` if attempted.
- [x] Implement `capacity` property to return the jar’s maximum capacity.
- [x] Implement the `size` property to return the current number of cookies.
- [x] Ensure method signatures exactly match the provided structure.
- [x] Create a new file named `test_jar.py`.
- [x] Import the `Jar` class into `test_jar.py`.
- [x] Write a `test_init` function to verify correct capacity initialization.
- [x] Write a `test_str` function to verify string output reflects cookie count.
- [x] Write a `test_deposit` function to verify cookie addition and
      capacity enforcement.
- [x] Write a `test_withdraw` function to verify cookie removal and
      underflow protection.
- [x] Ensure all test function names begin with `test_`.
- [x] Run `pytest test_jar.py` and confirm all tests pass.
- [x] Optionally run `check50 cs50/problems/2022/python/jar` to validate
      against CS50 tests.
- [x] Submit the assignment using `submit50 cs50/problems/2022/python/jar`.
