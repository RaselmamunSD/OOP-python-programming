"""
Ans:Structure:
List: A list is an ordered collection of items. It maintains the order of elements and allows duplicate values. Elements in a list are indexed and can be accessed using their index positions.
Dictionary: A dictionary is an unordered collection of key-value pairs. It does not maintain any specific order. Each element in a dictionary is identified by its unique key, and the corresponding value can be accessed using the key.
Indexing and Accessing Elements:
List: Elements in a list can be accessed using index positions. The index starts from 0 for the first element, and negative indexing is also supported to access elements from the end of the list.
Dictionary: Elements in a dictionary are accessed using keys instead of indices. Each key is unique, and it maps to a specific value. The value can be accessed by using the corresponding key.
Mutable vs Immutable:
List: Lists are mutable, which means their elements can be modified. Elements can be added, removed, or modified at any index position in the list.
Dictionary: Dictionaries are also mutable. Values can be added, removed, or modified by using their corresponding keys.
Duplicate Values:
List: Lists allow duplicate values. The same value can appear multiple times in a list.
Dictionary: Dictionary keys must be unique. Duplicate keys are not allowed, but different keys can have the same value.
Ordering:
List: Lists maintain the order of elements as they are inserted. The order of elements in a list will remain the same unless modified explicitly.
Dictionary: Dictionaries do not have a specific order. The elements are not stored in any particular order and can be accessed in any order.
Usage:
List: Lists are commonly used when the order of elements matters and when there may be duplicate values. They are useful for storing and manipulating collections of items.
Dictionary: Dictionaries are suitable when there is a need to store key-value pairs, especially when quick access to values based on a specific key is required.
Overall, lists are used for maintaining an ordered collection of items, while dictionaries are used for storing and accessing values using unique keys. The choice between lists and dictionaries depends on the specific requirements of the program and the type of data being stored.
 

#3b:
Ans:Here's an example to illustrate the usage of *args:
def sum_numbers(*args):
	total = 0
	for num in args:
    	total += num
	return total
 
print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5, 6, 7, 8))  # Output: 30
Consider the following example:
def display_info(**kwargs):
	for key, value in kwargs.items():
        print(f"{key}: {value}")
 
display_info(name="Alice", age=25, country="USA")
In this case, the display_info function accepts any number of keyword arguments. The **kwargs parameter collects these arguments as a dictionary, allowing you to access the key-value pairs within the function. In the example, it prints the information provided as keyword arguments.
You can also combine *args and **kwargs in a single function definition. In such cases, *args should come before **kwargs:
def process_data(*args, **kwargs):
	for arg in args:
    	print(arg)
	for key, value in kwargs.items():
        print(f"{key}: {value}")
 
process_data("apple", "banana", "orange", name="Alice", age=25)
In this example, the process_data function can accept both positional arguments (*args) and keyword arguments (**kwargs). It prints the positional arguments first and then iterates over the keyword arguments to display the key-value pairs.
Using *args and **kwargs provides flexibility and allows you to handle various scenarios when you need to work with a varying number of arguments or handle different types of arguments in your Python functions.
 

"""