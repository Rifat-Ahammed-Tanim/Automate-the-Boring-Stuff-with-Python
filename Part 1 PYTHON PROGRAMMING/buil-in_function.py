"""
1. Type Conversion Functions
Convert one data type into another.

| Function      | Description           | Example                         |
| ------------- | --------------------- | ------------------------------- |
| `int()`       | Convert to integer    | `int("10") → 10`                |
| `float()`     | Convert to float      | `float("3.14") → 3.14`          |
| `str()`       | Convert to string     | `str(123) → "123"`              |
| `bool()`      | Convert to boolean    | `bool(0) → False`               |
| `list()`      | Convert to list       | `list("abc") → ['a','b','c']`   |
| `tuple()`     | Convert to tuple      | `tuple([1,2]) → (1,2)`          |
| `set()`       | Convert to set        | `set([1,1,2]) → {1,2}`          |
| `dict()`      | Create dictionary     | `dict(a=1,b=2) → {'a':1,'b':2}` |
| `bytes()`     | Convert to bytes      | `bytes("Hi","utf-8")`           |
| `bytearray()` | Mutable bytes         | `bytearray("Hi","utf-8")`       |
| `complex()`   | Create complex number | `complex(2,3) → (2+3j)`         |
| `frozenset()` | Immutable set         | `frozenset([1,2,2]) → {1,2}`    |

"""

"""

2. Math & Numeric Functions
Work with numbers.

| Function   | Description          | Example                  |
| ---------- | -------------------- | ------------------------ |
| `abs()`    | Absolute value       | `abs(-7) → 7`            |
| `round()`  | Round number         | `round(3.1416,2) → 3.14` |
| `min()`    | Smallest value       | `min(3,7,2) → 2`         |
| `max()`    | Largest value        | `max([1,4,9]) → 9`       |
| `sum()`    | Sum of values        | `sum([1,2,3]) → 6`       |
| `pow()`    | Power (x^y)          | `pow(2,3) → 8`           |
| `divmod()` | Quotient & remainder | `divmod(7,3) → (2,1)`    |
| `bin()`    | Convert to binary    | `bin(8) → '0b1000'`      |
| `oct()`    | Convert to octal     | `oct(8) → '0o10'`        |
| `hex()`    | Convert to hex       | `hex(15) → '0xf'`        |


"""

"""

3. Iteration & Functional Programming
For loops and function-style coding.

| Function      | Description                | Example                                          |
| ------------- | -------------------------- | ------------------------------------------------ |
| `len()`       | Length of object           | `len("Hello") → 5`                               |
| `range()`     | Sequence of numbers        | `list(range(3)) → [0,1,2]`                       |
| `enumerate()` | Index + value              | `list(enumerate(['a','b'])) → [(0,'a'),(1,'b')]` |
| `map()`       | Apply function to iterable | `list(map(str, [1,2,3])) → ['1','2','3']`        |
| `filter()`    | Filter iterable            | `list(filter(lambda x:x>2,[1,2,3])) → [3]`       |
| `zip()`       | Combine iterables          | `list(zip([1,2],['a','b'])) → [(1,'a'),(2,'b')]` |
| `iter()`      | Get iterator               | `iter([1,2])`                                    |
| `next()`      | Next item from iterator    | `next(iter([1,2,3])) → 1`                        |
| `sorted()`    | Return sorted list         | `sorted([3,1,2]) → [1,2,3]`                      |
| `reversed()`  | Reverse iterator           | `list(reversed([1,2,3])) → [3,2,1]`              |


"""

"""

4. Object & Class Functions

| Function         | Description                 | Example                        |
| ---------------- | --------------------------- | ------------------------------ |
| `isinstance()`   | Check type of object        | `isinstance(5,int) → True`     |
| `issubclass()`   | Check subclass              | `issubclass(bool,int) → True`  |
| `getattr()`      | Get attribute               | `getattr("hi","upper")`        |
| `setattr()`      | Set attribute               | `setattr(obj,'x',10)`          |
| `hasattr()`      | Check attribute             | `hasattr("hi","upper") → True` |
| `delattr()`      | Delete attribute            | `delattr(obj,'x')`             |
| `property()`     | Create property in class    | Used in OOP                    |
| `classmethod()`  | Define class method         | Used in OOP                    |
| `staticmethod()` | Define static method        | Used in OOP                    |
| `super()`        | Access parent class         | `super().__init__()`           |
| `callable()`     | Check if object is callable | `callable(len) → True`         |

"""

"""

5. Input/Output & Utility Functions

| Function       | Description              | Example                         |
| -------------- | ------------------------ | ------------------------------- |
| `print()`      | Print to console         | `print("Hello")`                |
| `input()`      | Take input from user     | `input("Name: ")`               |
| `open()`       | Open a file              | `open("file.txt","r")`          |
| `dir()`        | List attributes/methods  | `dir(str)`                      |
| `help()`       | Get documentation        | `help(str)`                     |
| `id()`         | Memory address of object | `id(10)`                        |
| `globals()`    | Global namespace dict    | `globals()`                     |
| `locals()`     | Local namespace dict     | `locals()`                      |
| `vars()`       | `__dict__` of object     | `vars(obj)`                     |
| `repr()`       | String representation    | `repr("hi") → "'hi'"`           |
| `ascii()`      | String with ASCII        | `ascii("♥") → "'\\u2665'"`      |
| `format()`     | Format values            | `format(3.1416,".2f") → '3.14'` |
| `object()`     | Create base object       | `object()`                      |
| `memoryview()` | Memory view object       | `memoryview(b"abc")`            |
| `breakpoint()` | Debugging                | `breakpoint()`                  |
| `__import__()` | Import module manually   | `__import__('math')`            |

"""

"""

6. Compilation & Evaluation Functions

| Function    | Description         | Example                    |
| ----------- | ------------------- | -------------------------- |
| `eval()`    | Evaluate expression | `eval("5+3") → 8`          |
| `exec()`    | Execute Python code | `exec("x=5; print(x)")`    |
| `compile()` | Compile code object | `compile("5+3","","eval")` |

"""