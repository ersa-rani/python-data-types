# Python has various built-in data types

# Numeric Types
integer_value = 10  # int: Stores whole numbers
float_value = 10.5  # float: Stores decimal numbers
complex_value = 3 + 4j  # complex: Stores complex numbers

# Sequence Types
string_value = "Hello, Python!"  # str: Stores text
list_value = [1, 2, 3, 4, 5]  # list: Stores an ordered collection of items
tuple_value = (1, 2, 3, 4, 5)  # tuple: Immutable ordered collection
range_value = range(10)  # range: Generates a sequence of numbers

# Set Types
set_value = {1, 2, 3, 4, 5}  # set: Unordered collection of unique elements
frozenset_value = frozenset([1, 2, 3, 4, 5])  # frozenset: Immutable set

# Mapping Type
dict_value = {"name": "Alice", "age": 25}  # dict: Key-value pair collection

# Boolean Type
bool_value = True  # bool: Represents True or False

# None Type
none_value = None  # NoneType: Represents absence of a value

# Built-in Collection Types
list_of_lists = [[1, 2], [3, 4]]  # Nested list
tuple_of_tuples = ((1, 2), (3, 4))  # Nested tuple
dict_of_dicts = {"student": {"name": "John", "age": 21}}  # Nested dictionary

# Custom Objects
class CustomClass:
    pass  #or ...

custom_object = CustomClass()  # Instance of a user-defined class

# Callable Types
def function_example():
    return "I am a function!"

lambda_function = lambda x: x * 2  # Lambda function

# Generator & Iterator Types
def generator_example():
    yield 1
    yield 2

gen = generator_example()  # Generator
dict_iterator = iter({"a": 1, "b": 2})  # Iterator from dictionary

# Special String Types
unicode_string = "αβγ"  # Unicode string
raw_string = r"C:\\path\\to\\file"  # Raw string (ignores escape sequences)

# Advanced Set Types
empty_set = set()  # Empty set
disjoint_set = {1, 2} & {3, 4}  # Intersection of two sets

# Advanced Dict Types
from collections import defaultdict, OrderedDict

def_dict = defaultdict(int)  # Dictionary with default values
ordered_dict = OrderedDict([("a", 1), ("b", 2)])  # Ordered dictionary

# Boolean Expressions
is_python_fun = bool("Yes")  # Evaluates to True
is_empty_string_false = bool("")  # Evaluates to False

# Advanced Numerical Types
import decimal
import fractions

decimal_value = decimal.Decimal("10.5")  # Decimal type for precise calculations
fraction_value = fractions.Fraction(1, 3)  # Fraction type for rational numbers

# Other Advanced Types
import datetime

date_value = datetime.date(2025, 2, 26)  # Stores a date

# Type Checking
print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(string_value))
print(type(list_value))
print(type(tuple_value))
print(type(range_value))
print(type(set_value))
print(type(frozenset_value))
print(type(dict_value))
print(type(bool_value))
print(type(none_value))
print(type(custom_object))
print(type(function_example))
print(type(lambda_function))
print(type(gen))
print(type(dict_iterator))
print(type(unicode_string))
print(type(raw_string))
print(type(empty_set))
print(type(disjoint_set))
print(type(def_dict))
print(type(ordered_dict))
print(type(is_python_fun))
print(type(is_empty_string_false))
print(type(decimal_value))
print(type(fraction_value))
print(type(date_value))
