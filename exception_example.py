# Example 1:-

def type_test(num1, num2):
    try:
        a = int(num1)
        b = int(num2)
        print(a / b)
    except ValueError:
        print("Invalid input")

    finally:
        print("Done")

type_test(5, 2)
type_test(5,"Five")
    
# Output:
# 2
# Done
# Invalid input


# Example 2:-


def fibonacci(N):
    try:
        if N < 0:
            raise ValueError("N must be non-negative")
        L = []
        a, b = 0, 1
        while len(L) < N:
            a, b = b, a + b
            L.append(a)
        return L
    except ValueError as e:
        print(e)

    finally:
        print("Done")

print(fibonacci(10))
print(fibonacci(-1))

# Output:-
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# N must be non-negative
# Done
# None


# Example 3 program with mutiple except:-
def type_test2(num1, num2):
    try:
        a = int(num1)
        b = int(num2)
        print(a / b)
    except (ValueError, ZeroDivisionError) as e:
        print(e)

    finally:
        print("Done") 

type_test2(5, 2)
type_test2(5,"Five")
type_test2(5,0)

# Output:-
# 2
# Done
# invalid literal for int() with base 10: 'Five'
# Done
# integer division or modulo by zero
# Done


# Example 4 custom exception to prevent function call after 5 calls implementation without handling:-
class PhoneOverUsage(Exception):
    pass

class Phone:
    def __init__(self):
        self.counter = 0

    def no_of_times_used(self):
        self.counter += 1
        if self.counter > 5:
            raise PhoneOverUsage("Your daily limit to use the phone is over")
        return self.counter

# phone = Phone()
# print(f"Phone Used {phone.no_of_times_used()} times")
# print(f"Phone Used {phone.no_of_times_used()} times") this will throw exception as it is not handled
# print(f"Phone Used {phone.no_of_times_used()} times")
# print(f"Phone Used {phone.no_of_times_used()} times")
# print(f"Phone Used {phone.no_of_times_used()} times")
# print(f"Phone Used {phone.no_of_times_used()} times")

# Output:-
# Phone Used 1 times
# Phone Used 2 times
# Phone Used 3 times
# Phone Used 4 times
# Phone Used 5 times
# Traceback (most recent call last):
#   File "<string>", line 20, in <module>
# File "<string>", line 11, in no_of_times_used
# __main__.PhoneOverUsage: Your daily limit to use the phone is over


# Example 5 custom exception to prevent function call after 5 calls implementation with handling:-


try:
    phone2 = Phone()
    print(f"Phone Used {phone2.no_of_times_used()} times")
    print(f"Phone Used {phone2.no_of_times_used()} times")
    print(f"Phone Used {phone2.no_of_times_used()} times")
    print(f"Phone Used {phone2.no_of_times_used()} times")
    print(f"Phone Used {phone2.no_of_times_used()} times")
    print(f"Phone Used {phone2.no_of_times_used()} times")
except PhoneOverUsage as e:
    print(e)

finally:
    print("Exception handled : you can you the phone tommorow")


# Output:-
# Exception handled : you can you the phone tommorow


