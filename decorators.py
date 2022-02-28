# Decorator

# A function that takes function as an argument and return a function as its output
# Because of the @ syntax in Python, decorating a function replaces that function with
# the result of calling the decorator on the function.



# Function Wrapper

# Wrappers around the functions are also knows as decorators which are a very powerful 
# and useful tool in Python since it allows programmers to modify the behavior of function 
# or class.

# Example 1 :-
lines = '-' * 60 + '\n'

def with_lines(func):
    def wrapper():
        return f'{lines}{func()}{lines}'
    return wrapper

def a():
    return f'I am in a!\n'
new_a = with_lines(a)


def b():
    return f'I am in b!\n'
new_b = with_lines(b)

print(a())
print(b())
print(new_a())
print(new_b())

# Output :-
# I am in a!

# I am in b!

# ------------------------------------------------------------
# I am in a!
# ------------------------------------------------------------

# -----------------------------------------------------------------
# I am in b!
# -----------------------------------------------------------------


# Example 2 :- using @annotations to add some extra information to the function

lines = '-' * 60 + '\n'

def with_lines(func):
    def wrapper(*args, **kwargs):
        return f'{lines}{func(*args, **kwargs)}{lines}'
    return wrapper

@with_lines
def a():
    return f'I am in a!\n'
# a = with_lines(a)   # this line (after) is the same as @with_lines (before)


@with_lines
def b():
    return f'I am in b!\n'
# b = with_lines(b)  # this line (after) is the same as line 14

@with_lines
def add(x, y):
    return f'{x} + {y} = {x+y}\n'

print(a())
print(b())
print(add(3,5))  # add is actually wrapper! so when I call add(3,5), it's saying wrapper(3,5)

# OUTPUT :- 

# -----------------------------------------------------------------
# I am in a!
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# I am in b!
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# 3 + 5 = 8
# -----------------------------------------------------------------



# Example 3 :- Wrapper that filter even from list of ints


# Wrapper that filter even from list of ints
def only_evens(func):
    def wrapper(*args):
        even_numbers = [num for num in args if num % 2 == 0]
        print("\n\nWrapper added")
        print(f"even numbers {even_numbers}")
        result = f"sum of even numbers :- {func(*even_numbers)}"
        return result

    return wrapper



def add_nums(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print("Original add_nums function output :-",add_nums(1,2,3,4,5,6,7,8,9,10))

@only_evens
def add_nums(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print("Original add_nums function output :-",add_nums(1,2,3,4,5,6,7,8,9,10))

# Output :-
# Original add_nums function output :- 55


# Wrapper added
# even numbers [2, 4, 6, 8, 10]
# Original add_nums function output :- sum of even numbers :- 30