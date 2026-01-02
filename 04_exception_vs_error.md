# Difference between Exception and Error

## Exception

An Exception is a runtime error that occurs during program execution
and can be handled using `try-except` blocks. Exceptions usually arise due
to logical or runtime issues that can be fixed mostly.

Examples:

- ValueError
- ZeroDivisionError
- IndexError

## Error

An Error is a serious issue caused by system-level problems and is not
generally handled by application code. Errors usually indicate issues beyond
the control of the programmer.

Examples:

- MemoryError
- SystemError
- OverflowError

---

## Key Differences

| Aspect       | Exception                       | Error                      |
| ------------ | ------------------------------- | -------------------------- |
| Handling     | Can be handled using try-except | Usually cannot be handled  |
| Cause        | Program logic or runtime issues | System-level issues        |
| Control      | Programmer has control          | Outside programmer control |
| Program Flow | Program can continue            | Program terminates         |
| Examples     | ValueError, IndexError          | MemoryError, SystemError   |

## Example of Exception Handling

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input provided")
```
