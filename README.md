# 🐍 Python Data Types 

Python provides various built-in data types that help in handling different kinds of data effectively. Below is a detailed explanation of data types covered in the Python script.

## 1. 🔢 **Numeric Types**
- **int**: Represents whole numbers. Example: `10`
- **float**: Represents decimal numbers. Example: `10.5`
- **complex**: Represents complex numbers with real and imaginary parts. Example: `3 + 4j`

## 2. 📚 **Sequence Types**
- **str**: Represents text data. Example: `"Hello, Python!"`
- **list**: Ordered collection of items, mutable. Example: `[1, 2, 3, 4, 5]`
- **tuple**: Ordered collection of items, immutable. Example: `(1, 2, 3, 4, 5)`
- **range**: Generates a sequence of numbers. Example: `range(10)`

## 3. 🔢 **Set Types**
- **set**: Unordered collection of unique elements. Example: `{1, 2, 3, 4, 5}`
- **frozenset**: Immutable version of a set. Example: `frozenset([1, 2, 3, 4, 5])`

## 4. 🔑 **Mapping Type**
- **dict**: Collection of key-value pairs. Example: `{"name": "Alice", "age": 25}`

## 5. ✅ **Boolean Type**
- **bool**: Represents `True` or `False` values. Example: `True`

## 6. 🚫 **None Type**
- **NoneType**: Represents the absence of a value. Example: `None`

## 7. 📦 **Built-in Collection Types**
- **Nested list**: List containing lists. Example: `[[1, 2], [3, 4]]`
- **Nested tuple**: Tuple containing tuples. Example: `((1, 2), (3, 4))`
- **Nested dictionary**: Dictionary containing dictionaries. Example: `{"student": {"name": "John", "age": 21}}`

## 8. 🏗 **Custom Objects**
- **Instance of a class**: Example: `custom_object = CustomClass()`

## 9. 🛠 **Callable Types**
- **Function**: Example: `def function_example(): return "I am a function!"`
- **Lambda function**: Example: `lambda x: x * 2`

## 10. 🔄 **Generator & Iterator Types**
- **Generator**: Example: `def generator_example(): yield 1; yield 2`
- **Iterator**: Example: `iter({"a": 1, "b": 2})`

## 11. ✍ **Special String Types**
- **Unicode string**: Example: `"\u03B1\u03B2\u03B3"`
- **Raw string**: Example: `r"C:\\path\\to\\file"`

## 12. 🎭 **Advanced Set Types**
- **Empty set**: Example: `set()`
- **Disjoint set**: Example: `{1, 2} & {3, 4}` (Intersection of two sets)

## 13. 📜 **Advanced Dict Types**
- **Defaultdict**: Dictionary with default values. Example: `defaultdict(int)`
- **OrderedDict**: Maintains order of items. Example: `OrderedDict([("a", 1), ("b", 2)])`

## 14. 🤔 **Boolean Expressions**
- **Truthy value**: Example: `bool("Yes")` (Evaluates to `True`)
- **Falsy value**: Example: `bool("")` (Evaluates to `False`)

## 15. 🔢 **Advanced Numerical Types**
- **Decimal**: Used for precise calculations. Example: `decimal.Decimal("10.5")`
- **Fraction**: Represents rational numbers. Example: `fractions.Fraction(1, 3)`

## 16. 📅 **Other Advanced Types**
- **Date**: Example: `datetime.date(2025, 2, 26)`

## 17. 🏷 **Type Checking**
You can check the type of any variable using the `type()` function. Example:
```python
print(type(integer_value))  # Output: <class 'int'>
print(type(float_value))    # Output: <class 'float'>
```

### 🎯 Conclusion
These data types are fundamental in Python and help in organizing and processing data efficiently. Understanding them will enhance your Python programming skills and improve code efficiency. 🚀

