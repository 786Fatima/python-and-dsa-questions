## try-except in Python

The try-except block is used to handle runtime errors which are called exceptions and
prevent the running program from crashing and smoothen the execution process.

There are various types of exceptions available to provide detailed knowlwdge about the runtime errors.

try: contains code that could have possible errors.

except: catch error and define its type and contains handling code.

else: runs in case there is no error.

finally: runs regardless of any occurrence of error and conclude the program.

### Syntax

```python
try:
    # risky code
except ExceptionType:
    # handling code
```
